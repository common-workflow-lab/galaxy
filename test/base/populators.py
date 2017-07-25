import json
import os.path
import time

from operator import itemgetter

import requests
import yaml

from pkg_resources import resource_string
from six import iteritems, StringIO

from base import api_asserts
from base.workflows_format_2 import (
    convert_and_import_workflow,
    ImporterGalaxyInterface,
)

# Simple workflow that takes an input and call cat wrapper on it.
workflow_str = resource_string( __name__, "data/test_workflow_1.ga" )
# Simple workflow that takes an input and filters with random lines twice in a
# row - first grabbing 8 lines at random and then 6.
workflow_random_x2_str = resource_string( __name__, "data/test_workflow_2.ga" )


DEFAULT_TIMEOUT = 60  # Secs to wait for state to turn ok


def skip_without_tool( tool_id ):
    """ Decorate an API test method as requiring a specific tool,
    have nose skip the test case is the tool is unavailable.
    """

    def method_wrapper( method ):

        def get_tool_ids( api_test_case ):
            index = api_test_case.galaxy_interactor.get( "tools", data=dict(in_panel=False) )
            tools = index.json()
            # In panels by default, so flatten out sections...
            tool_ids = [itemgetter( "id" )(_) for _ in tools]
            return tool_ids

        def wrapped_method( api_test_case, *args, **kwargs ):
            if tool_id not in get_tool_ids( api_test_case ):
                from nose.plugins.skip import SkipTest
                raise SkipTest( )

            return method( api_test_case, *args, **kwargs )

        # Must preserve method name so nose can detect and report tests by
        # name.
        wrapped_method.__name__ = method.__name__
        return wrapped_method

    return method_wrapper


# Now this is the newer than the planemo version of this function as of 2017/7/18
def galactic_job_json(job, test_data_directory, upload_func, collection_create_func):
    datasets = []
    dataset_collections = []

    def upload_file(file_path):
        if not os.path.isabs(file_path):
            file_path = os.path.join(test_data_directory, file_path)
        _ensure_file_exists(file_path)
        upload_response = upload_func(FileUploadTarget(file_path))
        dataset = upload_response["outputs"][0]
        datasets.append((dataset, file_path))
        dataset_id = dataset["id"]
        return {"src": "hda", "id": dataset_id}

    def upload_object(the_object):
        upload_response = upload_func(ObjectUploadTarget(the_object))
        dataset = upload_response["outputs"][0]
        datasets.append((dataset, the_object))
        dataset_id = dataset["id"]
        return {"src": "hda", "id": dataset_id}

    def replacement_item(value, force_to_file=False):
        if force_to_file:
            return upload_object(value)

        if isinstance(value, list):
            return replacement_list(value)
        elif not isinstance(value, dict):
            return value

        type_class = value.get("class", None)
        if type_class == "File":
            return replacement_file(value)
        else:
            return replacement_record(value)

    def replacement_file(value):
        file_path = value.get("location", None) or value.get("path", None)
        if file_path is None:
            return value

        return upload_file(file_path)

    def replacement_list(value):
        collection_element_identifiers = []
        for i, item in enumerate(value):
            dataset = replacement_item(item, force_to_file=True)
            collection_element = dataset.copy()
            collection_element["name"] = str(i)
            collection_element_identifiers.append(collection_element)

        collection = collection_create_func(collection_element_identifiers, "list")
        dataset_collections.append(collection)
        hdca_id = collection["id"]
        return {"src": "hdca", "id": hdca_id}

    def replacement_record(value):
        collection_element_identifiers = []
        for record_key, record_value in value.items():
            if record_value.get("class") != "File":
                raise NotImplementedError()

            dataset = upload_file(record_value["location"])
            collection_element = dataset.copy()
            collection_element["name"] = record_key
            collection_element_identifiers.append(collection_element)

        collection = collection_create_func(collection_element_identifiers, "record")
        dataset_collections.append(collection)
        hdca_id = collection["id"]
        return {"src": "hdca", "id": hdca_id}

    replace_keys = {}
    for key, value in iteritems(job):
        replace_keys[key] = replacement_item(value)

    job.update(replace_keys)
    return job, datasets


def _ensure_file_exists(file_path):
    if not os.path.exists(file_path):
        template = "File [%s] does not exist - parent directory [%s] does %sexist, cwd is [%s]"
        parent_directory = os.path.dirname(file_path)
        message = template % (
            file_path,
            parent_directory,
            "" if os.path.exists(parent_directory) else "not ",
            os.getcwd(),
        )
        raise Exception(message)


# Deprecated mixin, use dataset populator instead.
# TODO: Rework existing tests to target DatasetPopulator in a setup method instead.
class TestsDatasets:

    def _new_dataset( self, history_id, content='TestData123', **kwds ):
        return DatasetPopulator( self.galaxy_interactor ).new_dataset( history_id, content=content, **kwds)

    def _wait_for_history( self, history_id, assert_ok=False ):
        return DatasetPopulator( self.galaxy_interactor ).wait_for_history( history_id, assert_ok=assert_ok )

    def _new_history( self, **kwds ):
        return DatasetPopulator( self.galaxy_interactor ).new_history( **kwds )

    def _upload_payload( self, history_id, content, **kwds ):
        return DatasetPopulator( self.galaxy_interactor ).upload_payload( history_id, content, **kwds )

    def _run_tool_payload( self, tool_id, inputs, history_id, **kwds ):
        return DatasetPopulator( self.galaxy_interactor ).run_tool_payload( tool_id, inputs, history_id, **kwds )


class CwlToolRun( object ):

    def __init__( self, history_id, run_response ):
        self.history_id = history_id
        self.run_response = run_response

    @property
    def job_id( self ):
        return self.run_response[ "jobs" ][ 0 ][ "id" ]

    def output(self, output_index):
        return self.run_response["outputs"][output_index]

    def output_collection(self, output_index):
        return self.run_response["output_collections"][output_index]


class CwlWorkflowRun( object ):

    def __init__(self, workflow_id, invocation_id):
        self.workflow_id = workflow_id
        self.invocation_id = invocation_id


class BaseDatasetPopulator( object ):
    """ Abstract description of API operations optimized for testing
    Galaxy - implementations must implement _get and _post.
    """

    def new_dataset( self, history_id, content='TestData123', wait=False, **kwds ):
        run_response = self.new_dataset_request(history_id, content=content, wait=wait, **kwds)
        return run_response["outputs"][0]

    def new_dataset_request( self, history_id, content='TestData123', wait=False, **kwds ):
        payload = self.upload_payload( history_id, content, **kwds )
        run_response = self._post( "tools", data=payload ).json()
        if wait:
            job = run_response["jobs"][0]
            self.wait_for_job(job["id"])
            self.wait_for_history(history_id, assert_ok=True)
        return run_response

    def wait_for_history( self, history_id, assert_ok=False, timeout=DEFAULT_TIMEOUT ):
        try:
            return wait_on_state( lambda: self._get( "histories/%s" % history_id ), assert_ok=assert_ok, timeout=timeout )
        except AssertionError:
            self._summarize_history_errors( history_id )
            raise

    def wait_for_job( self, job_id, assert_ok=False, timeout=DEFAULT_TIMEOUT ):
        return wait_on_state( lambda: self.get_job_details( job_id ), assert_ok=assert_ok, timeout=timeout )

    def get_job_details( self, job_id, full=False ):
        return self._get( "jobs/%s?full=%s" % (job_id, full) )

    def _summarize_history_errors( self, history_id ):
        pass

    def new_history( self, **kwds ):
        name = kwds.get( "name", "API Test History" )
        create_history_response = self._post( "histories", data=dict( name=name ) )
        history_id = create_history_response.json()[ "id" ]
        return history_id

    def upload_payload( self, history_id, content, **kwds ):
        name = kwds.get( "name", "Test Dataset" )
        dbkey = kwds.get( "dbkey", "?" )
        file_type = kwds.get( "file_type", 'txt' )
        upload_params = {
            'files_0|NAME': name,
            'dbkey': dbkey,
            'file_type': file_type,
        }
        if hasattr(content, 'read'):
            upload_params[ "files_0|file_data"] = content
        else:
            upload_params[ 'files_0|url_paste' ] = content

        if "to_posix_lines" in kwds:
            upload_params[ "files_0|to_posix_lines"] = kwds[ "to_posix_lines" ]
        if "space_to_tab" in kwds:
            upload_params[ "files_0|space_to_tab" ] = kwds[ "space_to_tab" ]
        return self.run_tool_payload(
            tool_id='upload1',
            inputs=upload_params,
            history_id=history_id,
            upload_type='upload_dataset'
        )

    def run_tool_payload( self, tool_id, inputs, history_id, **kwds ):
        if "files_0|file_data" in inputs:
            kwds[ "__files" ] = { "files_0|file_data": inputs[ "files_0|file_data" ] }
            del inputs[ "files_0|file_data" ]

        ir = kwds.get("inputs_representation", None)
        if ir is None and "inputs_representation" in kwds:
            del kwds["inputs_representation"]

        return dict(
            tool_id=tool_id,
            inputs=json.dumps(inputs),
            history_id=history_id,
            **kwds
        )

    def run_tool( self, tool_id, inputs, history_id, assert_ok=True, **kwds ):
        payload = self.run_tool_payload( tool_id, inputs, history_id, **kwds )
        tool_response = self._post( "tools", data=payload )
        if assert_ok:
            api_asserts.assert_status_code_is( tool_response, 200 )
            return tool_response.json()
        else:
            return tool_response

    def run_cwl_artifact(
        self, tool_id, json_path=None, job=None, test_data_directory=None, history_id=None, assert_ok=True, tool_or_workflow="tool",
    ):
        if test_data_directory is None and json_path is not None:
            test_data_directory = os.path.dirname(json_path)
        if json_path is not None:
            assert job is None
            with open( json_path, "r" ) as f:
                if json_path.endswith(".yml") or json_path.endswith(".yaml"):
                    job_as_dict = yaml.load( f )
                else:
                    job_as_dict = json.load( f )
        else:
            job_as_dict = job
        if history_id is None:
            history_id = self.new_history()

        def upload_func(upload_target):
            if isinstance(upload_target, FileUploadTarget):
                path = upload_target.path
                with open( path, "rb" ) as f:
                    content = f.read()
                return self.new_dataset_request(
                    history_id=history_id,
                    content=content,
                    file_type="auto",
                )
            else:
                content = json.dumps(upload_target.object)
                return self.new_dataset_request(
                    history_id=history_id,
                    content=content,
                    file_type="expression.json",
                )

        def create_collection_func(element_identifiers, collection_type):
            payload = {
                "name": "dataset collection",
                "instance_type": "history",
                "history_id": history_id,
                "element_identifiers": json.dumps(element_identifiers),
                "collection_type": collection_type,
                "fields": None if collection_type != "record" else "auto",
            }
            response = self._post( "dataset_collections", data=payload )
            assert response.status_code == 200
            return response.json()

        job_as_dict, datasets_uploaded = galactic_job_json(
            job_as_dict,
            test_data_directory,
            upload_func,
            create_collection_func,
        )
        if datasets_uploaded:
            self.wait_for_history( history_id=history_id, assert_ok=True )
        if tool_or_workflow == "tool":
            run_response = self.run_tool( tool_id, job_as_dict, history_id, inputs_representation="cwl", assert_ok=assert_ok )
            run_object = CwlToolRun( history_id, run_response )
            if assert_ok:
                try:
                    final_state = self.wait_for_job( run_object.job_id )
                    assert final_state == "ok"
                except Exception:
                    self._summarize_history_errors( history_id )
                    raise

            return run_object
        else:
            route = "workflows"
            path = os.path.join(tool_id)
            data = dict(
                from_path=path,
            )
            upload_response = self._post(route, data=data)
            api_asserts.assert_status_code_is(upload_response, 200)
            workflow = upload_response.json()
            workflow_id = workflow["id"]

            workflow_request = dict(
                history="hist_id=%s" % history_id,
                workflow_id=workflow_id,
                inputs=json.dumps(job_as_dict),
                inputs_by="name",
            )
            url = "workflows/%s/invocations" % workflow_id
            invocation_response = self._post(url, data=workflow_request)
            api_asserts.assert_status_code_is(invocation_response, 200)
            invocation_id = invocation_response.json()["id"]
            return CwlWorkflowRun(workflow_id, invocation_id)

    run_cwl_tool = run_cwl_artifact

    def get_history_dataset_content( self, history_id, wait=True, **kwds ):
        dataset_id = self.__history_content_id( history_id, wait=wait, **kwds )
        display_response = self.__get_contents_request( history_id, "/%s/display" % dataset_id )
        assert display_response.status_code == 200, display_response.content
        return display_response.content

    def get_history_dataset_details( self, history_id, **kwds ):
        dataset_id = self.__history_content_id( history_id, **kwds )
        details_response = self.__get_contents_request( history_id, "/datasets/%s" % dataset_id )
        assert details_response.status_code == 200
        return details_response.json()

    def get_history_collection_details( self, history_id, **kwds ):
        hdca_id = self.__history_content_id( history_id, **kwds )
        details_response = self.__get_contents_request( history_id, "/dataset_collections/%s" % hdca_id )
        assert details_response.status_code == 200, details_response.content
        return details_response.json()

    def __history_content_id( self, history_id, wait=True, **kwds ):
        if wait:
            assert_ok = kwds.get( "assert_ok", True )
            self.wait_for_history( history_id, assert_ok=assert_ok )
        # kwds should contain a 'dataset' object response, a 'dataset_id' or
        # the last dataset in the history will be fetched.
        if "dataset_id" in kwds:
            history_content_id = kwds[ "dataset_id" ]
        elif "content_id" in kwds:
            history_content_id = kwds[ "content_id" ]
        elif "dataset" in kwds:
            history_content_id = kwds[ "dataset" ][ "id" ]
        else:
            hid = kwds.get( "hid", None )  # If not hid, just grab last dataset
            history_contents = self.__get_contents_request( history_id ).json()
            if hid:
                history_content_id = None
                for history_item in history_contents:
                    if history_item["hid"] == hid:
                        history_content_id = history_item["id"]
                if history_content_id is None:
                    raise Exception("Could not find content with HID [%s] in [%s]" % (hid, history_contents))
            else:
                # No hid specified - just grab most recent element.
                history_content_id = history_contents[-1]["id"]
        return history_content_id

    def __get_contents_request( self, history_id, suffix=""):
        url = "histories/%s/contents" % history_id
        if suffix:
            url = "%s%s" % ( url, suffix )
        return self._get( url )


class DatasetPopulator( BaseDatasetPopulator ):

    def __init__( self, galaxy_interactor ):
        self.galaxy_interactor = galaxy_interactor

    def _post( self, route, data={}, files=None ):
        files = data.get( "__files", None )
        if files is not None:
            del data[ "__files" ]

        return self.galaxy_interactor.post( route, data, files=files )

    def _get( self, route ):
        return self.galaxy_interactor.get( route )

    def _summarize_history_errors( self, history_id ):
        self.galaxy_interactor._summarize_history_errors( history_id )

    def wait_for_dataset(self, history_id, dataset_id, assert_ok=False, timeout=DEFAULT_TIMEOUT):
        return wait_on_state(lambda: self._get("histories/%s/contents/%s" % (history_id, dataset_id)), assert_ok=assert_ok, timeout=timeout)


class FileUploadTarget(object):

    def __init__(self, path):
        self.path = path


class ObjectUploadTarget(object):

    def __init__(self, the_object):
        self.object = the_object


class BaseWorkflowPopulator( object ):

    def load_workflow( self, name, content=workflow_str, add_pja=False ):
        workflow = json.loads( content )
        workflow[ "name" ] = name
        if add_pja:
            tool_step = workflow[ "steps" ][ "2" ]
            tool_step[ "post_job_actions" ][ "RenameDatasetActionout_file1" ] = dict(
                action_type="RenameDatasetAction",
                output_name="out_file1",
                action_arguments=dict( newname="foo ${replaceme}" ),
            )
        return workflow

    def load_random_x2_workflow( self, name ):
        return self.load_workflow( name, content=workflow_random_x2_str )

    def load_workflow_from_resource( self, name, filename=None ):
        if filename is None:
            filename = "data/%s.ga" % name
        content = resource_string( __name__, filename )
        return self.load_workflow( name, content=content )

    def simple_workflow( self, name, **create_kwds ):
        workflow = self.load_workflow( name )
        return self.create_workflow( workflow, **create_kwds )

    def create_workflow( self, workflow, **create_kwds ):
        upload_response = self.create_workflow_response( workflow, **create_kwds )
        uploaded_workflow_id = upload_response.json()[ "id" ]
        return uploaded_workflow_id

    def create_workflow_response( self, workflow, **create_kwds ):
        data = dict(
            workflow=json.dumps( workflow ),
            **create_kwds
        )
        upload_response = self._post( "workflows/upload", data=data )
        return upload_response

    def upload_yaml_workflow(self, has_yaml, **kwds):
        workflow = convert_and_import_workflow(has_yaml, galaxy_interface=self, **kwds)
        return workflow[ "id" ]

    def wait_for_invocation( self, workflow_id, invocation_id, timeout=DEFAULT_TIMEOUT ):
        url = "workflows/%s/usage/%s" % ( workflow_id, invocation_id )
        return wait_on_state( lambda: self._get( url ), timeout=timeout  )

    def wait_for_workflow( self, workflow_id, invocation_id, history_id, assert_ok=True, timeout=DEFAULT_TIMEOUT ):
        """ Wait for a workflow invocation to completely schedule and then history
        to be complete. """
        self.wait_for_invocation( workflow_id, invocation_id, timeout=timeout )
        self.dataset_populator.wait_for_history( history_id, assert_ok=assert_ok, timeout=timeout )


class WorkflowPopulator( BaseWorkflowPopulator, ImporterGalaxyInterface ):

    def __init__( self, galaxy_interactor ):
        self.galaxy_interactor = galaxy_interactor
        self.dataset_populator = DatasetPopulator( galaxy_interactor )

    def _post( self, route, data={}, admin=False ):
        return self.galaxy_interactor.post( route, data, admin=admin )

    def _get( self, route ):
        return self.galaxy_interactor.get( route )

    # Required for ImporterGalaxyInterface interface - so we can recurisvely import
    # nested workflows.
    def import_workflow(self, workflow, **kwds):
        workflow_str = json.dumps(workflow, indent=4)
        data = {
            'workflow': workflow_str,
        }
        data.update(**kwds)
        upload_response = self._post( "workflows", data=data )
        assert upload_response.status_code == 200, upload_response
        return upload_response.json()

    def import_tool(self, tool):
        """ Import a workflow via POST /api/workflows or
        comparable interface into Galaxy.
        """
        upload_response = self._import_tool_response(tool)
        assert upload_response.status_code == 200, upload_response
        return upload_response.json()

    def _import_tool_response(self, tool):
        tool_str = json.dumps(tool, indent=4)
        data = {
            'representation': tool_str
        }
        upload_response = self._post( "dynamic_tools", data=data, admin=True )
        return upload_response


class LibraryPopulator( object ):

    def __init__( self, api_test_case ):
        self.api_test_case = api_test_case
        self.galaxy_interactor = api_test_case.galaxy_interactor

    def new_private_library( self, name ):
        library = self.new_library( name )
        library_id = library[ "id" ]

        role_id = self.user_private_role_id()
        self.set_permissions( library_id, role_id )
        return library

    def new_library( self, name ):
        data = dict( name=name )
        create_response = self.galaxy_interactor.post( "libraries", data=data, admin=True )
        return create_response.json()

    def set_permissions( self, library_id, role_id=None ):
        if role_id:
            perm_list = json.dumps( role_id )
        else:
            perm_list = json.dumps( [] )

        permissions = dict(
            LIBRARY_ACCESS_in=perm_list,
            LIBRARY_MODIFY_in=perm_list,
            LIBRARY_ADD_in=perm_list,
            LIBRARY_MANAGE_in=perm_list,
        )
        self.galaxy_interactor.post( "libraries/%s/permissions" % library_id, data=permissions, admin=True )

    def user_email( self ):
        users_response = self.galaxy_interactor.get( "users" )
        users = users_response.json()
        assert len( users ) == 1
        return users[ 0 ][ "email" ]

    def user_private_role_id( self ):
        user_email = self.user_email()
        roles_response = self.api_test_case.galaxy_interactor.get( "roles", admin=True )
        users_roles = [ r for r in roles_response.json() if r[ "name" ] == user_email ]
        assert len( users_roles ) == 1
        return users_roles[ 0 ][ "id" ]

    def create_dataset_request( self, library, **kwds ):
        create_data = {
            "folder_id": kwds.get( "folder_id", library[ "root_folder_id" ] ),
            "create_type": "file",
            "files_0|NAME": kwds.get( "name", "NewFile" ),
            "upload_option": kwds.get( "upload_option", "upload_file" ),
            "file_type": kwds.get( "file_type", "auto" ),
            "db_key": kwds.get( "db_key", "?" ),
        }
        files = {
            "files_0|file_data": kwds.get( "file", StringIO( kwds.get( "contents", "TestData" ) ) ),
        }
        return create_data, files

    def new_library_dataset( self, name, **create_dataset_kwds ):
        library = self.new_private_library( name )
        payload, files = self.create_dataset_request( library, **create_dataset_kwds )
        url_rel = "libraries/%s/contents" % ( library[ "id" ] )
        dataset = self.api_test_case.galaxy_interactor.post( url_rel, payload, files=files ).json()[0]

        def show():
            return self.api_test_case.galaxy_interactor.get( "libraries/%s/contents/%s" % ( library[ "id" ], dataset[ "id" ] ) )

        wait_on_state(show, timeout=DEFAULT_TIMEOUT)
        return show().json()


class BaseDatasetCollectionPopulator( object ):

    def create_list_from_pairs( self, history_id, pairs, name="Dataset Collection from pairs" ):
        element_identifiers = []
        for i, pair in enumerate( pairs ):
            element_identifiers.append( dict(
                name="test%d" % i,
                src="hdca",
                id=pair
            ) )

        payload = dict(
            instance_type="history",
            history_id=history_id,
            element_identifiers=json.dumps(element_identifiers),
            collection_type="list:paired",
            name=name,
        )
        return self.__create( payload )

    def create_list_of_pairs_in_history( self, history_id, **kwds ):
        pair1 = self.create_pair_in_history( history_id, **kwds ).json()["id"]
        return self.create_list_from_pairs( history_id, [ pair1 ] )

    def create_pair_in_history( self, history_id, **kwds ):
        payload = self.create_pair_payload(
            history_id,
            instance_type="history",
            **kwds
        )
        return self.__create( payload )

    def create_list_in_history( self, history_id, **kwds ):
        payload = self.create_list_payload(
            history_id,
            instance_type="history",
            **kwds
        )
        return self.__create( payload )

    def create_list_payload( self, history_id, **kwds ):
        return self.__create_payload( history_id, identifiers_func=self.list_identifiers, collection_type="list", **kwds )

    def create_pair_payload( self, history_id, **kwds ):
        return self.__create_payload( history_id, identifiers_func=self.pair_identifiers, collection_type="paired", **kwds )

    def __create_payload( self, history_id, identifiers_func, collection_type, **kwds ):
        contents = None
        if "contents" in kwds:
            contents = kwds[ "contents" ]
            del kwds[ "contents" ]

        if "element_identifiers" not in kwds:
            kwds[ "element_identifiers" ] = json.dumps( identifiers_func( history_id, contents=contents ) )

        if "name" not in kwds:
            kwds["name"] = "Test Dataset Collection"

        payload = dict(
            history_id=history_id,
            collection_type=collection_type,
            **kwds
        )
        return payload

    def pair_identifiers( self, history_id, contents=None ):
        hda1, hda2 = self.__datasets( history_id, count=2, contents=contents )

        element_identifiers = [
            dict( name="forward", src="hda", id=hda1[ "id" ] ),
            dict( name="reverse", src="hda", id=hda2[ "id" ] ),
        ]
        return element_identifiers

    def list_identifiers( self, history_id, contents=None ):
        count = 3 if not contents else len( contents )
        # Contents can be a list of strings (with name auto-assigned here) or a list of
        # 2-tuples of form (name, dataset_content).
        if contents and isinstance(contents[0], tuple):
            hdas = self.__datasets( history_id, count=count, contents=[c[1] for c in contents] )

            def hda_to_identifier(i, hda):
                return dict(name=contents[i][0], src="hda", id=hda["id"])
        else:
            hdas = self.__datasets( history_id, count=count, contents=contents )

            def hda_to_identifier(i, hda):
                return dict(name="data%d" % (i + 1), src="hda", id=hda["id"])
        element_identifiers = [hda_to_identifier(i, hda) for (i, hda) in enumerate(hdas)]
        return element_identifiers

    def __create( self, payload ):
        return self._create_collection( payload )

    def __datasets( self, history_id, count, contents=None ):
        datasets = []
        for i in range( count ):
            new_kwds = {}
            if contents:
                new_kwds[ "content" ] = contents[ i ]
            datasets.append( self.dataset_populator.new_dataset( history_id, **new_kwds ) )
        return datasets


class DatasetCollectionPopulator( BaseDatasetCollectionPopulator ):

    def __init__( self, galaxy_interactor ):
        self.galaxy_interactor = galaxy_interactor
        self.dataset_populator = DatasetPopulator( galaxy_interactor )

    def _create_collection( self, payload ):
        create_response = self.galaxy_interactor.post( "dataset_collections", data=payload )
        return create_response


def wait_on_state( state_func, skip_states=["running", "queued", "new", "ready"], assert_ok=False, timeout=DEFAULT_TIMEOUT ):
    def get_state( ):
        response = state_func()
        assert response.status_code == 200, "Failed to fetch state update while waiting."
        state = response.json()[ "state" ]
        if state in skip_states:
            return None
        else:
            if assert_ok:
                assert state == "ok", "Final state - %s - not okay." % state
            return state
    return wait_on( get_state, desc="state", timeout=timeout)


class GiPostGetMixin:
    """Mixin for adapting Galaxy testing populators helpers to bioblend."""

    def _get(self, route):
        return self._gi.make_get_request(self.__url(route))

    def _post(self, route, data={}):
        data = data.copy()
        data['key'] = self._gi.key
        return requests.post(self.__url(route), data=data)

    def __url(self, route):
        return self._gi.url + "/" + route


class GiDatasetPopulator(BaseDatasetPopulator, GiPostGetMixin):

    """Implementation of BaseDatasetPopulator backed by bioblend."""

    def __init__(self, gi):
        """Construct a dataset populator from a bioblend GalaxyInstance."""
        self._gi = gi


class GiDatasetCollectionPopulator(BaseDatasetCollectionPopulator, GiPostGetMixin):

    """Implementation of BaseDatasetCollectionPopulator backed by bioblend."""

    def __init__(self, gi):
        """Construct a dataset collection populator from a bioblend GalaxyInstance."""
        self._gi = gi
        self.dataset_populator = GiDatasetPopulator(gi)

    def _create_collection(self, payload):
        create_response = self._post( "dataset_collections", data=payload )
        return create_response


class GiWorkflowPopulator(BaseWorkflowPopulator, GiPostGetMixin):

    """Implementation of BaseWorkflowPopulator backed by bioblend."""

    def __init__(self, gi):
        """Construct a workflow populator from a bioblend GalaxyInstance."""
        self._gi = gi
        self.dataset_populator = GiDatasetPopulator(gi)


def wait_on( function, desc, timeout=DEFAULT_TIMEOUT ):
    delta = .25
    iteration = 0
    while True:
        total_wait = delta * iteration
        if total_wait > timeout:
            timeout_message = "Timed out after %s seconds waiting on %s." % (
                total_wait, desc
            )
            assert False, timeout_message
        iteration += 1
        value = function()
        if value is not None:
            return value
        time.sleep( delta )
