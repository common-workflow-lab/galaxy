import json
import os
import shutil
import tempfile
from unittest import TestCase
from uuid import uuid4

import yaml

import galaxy.model
from galaxy.tool_util.cwl import (
    to_cwl_job,
    tool_proxy as real_tool_proxy,
    workflow_proxy,
)
from galaxy.tool_util.cwl.parser import (
    _to_cwl_tool_object,
    tool_proxy_from_persistent_representation,
)
from galaxy.tool_util.cwl.representation import USE_FIELD_TYPES
from galaxy.tool_util.parser.cwl import CWL_DEFAULT_FILE_OUTPUT
from galaxy.tool_util.parser.factory import get_tool_source
from galaxy.tools.parameters import populate_state
from galaxy.tools.parameters.wrapped import WrappedParameters
from .. import tools_support
from ..unittest_utils import galaxy_mock


TESTS_DIRECTORY = os.path.dirname(__file__)
CWL_TOOLS_DIRECTORY = os.path.abspath(os.path.join(TESTS_DIRECTORY, "cwl_tools"))


def tool_proxy(*args, **kwd):
    if 'uuid' not in kwd:
        kwd['uuid'] = str(uuid4())
    return real_tool_proxy(*args, **kwd)


def test_tool_proxy():
    """Test that tool proxies load some valid tools correctly."""
    tool_proxy(_cwl_tool_path("v1.0/v1.0/cat1-testcli.cwl"))
    tool_proxy(_cwl_tool_path("v1.0/v1.0/cat3-tool.cwl"))
    tool_proxy(_cwl_tool_path("v1.0/v1.0/env-tool1.cwl"))
    tool_proxy(_cwl_tool_path("v1.0/v1.0/sorttool.cwl"))
    tool_proxy(_cwl_tool_path("v1.0/v1.0/bwa-mem-tool.cwl"))
    tool_proxy(_cwl_tool_path("v1.0/v1.0/parseInt-tool.cwl"))


def test_tool_source_records():
    record_output_path = _cwl_tool_path("v1.0/v1.0/record-output.cwl")
    tool_source = get_tool_source(record_output_path)
    inputs = _inputs(tool_source)
    assert len(inputs) == 1, inputs

    output_data, output_collections = _outputs(tool_source)
    assert len(output_data) == 1
    assert len(output_collections) == 1


def test_serialize_deserialize():
    path = _cwl_tool_path("v1.0/v1.0/cat5-tool.cwl")
    tool = tool_proxy(path)
    expected_uuid = tool._uuid
    print(tool._tool.tool)
    rep = tool.to_persistent_representation()
    tool = tool_proxy_from_persistent_representation(rep)
    assert tool._uuid == expected_uuid
    print(tool)
    tool.job_proxy({"file1": "/moo"}, {})
    print(tool._tool.tool)

    with open(path) as f:
        tool_object = yaml.safe_load(f)
    tool_object = json.loads(json.dumps(tool_object))
    tool = _to_cwl_tool_object(tool_object=tool_object, uuid=expected_uuid)
    assert tool._uuid == expected_uuid


def test_job_proxy():
    bwa_parser = get_tool_source(_cwl_tool_path("v1.0/v1.0/bwa-mem-tool.cwl"))
    bwa_inputs = {
        "reference": {
            "class": "File",
            "location": _cwl_tool_path("v1.0/v1.0/chr20.fa"),
            "size": 123,
            "checksum": "sha1$hash"
        },
        "reads": [
            {
                "class": "File",
                "location": _cwl_tool_path("v1.0/v1.0/example_human_Illumina.pe_1.fastq")
            },
            {
                "class": "File",
                "location": _cwl_tool_path("v1.0/v1.0/example_human_Illumina.pe_2.fastq")
            }
        ],
        "min_std_max_min": [
            1,
            2,
            3,
            4
        ],
        "minimum_seed_length": 3
    }
    bwa_proxy = bwa_parser.tool_proxy
    bwa_id = bwa_parser.parse_id()

    job_proxy = bwa_proxy.job_proxy(
        bwa_inputs,
        {},
        "/",
    )

    cmd = job_proxy.command_line
    print(cmd)

    bind_parser = get_tool_source(_cwl_tool_path("v1.0/v1.0/binding-test.cwl"))
    binding_proxy = bind_parser.tool_proxy
    binding_id = bind_parser.parse_id()

    job_proxy = binding_proxy.job_proxy(
        bwa_inputs,
        {},
        "/",
    )

    cmd = job_proxy.command_line
    assert bwa_id != binding_id, bwa_id


def test_cores_min():
    sort_parser = get_tool_source(_cwl_tool_path("v1.0/v1.0/sorttool.cwl"))
    bwa_parser = get_tool_source(_cwl_tool_path("v1.0/v1.0/bwa-mem-tool.cwl"))

    assert sort_parser.parse_cores_min() == 1
    assert bwa_parser.parse_cores_min() == 2


def test_success_codes():
    exit_success_parser = get_tool_source(_cwl_tool_path("v1.0/v1.0/exit-success.cwl"))

    stdio, _ = exit_success_parser.parse_stdio()
    assert len(stdio) == 2
    stdio_0 = stdio[0]
    assert stdio_0.range_start == float("-inf")
    assert stdio_0.range_end == 0

    stdio_1 = stdio[1]
    assert stdio_1.range_start == 2
    assert stdio_1.range_end == float("inf")

    bwa_parser = get_tool_source(_cwl_tool_path("v1.0/v1.0/bwa-mem-tool.cwl"))
    stdio, _ = bwa_parser.parse_stdio()

    assert len(stdio) == 2
    stdio_0 = stdio[0]
    assert stdio_0.range_start == float("-inf")
    assert stdio_0.range_end == -1

    stdio_1 = stdio[1]
    assert stdio_1.range_start == 1
    assert stdio_1.range_end == float("inf")


def test_serialize_deserialize_workflow_embed():
    # Test inherited hints and requirements from workflow -> tool
    # work here.
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/count-lines2-wf.cwl"))
    step_proxies = proxy.step_proxies()
    tool_proxy = step_proxies[0].tool_proxy
    assert tool_proxy.requirements, tool_proxy.requirements


def test_reference_proxies():
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/count-lines1-wf.cwl"))
    proxy.tool_reference_proxies()


def test_subworkflow_parsing():
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/count-lines10-wf.cwl"))
    assert len(proxy.tool_reference_proxies()) == 2

    assert len(proxy.output_labels) == 1
    assert "count_output" in proxy.output_labels, proxy.output_labels

    galaxy_workflow_dict = proxy.to_dict()
    steps = galaxy_workflow_dict["steps"]
    assert len(steps) == 2  # One input, one subworkflow

    subworkflow_step = steps[1]
    assert subworkflow_step["type"] == "subworkflow"


def test_checks_is_a_tool():
    """Test that tool proxy cannot be created for a workflow."""
    exception = None
    try:
        tool_proxy(_cwl_tool_path("v1.0/v1.0/count-lines1-wf.cwl"))
    except Exception as e:
        exception = e

    assert exception is not None
    assert "CommandLineTool" in str(exception), str(exception)


def test_workflow_of_files_proxy():
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/count-lines1-wf.cwl"))
    step_proxies = proxy.step_proxies()
    assert len(step_proxies) == 2

    galaxy_workflow_dict = proxy.to_dict()

    assert len(proxy.runnables) == 2

    assert len(galaxy_workflow_dict["steps"]) == 3
    wc_step = galaxy_workflow_dict["steps"][1]
    exp_step = galaxy_workflow_dict["steps"][2]
    assert wc_step["input_connections"]
    assert exp_step["input_connections"]


def test_workflow_embedded_tools_proxy():
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/count-lines2-wf.cwl"))
    step_proxies = proxy.step_proxies()
    assert len(step_proxies) == 2
    print(step_proxies[1].requirements)
    print(step_proxies[1]._step.embedded_tool.requirements)
    galaxy_workflow_dict = proxy.to_dict()

    assert len(proxy.runnables) == 2
    print(proxy.runnables[1])

    assert len(galaxy_workflow_dict["steps"]) == 3
    wc_step = galaxy_workflow_dict["steps"][1]
    exp_step = galaxy_workflow_dict["steps"][2]
    assert wc_step["input_connections"]
    assert exp_step["input_connections"]


def test_workflow_scatter():
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/count-lines3-wf.cwl"))

    step_proxies = proxy.step_proxies()
    assert len(step_proxies) == 1

    galaxy_workflow_dict = proxy.to_dict()
    assert len(galaxy_workflow_dict["steps"]) == 2

    # TODO: For CWL - deactivate implicit scattering Galaxy does
    # and force annotation in the workflow of scattering? Maybe?
    wc_step = galaxy_workflow_dict["steps"][1]
    assert wc_step["input_connections"]

    assert "inputs" in wc_step
    wc_inputs = wc_step["inputs"]
    assert len(wc_inputs) == 1
    file_input = wc_inputs[0]
    assert file_input["scatter_type"] == "dotproduct", wc_step

    assert len(wc_step["workflow_outputs"]) == 1


def test_workflow_outputs_of_inputs():
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/any-type-compat.cwl"))

    galaxy_workflow_dict = proxy.to_dict()
    assert len(galaxy_workflow_dict["steps"]) == 3
    input_step = galaxy_workflow_dict["steps"][0]

    assert len(input_step["workflow_outputs"]) == 1


def test_workflow_scatter_multiple_input():
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/count-lines4-wf.cwl"))

    step_proxies = proxy.step_proxies()
    assert len(step_proxies) == 1

    galaxy_workflow_dict = proxy.to_dict()
    assert len(galaxy_workflow_dict["steps"]) == 3


def test_workflow_multiple_input_merge_flattened():
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/count-lines7-wf.cwl"))

    galaxy_workflow_dict = proxy.to_dict()
    assert len(galaxy_workflow_dict["steps"]) == 3

    tool_step = galaxy_workflow_dict["steps"][2]
    assert "inputs" in tool_step
    inputs = tool_step["inputs"]
    assert len(inputs) == 1
    input = inputs[0]
    assert input["merge_type"] == "merge_flattened"


def test_workflow_step_value_from():
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/step-valuefrom-wf.cwl"))

    galaxy_workflow_dict = proxy.to_dict()
    assert len(galaxy_workflow_dict["steps"]) == 3

    print(galaxy_workflow_dict["steps"])
    tool_step = [s for s in galaxy_workflow_dict["steps"].values() if s["label"] == "step1"][0]
    assert "inputs" in tool_step
    inputs = tool_step["inputs"]
    assert len(inputs) == 1
    assert "value_from" in inputs[0], inputs


def test_workflow_input_without_source():
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/step-valuefrom3-wf.cwl"))

    galaxy_workflow_dict = proxy.to_dict()
    assert len(galaxy_workflow_dict["steps"]) == 3

    tool_step = galaxy_workflow_dict["steps"][2]
    assert "inputs" in tool_step
    inputs = tool_step["inputs"]
    assert len(inputs) == 3, inputs
    assert inputs[2].get("value_from")


def test_workflow_input_default():
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/pass-unconnected.cwl"))
    galaxy_workflow_dict = proxy.to_dict()
    assert len(galaxy_workflow_dict["steps"]) == 3

    tool_step = galaxy_workflow_dict["steps"][2]

    assert "inputs" in tool_step
    inputs = tool_step["inputs"]
    assert len(inputs) == 2, inputs
    assert inputs[1]


def test_search_workflow():
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/search.cwl#main"))
    galaxy_workflow_dict = proxy.to_dict()
    assert len(galaxy_workflow_dict["steps"]) == 5


def test_workflow_simple_optional_input():
    proxy = workflow_proxy(_cwl_tool_path("v1.0_custom/int-opt-io-wf.cwl"))

    galaxy_workflow_dict = proxy.to_dict()
    assert len(galaxy_workflow_dict["steps"]) == 2

    input_step = galaxy_workflow_dict["steps"][0]
    assert input_step['type'] == "parameter_input", input_step
    assert input_step['tool_state']['parameter_type'] == "field", input_step


def test_boolean_defaults():
    proxy = workflow_proxy(_cwl_tool_path("v1.2/tests/conditionals/cond-wf-002_nojs.cwl"))
    galaxy_workflow_dict = proxy.to_dict()
    assert len(galaxy_workflow_dict["steps"]) == 3
    bool_input = galaxy_workflow_dict["steps"][0]
    assert bool_input["label"] == "test", bool_input
    bool_tool_state = bool_input["tool_state"]
    assert bool_tool_state["optional"]
    assert bool_tool_state["default"]["value"] is False


def test_workflow_file_optional_input():
    proxy = workflow_proxy(_cwl_tool_path("v1.0/v1.0/count-lines11-wf.cwl"))

    galaxy_workflow_dict = proxy.to_dict()
    assert len(galaxy_workflow_dict["steps"]) == 3

    input_step = galaxy_workflow_dict["steps"][0]
    # TODO: make this File? - implemented in Galaxy now
    assert input_step['type'] == "parameter_input", input_step
    assert input_step['tool_state']['optional'] is True, input_step


def test_load_proxy_simple():
    cat3 = _cwl_tool_path("v1.0/v1.0/cat3-tool.cwl")
    tool_source = get_tool_source(cat3)

    # Behavior was changed - too verbose?
    # description = tool_source.parse_description()
    # assert description == "Print the contents of a file to stdout using 'cat' running in a docker container.", description

    input_sources = _inputs(tool_source)
    assert len(input_sources) == 1

    input_source = input_sources[0]
    assert input_source.parse_help() == "The file that will be copied using 'cat'"
    assert input_source.parse_label() == "Input File"

    outputs, output_collections = tool_source.parse_outputs(None)
    assert len(outputs) == 1

    output1 = outputs['output_file']
    assert output1.format == CWL_DEFAULT_FILE_OUTPUT, output1.format  # Have Galaxy auto-detect

    _, containers = tool_source.parse_requirements_and_containers()
    assert len(containers) == 1


def test_cwl_strict_parsing():
    md5sum_non_strict_path = _cwl_tool_path("v1.0_custom/md5sum_non_strict.cwl")
    threw_exception = False
    try:
        get_tool_source(md5sum_non_strict_path).tool_proxy
    except Exception:
        threw_exception = True

    assert threw_exception
    get_tool_source(md5sum_non_strict_path, strict_cwl_validation=False).tool_proxy


def test_load_proxy_bwa_mem():
    bwa_mem = _cwl_tool_path("v1.0/v1.0/bwa-mem-tool.cwl")
    tool_source = get_tool_source(bwa_mem)
    tool_id = tool_source.parse_id()
    assert tool_id == "bwa-mem-tool.cwl", tool_id
    _inputs(tool_source)
    # TODO: test repeat generated...


def test_representation_id():
    cat3 = _cwl_tool_path("v1.0/v1.0/cat3-tool.cwl")
    with open(cat3) as f:
        representation = yaml.safe_load(f)
        representation["id"] = "my-cool-id"

        uuid = str(uuid4())
        proxy = tool_proxy(tool_object=representation, tool_directory="/", uuid=uuid)
        tool_id = proxy.galaxy_id()
        # assert tool_id == "my-cool-id", tool_id
        assert tool_id == uuid, tool_id
        id_proxy = tool_proxy_from_persistent_representation(proxy.to_persistent_representation())
        tool_id = id_proxy.galaxy_id()
        assert tool_id == uuid, tool_id
        assert proxy._uuid == id_proxy._uuid
        # assert tool_id == "my-cool-id", tool_id


def test_env_tool1():
    env_tool1 = _cwl_tool_path("v1.0/v1.0/env-tool1.cwl")
    tool_source = get_tool_source(env_tool1)
    _inputs(tool_source)


def test_wc2_tool():
    env_tool1 = _cwl_tool_path("v1.0/v1.0/wc2-tool.cwl")
    tool_source = get_tool_source(env_tool1)
    _inputs(tool_source)
    datasets, collections = _outputs(tool_source)
    assert len(datasets) == 1, datasets
    output = datasets["output"]
    assert output.format == "expression.json", output.format


def test_optional_output():
    optional_output2_tool1 = _cwl_tool_path("v1.0/v1.0/optional-output.cwl")
    tool_source = get_tool_source(optional_output2_tool1)
    datasets, collections = _outputs(tool_source)
    assert len(datasets) == 2, datasets
    output = datasets["optional_file"]
    assert output.format == CWL_DEFAULT_FILE_OUTPUT, output.format


def test_sorttool():
    env_tool1 = _cwl_tool_path("v1.0/v1.0/sorttool.cwl")
    tool_source = get_tool_source(env_tool1)

    assert tool_source.parse_id() == "sorttool.cwl"

    inputs = _inputs(tool_source)
    assert len(inputs) == 2
    bool_input = inputs[0]
    file_input = inputs[1]
    assert bool_input.parse_input_type() == "param"
    assert bool_input.get("type") == "boolean"

    assert file_input.parse_input_type() == "param"
    assert file_input.get("type") == "data", file_input.get("type")

    output_data, output_collections = _outputs(tool_source)
    assert len(output_data) == 1
    assert len(output_collections) == 0


def test_scheadef_tool():
    tool_path = _cwl_tool_path("v1.0/v1.0/schemadef-tool.cwl")
    tool_source = get_tool_source(tool_path)
    _inputs(tool_source)


def test_params_tool():
    tool_path = _cwl_tool_path("v1.0/v1.0/params.cwl")
    tool_source = get_tool_source(tool_path)
    _inputs(tool_source)


def test_cat1():
    cat1_tool = _cwl_tool_path("v1.0/v1.0/cat1-testcli.cwl")
    tool_source = get_tool_source(cat1_tool)
    inputs = _inputs(tool_source)

    assert len(inputs) == 3, inputs
    file_input = inputs[0]

    assert file_input.parse_input_type() == "param"
    assert file_input.get("type") == "data", file_input.get("type")

    # User needs to specify if want to select boolean or not.
    if not USE_FIELD_TYPES:
        null_or_bool_input = inputs[1]
        assert null_or_bool_input.parse_input_type() == "conditional"
    else:
        field_input = inputs[1]
        assert field_input.parse_input_type() == "param"
        assert field_input.get("type") == "field", field_input.get("type")

    output_data, output_collections = _outputs(tool_source)
    assert len(output_data) == 1
    assert len(output_collections) == 1


def test_tool_reload():
    cat1_tool = _cwl_tool_path("v1.0/v1.0/cat1-testcli.cwl")
    tool_source = get_tool_source(cat1_tool)
    _inputs(tool_source)

    # Test reloading - had a regression where this broke down.
    cat1_tool_again = _cwl_tool_path("v1.0/v1.0/cat1-testcli.cwl")
    tool_source = get_tool_source(cat1_tool_again)
    _inputs(tool_source)


class CwlToolObjectTestCase(TestCase, tools_support.UsesApp, tools_support.UsesTools):

    def setUp(self):
        self.test_directory = tempfile.mkdtemp()
        self.app = galaxy_mock.MockApp()
        self.history = galaxy.model.History()
        self.trans = galaxy_mock.MockTrans(history=self.history)

    def tearDown(self):
        shutil.rmtree(self.test_directory)

    def test_default_data_inputs(self):
        self._init_tool(tool_path=_cwl_tool_path("v1.0/v1.0/default_path.cwl"))
        print("TOOL IS %s" % self.tool)
        hda = self._new_hda()
        errors = {}
        cwl_inputs = {
            "file1": {"src": "hda", "id": self.app.security.encode_id(hda.id)}
        }
        inputs = self.tool.inputs_from_dict({"inputs": cwl_inputs, "inputs_representation": "cwl"})
        print(inputs)
        print("pre-populated state is %s" % inputs)
        populated_state = {}
        populate_state(self.trans, self.tool.inputs, inputs, populated_state, errors)
        print("populated state is %s" % inputs)
        wrapped_params = WrappedParameters(self.trans, self.tool, populated_state)
        input_json = to_cwl_job(self.tool, wrapped_params.params, self.test_directory)
        print(inputs)
        print("to_cwl_job is %s" % input_json)
        # assert False

    def _new_hda(self):
        hda = galaxy.model.HistoryDatasetAssociation(history=self.history)
        hda.visible = True
        hda.dataset = galaxy.model.Dataset()
        self.trans.model.context.add(hda)
        self.trans.model.context.flush()
        return hda


def _outputs(tool_source):
    return tool_source.parse_outputs(object())


def get_cwl_tool_source(path):
    path = _cwl_tool_path(path)
    return get_tool_source(path)


def _inputs(tool_source=None, path=None):
    if tool_source is None:
        path = _cwl_tool_path(path)
        tool_source = get_tool_source(path)

    input_pages = tool_source.parse_input_pages()
    assert input_pages.inputs_defined
    page_sources = input_pages.page_sources
    assert len(page_sources) == 1
    page_source = page_sources[0]
    input_sources = page_source.parse_input_sources()
    return input_sources


def _cwl_tool_path(path):
    return os.path.join(CWL_TOOLS_DIRECTORY, path)
