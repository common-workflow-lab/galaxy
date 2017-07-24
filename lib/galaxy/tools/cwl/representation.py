""" This module is responsible for converting between Galaxy's tool
input description and the CWL description for a job json. """

import collections
import json
import logging
import os

from six import string_types

from galaxy.exceptions import RequestParameterInvalidException
from galaxy.util import safe_makedirs, string_as_bool
from galaxy.util.bunch import Bunch

log = logging.getLogger(__name__)

NOT_PRESENT = object()

NO_GALAXY_INPUT = object()

INPUT_TYPE = Bunch(
    DATA="data",
    INTEGER="integer",
    FLOAT="float",
    TEXT="text",
    BOOLEAN="boolean",
    SELECT="select",
    CONDITIONAL="conditional",
    DATA_COLLECTON="data_collection",
)

TypeRepresentation = collections.namedtuple("TypeRepresentation", ["name", "galaxy_param_type", "label", "collection_type"])
TYPE_REPRESENTATIONS = [
    TypeRepresentation("null", NO_GALAXY_INPUT, "no input", None),
    TypeRepresentation("integer", INPUT_TYPE.INTEGER, "an integer", None),
    TypeRepresentation("float", INPUT_TYPE.FLOAT, "a decimal number", None),
    TypeRepresentation("file", INPUT_TYPE.DATA, "a dataset", None),
    TypeRepresentation("boolean", INPUT_TYPE.BOOLEAN, "a boolean", None),
    TypeRepresentation("text", INPUT_TYPE.TEXT, "a simple text field", None),
    TypeRepresentation("record", INPUT_TYPE.DATA_COLLECTON, "record as a dataset collection", "record"),
    TypeRepresentation("json", INPUT_TYPE.TEXT, "arbitrary JSON structure", None),
    TypeRepresentation("array", INPUT_TYPE.DATA_COLLECTON, "as a dataset list", "list"),
]
TypeRepresentation.uses_param = lambda self: self.galaxy_param_type is not NO_GALAXY_INPUT

CWL_TYPE_TO_REPRESENTATIONS = {
    "Any": ["integer", "float", "file", "boolean", "text", "record", "json"],
    "array": ["array"],
    "string": ["text"],
    "boolean": ["boolean"],
    "int": ["integer"],
    "float": ["float"],
    "File": ["file"],
    "null": ["null"],
    "record": ["record"],
}


def type_representation_from_name(type_representation_name):
    for type_representation in TYPE_REPRESENTATIONS:
        if type_representation.name == type_representation_name:
            return type_representation

    assert False


def type_descriptions_for_field_types(field_types):
    type_representation_names = set([])
    for field_type in field_types:
        type_representation_names_for_field_type = CWL_TYPE_TO_REPRESENTATIONS.get(field_type)
        assert type_representation_names_for_field_type is not None, field_type
        type_representation_names.update(type_representation_names_for_field_type)
    type_representations = []
    for type_representation in TYPE_REPRESENTATIONS:
        if type_representation.name in type_representation_names:
            type_representations.append(type_representation)
    return type_representations


def to_cwl_job(tool, param_dict, local_working_directory):
    """ tool is Galaxy's representation of the tool and param_dict is the
    parameter dictionary with wrapped values.
    """
    tool_proxy = tool._cwl_tool_proxy
    input_fields = tool_proxy.input_fields()
    inputs = tool.inputs
    input_json = {}

    inputs_dir = os.path.join(local_working_directory, "_inputs")

    def simple_value(input, param_dict_value, type_representation_name=None):
        type_representation = type_representation_from_name(type_representation_name)
        # Hmm... cwl_type isn't really the cwl type in every case,
        # like in the case of json for instance.

        def dataset_wrapper_to_file_json(dataset_wrapper):
            extra_files_path = dataset_wrapper.extra_files_path
            secondary_files_path = os.path.join(extra_files_path, "__secondary_files__")
            path = str(dataset_wrapper)
            if os.path.exists(secondary_files_path):
                safe_makedirs(inputs_dir)
                name = os.path.basename(path)
                new_input_path = os.path.join(inputs_dir, name)
                os.symlink(path, new_input_path)
                for secondary_file_name in os.listdir(secondary_files_path):
                    secondary_file_path = os.path.join(secondary_files_path, secondary_file_name)
                    os.symlink(secondary_file_path, new_input_path + secondary_file_name)
                path = new_input_path

            return {"location": path,
                    "class": "File"}

        if type_representation.galaxy_param_type == NO_GALAXY_INPUT:
            assert param_dict_value is None
            return None

        if type_representation.name == "file":
            dataset_wrapper = param_dict_value
            return dataset_wrapper_to_file_json(dataset_wrapper)
        elif type_representation.name == "integer":
            return int(str(param_dict_value))
        elif type_representation.name == "long":
            return int(str(param_dict_value))
        elif type_representation.name == "float":
            return float(str(param_dict_value))
        elif type_representation.name == "boolean":
            return string_as_bool(param_dict_value)
        elif type_representation.name == "text":
            return str(param_dict_value)
        elif type_representation.name == "json":
            raw_value = param_dict_value.value
            return json.loads(raw_value)
        elif type_representation.name == "record":
            rval = dict()  # TODO: THIS NEEDS TO BE ORDERED BUT odict not json serializable!
            for key, value in param_dict_value.items():
                rval[key] = dataset_wrapper_to_file_json(value)
            return rval
        else:
            return str(param_dict_value)

    for input_name, input in inputs.iteritems():
        if input.type == "repeat":
            only_input = input.inputs.values()[0]
            array_value = []
            for instance in param_dict[input_name]:
                array_value.append(simple_value(only_input, instance[input_name[:-len("_repeat")]]))
            input_json[input_name[:-len("_repeat")]] = array_value
        elif input.type == "conditional":
            assert input_name in param_dict, "No value for %s in %s" % (input_name, param_dict)
            current_case = param_dict[input_name]["_cwl__type_"]
            if str(current_case) != "null":  # str because it is a wrapped...
                case_index = input.get_current_case( current_case )
                case_input = input.cases[ case_index ].inputs["_cwl__value_"]
                case_value = param_dict[input_name]["_cwl__value_"]
                input_json[input_name] = simple_value(case_input, case_value, current_case)
        else:
            matched_field = None
            for field in input_fields:
                if field["name"] == input_name:
                    matched_field = field
            field_type = field_to_field_type(matched_field)
            assert not isinstance(field_type, list)
            type_descriptions = type_descriptions_for_field_types([field_type])
            assert len(type_descriptions) == 1
            type_description_name = type_descriptions[0].name
            input_json[input_name] = simple_value(input, param_dict[input_name], type_description_name)

    return input_json


def to_galaxy_parameters(tool, as_dict):
    """ Tool is Galaxy's representation of the tool and as_dict is a Galaxified
    representation of the input json (no paths, HDA references for instance).
    """
    inputs = tool.inputs
    galaxy_request = {}

    def from_simple_value(input, param_dict_value, type_representation_name=None):
        if type_representation_name == "json":
            return json.dumps(param_dict_value)
        else:
            return param_dict_value

    for input_name, input in inputs.iteritems():
        as_dict_value = as_dict.get(input_name, NOT_PRESENT)
        galaxy_input_type = input.type

        if galaxy_input_type == "repeat":
            if input_name not in as_dict:
                continue

            only_input = input.inputs.values()[0]
            for index, value in enumerate(as_dict_value):
                key = "%s_repeat_0|%s" % (input_name, only_input.name)
                galaxy_value = from_simple_value(only_input, value)
                galaxy_request[key] = galaxy_value
        elif galaxy_input_type == "conditional":
            case_strings = input.case_strings
            # TODO: less crazy handling of defaults...
            if (as_dict_value is NOT_PRESENT or as_dict_value is None) and "null" in case_strings:
                type_representation_name = "null"
            elif (as_dict_value is NOT_PRESENT or as_dict_value is None):
                raise RequestParameterInvalidException(
                    "Cannot translate CWL datatype - value [%s] of type [%s] with case_strings [%s]. Non-null property must be set." % (
                        as_dict_value, type(as_dict_value), case_strings
                    )
                )
            elif isinstance(as_dict_value, bool) and "boolean" in case_strings:
                type_representation_name = "boolean"
            elif isinstance(as_dict_value, int) and "integer" in case_strings:
                type_representation_name = "integer"
            elif isinstance(as_dict_value, int) and "long" in case_strings:
                type_representation_name = "long"
            elif isinstance(as_dict_value, (int, float)) and "float" in case_strings:
                type_representation_name = "float"
            elif isinstance(as_dict_value, (int, float)) and "double" in case_strings:
                type_representation_name = "double"
            elif isinstance(as_dict_value, string_types) and "string" in case_strings:
                type_representation_name = "string"
            elif isinstance(as_dict_value, dict) and "src" in as_dict_value and "id" in as_dict_value and "file" in case_strings:
                type_representation_name = "file"
            elif "json" in case_strings and as_dict_value is not None:
                type_representation_name = "json"
            else:
                raise RequestParameterInvalidException(
                    "Cannot translate CWL datatype - value [%s] of type [%s] with case_strings [%s]." % (
                        as_dict_value, type(as_dict_value), case_strings
                    )
                )
            galaxy_request["%s|_cwl__type_" % input_name] = type_representation_name
            if type_representation_name != "null":
                current_case_index = input.get_current_case(type_representation_name)
                current_case_inputs = input.cases[ current_case_index ].inputs
                current_case_input = current_case_inputs[ "_cwl__value_" ]
                galaxy_value = from_simple_value(current_case_input, as_dict_value, type_representation_name)
                galaxy_request["%s|_cwl__value_" % input_name] = galaxy_value
        elif as_dict_value is NOT_PRESENT:
            continue
        else:
            galaxy_value = from_simple_value(input, as_dict_value)
            galaxy_request[input_name] = galaxy_value

    log.info("Converted galaxy_request is %s" % galaxy_request)
    return galaxy_request


def field_to_field_type(field):
    field_type = field["type"]
    if isinstance(field_type, dict):
        field_type = field_type["type"]
    if isinstance(field_type, list):
        field_type_length = len(field_type)
        if field_type_length == 0:
            raise Exception("Zero-length type list encountered, invalid CWL?")
        elif len(field_type) == 1:
            field_type = field_type[0]

    return field_type
