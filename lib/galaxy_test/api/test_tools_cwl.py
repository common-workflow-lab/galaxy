"""Test CWL Tool Execution via the API."""

from sys import platform as _platform

from galaxy.tool_util.cwl.representation import USE_FIELD_TYPES
from galaxy_test.api._framework import ApiTestCase
from galaxy_test.base.populators import (
    CwlPopulator,
    DatasetPopulator,
    WorkflowPopulator,
)
from galaxy_test.base.populators import skip_without_tool

IS_OS_X = _platform == "darwin"


class CwlToolsTestCase(ApiTestCase):
    """Test CWL Tool Execution via the API."""

    def setUp(self):
        """Setup dataset populator."""
        super().setUp()
        self.dataset_populator = DatasetPopulator(self.galaxy_interactor)
        worklfow_populator = WorkflowPopulator(self.galaxy_interactor)
        self.cwl_populator = CwlPopulator(self.dataset_populator, worklfow_populator)

    @skip_without_tool("cat1-tool")
    def test_cat1_number(self):
        """Test execution of cat1 using the "normal" Galaxy job API representation."""
        history_id = self.dataset_populator.new_history()
        hda1 = _dataset_to_param(self.dataset_populator.new_dataset(history_id, content='1\n2\n3', name="test1"))
        if not USE_FIELD_TYPES:
            inputs = {
                "file1": hda1,
                "numbering|_cwl__type_": "boolean",
                "numbering|_cwl__value_": True,
            }
        else:
            inputs = {
                "file1": hda1,
                "numbering": {"src": "json", "value": True},
            }
        stdout = self._run_and_get_stdout("cat1-tool", history_id, inputs, assert_ok=True)
        self.assertEquals(stdout, "     1\t1\n     2\t2\n     3\t3\n")

    @skip_without_tool("cat1-tool")
    def test_cat1_number_cwl_json(self):
        """Test execution of cat1 using the "CWL" Galaxy job API representation."""
        history_id = self.dataset_populator.new_history()
        hda1 = _dataset_to_param(self.dataset_populator.new_dataset(history_id, content='1\n2\n3'))
        inputs = {
            "file1": hda1,
            "numbering": True,
        }
        stdout = self._run_and_get_stdout("cat1-tool", history_id, inputs, assert_ok=True, inputs_representation="cwl")
        self.assertEquals(stdout, "     1\t1\n     2\t2\n     3\t3\n")

    @skip_without_tool("cat1-tool")
    def test_cat1_number_cwl_json_file(self):
        """Test execution of cat1 using the CWL job definition file."""
        run_object = self.cwl_populator.run_cwl_artifact("cat1-tool", "test/functional/tools/cwl_tools/v1.0/v1.0/cat-job.json")
        stdout = self._get_job_stdout(run_object.job_id)
        self.assertEquals(stdout, "Hello world!\n")

    @skip_without_tool("cat1-tool")
    def test_cat1_number_cwl_n_json_file(self):
        run_object = self.cwl_populator.run_cwl_artifact("cat1-tool", "test/functional/tools/cwl_tools/v1.0/v1.0/cat-n-job.json")
        stdout = self._get_job_stdout(run_object.job_id)
        self.assertEquals(stdout, "     1\tHello world!\n")

    @skip_without_tool("cat2-tool")
    def test_cat2(self):
        run_object = self.cwl_populator.run_cwl_artifact("cat2-tool", "test/functional/tools/cwl_tools/v1.0/v1.0/cat-job.json")
        stdout = self._get_job_stdout(run_object.job_id)
        self.assertEquals(stdout, "Hello world!\n")

    @skip_without_tool("cat4-tool")
    def test_cat4(self):
        run_object = self.cwl_populator.run_cwl_artifact("cat4-tool", "test/functional/tools/cwl_tools/v1.0/v1.0/cat-job.json")
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        self.assertEquals(output1_content, "Hello world!\n")

    @skip_without_tool("cat-default")
    def test_cat_default(self):
        run_object = self.cwl_populator.run_cwl_artifact("cat-default", job={})
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        self.assertEquals(output1_content, "Hello world!\n")

    @skip_without_tool("wc-tool")
    def test_wc(self):
        run_object = self.cwl_populator.run_cwl_artifact("wc-tool", "test/functional/tools/cwl_tools/v1.0/v1.0/wc-job.json")
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        if not IS_OS_X:
            self.assertEquals(output1_content, "  16  198 1111\n")
        else:
            self.assertEquals(output1_content, "      16     198    1111\n")

    @skip_without_tool("wc2-tool")
    def test_wc2(self):
        run_object = self.cwl_populator.run_cwl_artifact("wc2-tool", "test/functional/tools/cwl_tools/v1.0/v1.0/wc-job.json")
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        self.assertEquals(output1_content, "16")

    @skip_without_tool("wc3-tool")
    def test_wc3(self):
        run_object = self.cwl_populator.run_cwl_artifact(
            "wc4-tool",
            job={
                "file1": [
                    {
                        "class": "File",
                        "path": "whale.txt"
                    },
                ],
            },
            test_data_directory="test/functional/tools/cwl_tools/v1.0/v1.0/"
        )
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        self.assertEquals(output1_content, "16")

    @skip_without_tool("wc4-tool")
    def test_wc4(self):
        run_object = self.cwl_populator.run_cwl_artifact("wc4-tool", "test/functional/tools/cwl_tools/v1.0/v1.0/wc-job.json")
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        self.assertEquals(output1_content, "16")

    @skip_without_tool("galactic_cat")
    def test_galactic_cat_1(self):
        with self.dataset_populator.test_history() as history_id:
            hda_id = self.dataset_populator.new_dataset(history_id, name="test_dataset.txt")["id"]
            self.dataset_populator.wait_for_history(history_id, assert_ok=True)
            inputs = {
                "input1": {"src": "hda", "id": hda_id}
            }
            run_response = self._run("galactic_cat", history_id, inputs, assert_ok=True)
            dataset = run_response["outputs"][0]
            content = self.dataset_populator.get_history_dataset_content(history_id, dataset=dataset)
            assert content.strip() == "TestData123", content

    @skip_without_tool("galactic_record_input")
    def test_galactic_record_input(self):
        with self.dataset_populator.test_history() as history_id:
            hda1_id = self.dataset_populator.new_dataset(history_id, content="moo", name="test_dataset.txt")["id"]
            hda2_id = self.dataset_populator.new_dataset(history_id, content="cow dog foo", name="test_dataset.txt")["id"]
            self.dataset_populator.wait_for_history(history_id, assert_ok=True)
            inputs = {
                "input1": {"src": "hda", "id": hda1_id},
                "input2": {"src": "hda", "id": hda2_id},
            }
            run_response = self._run("galactic_record_input", history_id, inputs, assert_ok=True)
            dataset = run_response["outputs"][0]
            content = self.dataset_populator.get_history_dataset_content(history_id, dataset=dataset)
            assert content.strip() == "moo", content

            dataset = run_response["outputs"][1]
            content = self.dataset_populator.get_history_dataset_content(history_id, dataset=dataset)
            assert content.strip() == "cow dog foo", content

    def _run_and_get_stdout(self, tool_id, history_id, inputs, **kwds):
        response = self._run(tool_id, history_id, inputs, **kwds)
        assert "jobs" in response
        job = response["jobs"][0]
        job_id = job["id"]
        final_state = self.dataset_populator.wait_for_job(job_id)
        assert final_state == "ok"
        return self._get_job_stdout(job_id)

    def _get_job_stdout(self, job_id):
        job_details = self.dataset_populator.get_job_details(job_id, full=True)
        stdout = job_details.json()["stdout"]
        return stdout

    @skip_without_tool("cat3-tool")
    def test_cat3(self):
        with self.dataset_populator.test_history() as history_id:
            hda1 = _dataset_to_param(self.dataset_populator.new_dataset(history_id, content='1\t2\t3'))
            inputs = {
                "f1": hda1,
            }
            response = self._run("cat3-tool", history_id, inputs, assert_ok=True)
            output1 = response["outputs"][0]
            output1_details = self.dataset_populator.get_history_dataset_details(history_id, dataset=output1)
            assert "created_from_basename" in output1_details, output1_details.keys()
            assert output1_details["created_from_basename"] == "output.txt", output1_details["created_from_basename"]
            output1_content = self.dataset_populator.get_history_dataset_content(history_id, dataset=output1)
            assert output1_content == "1\t2\t3\n", output1_content

    @skip_without_tool("sorttool")
    def test_sorttool(self):
        history_id = self.dataset_populator.new_history()
        hda1 = _dataset_to_param(self.dataset_populator.new_dataset(history_id, content='1\n2\n3'))
        inputs = {
            "reverse": False,
            "input": hda1
        }
        response = self._run("sorttool", history_id, inputs, assert_ok=True)
        output1 = response["outputs"][0]
        output1_content = self.dataset_populator.get_history_dataset_content(history_id, dataset=output1)
        assert output1_content == "1\n2\n3\n", output1_content

    @skip_without_tool("sorttool")
    def test_sorttool_reverse(self):
        history_id = self.dataset_populator.new_history()
        hda1 = _dataset_to_param(self.dataset_populator.new_dataset(history_id, content='1\n2\n3'))
        inputs = {
            "reverse": True,
            "input": hda1
        }
        response = self._run("sorttool", history_id, inputs, assert_ok=True)
        output1 = response["outputs"][0]
        output1_content = self.dataset_populator.get_history_dataset_content(history_id, dataset=output1)
        assert output1_content == "3\n2\n1\n", output1_content

    @skip_without_tool("env-tool1")
    def test_env_tool1(self):
        history_id = self.dataset_populator.new_history()
        inputs = {
            "in": "Hello World",
        }
        response = self._run("env-tool1", history_id, inputs, assert_ok=True)
        output1 = response["outputs"][0]
        output1_content = self.dataset_populator.get_history_dataset_content(history_id, dataset=output1)
        self.assertEquals(output1_content, "Hello World\n")

    @skip_without_tool("env-tool2")
    def test_env_tool2(self):
        run_object = self.cwl_populator.run_cwl_artifact("env-tool2", "test/functional/tools/cwl_tools/v1.0/v1.0/env-job.json")
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        self.assertEquals(output1_content, "hello test env\n")

    @skip_without_tool("rename")
    def test_rename(self):
        run_object = self.cwl_populator.run_cwl_artifact("rename", "test/functional/tools/cwl_tools/v1.0/v1.0/rename-job.json")
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        self.assertEquals(output1_content, whale_text())

    @skip_without_tool("optional-output")
    def test_optional_output(self):
        run_object = self.cwl_populator.run_cwl_artifact("optional-output", "test/functional/tools/cwl_tools/v1.0/v1.0/cat-job.json")
        output_file = run_object.output(0)
        optional_file = run_object.output(1)
        output_content = self.dataset_populator.get_history_dataset_content(run_object.history_id, dataset=output_file)
        optional_content = self.dataset_populator.get_history_dataset_content(run_object.history_id, dataset=optional_file)
        self.assertEquals(output_content, "Hello world!\n")
        self.assertEquals(optional_content, "null")

    @skip_without_tool("optional-output2")
    def test_optional_output2_on(self):
        run_object = self.cwl_populator.run_cwl_artifact(
            "optional-output2",
            job={
                "produce": "do_write",
            },
            test_data_directory="test/functional/tools/cwl_tools/v1.0/v1.0/"
        )
        output_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        self.assertEquals(output_content, "bees\n")

    @skip_without_tool("optional-output2")
    def test_optional_output2_off(self):
        run_object = self.cwl_populator.run_cwl_artifact(
            "optional-output2",
            job={
                "produce": "dont_write",
            },
            test_data_directory="test/functional/tools/cwl_tools/v1.0/v1.0/"
        )
        output_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        self.assertEquals(output_content, "null")

    @skip_without_tool("index1")
    @skip_without_tool("showindex1")
    def test_index1(self):
        run_object = self.cwl_populator.run_cwl_artifact(
            "index1",
            job={
                "file": {
                    "class": "File",
                    "path": "whale.txt"
                },
            },
            test_data_directory="test/functional/tools/cwl_tools/v1.0/v1.0/",
        )
        output1 = self.dataset_populator.get_history_dataset_details(run_object.history_id)
        run_object = self.cwl_populator.run_cwl_artifact(
            "showindex1",
            job={
                "file": {
                    "src": "hda",
                    "id": output1["id"],
                },
            },
            test_data_directory="test/functional/tools/cwl_tools/v1.0/v1.0/",
            history_id=run_object.history_id,
        )
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        assert "call: 1\n" in output1_content, output1_content

    @skip_without_tool("any1")
    def test_any1_0(self):
        run_object = self.cwl_populator.run_cwl_artifact(
            "any1",
            job={"bar": 7},
            test_data_directory="test/functional/tools/cwl_tools/v1.0/v1.0/",
        )
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        assert output1_content == '7', output1_content

    @skip_without_tool("any1")
    def test_any1_1(self):
        run_object = self.cwl_populator.run_cwl_artifact(
            "any1",
            job={"bar": "7"},
            test_data_directory="test/functional/tools/cwl_tools/v1.0/v1.0/",
        )
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        assert output1_content == '"7"', output1_content

    @skip_without_tool("any1")
    def test_any1_file(self):
        run_object = self.cwl_populator.run_cwl_artifact(
            "any1",
            job={"bar": {
                "class": "File",
                "location": "whale.txt",
            }},
            test_data_directory="test/functional/tools/cwl_tools/v1.0/v1.0/",
        )
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        self.dataset_populator._summarize_history_errors(run_object.history_id)
        assert output1_content == '"File"', "[%s]" % output1_content

    @skip_without_tool("any1")
    def test_any1_2(self):
        run_object = self.cwl_populator.run_cwl_artifact(
            "any1",
            job={"bar": {"Cow": ["Turkey"]}},
            test_data_directory="test/functional/tools/cwl_tools/v1.0/v1.0/",
        )
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        assert output1_content == '{"Cow": ["Turkey"]}', output1_content

    @skip_without_tool("null-expression1-tool")
    def test_null_expression_1_1(self):
        run_object = self.cwl_populator.run_cwl_artifact("null-expression1-tool", "test/functional/tools/cwl_tools/v1.0/v1.0/empty.json")
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        assert output1_content == '1', output1_content

    @skip_without_tool("null-expression1-tool")
    def test_null_expression_1_2(self):
        run_object = self.cwl_populator.run_cwl_artifact("null-expression1-tool", "test/functional/tools/cwl_tools/v1.0/v1.0/null-expression2-job.json")
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        assert output1_content == '2', output1_content

    @skip_without_tool("null-expression2-tool")
    def test_null_expression_any_bad_1(self):
        """Test explicitly passing null to Any type without a default value fails."""
        run_object = self.cwl_populator.run_cwl_artifact("null-expression2-tool", "test/functional/tools/cwl_tools/v1.0/v1.0/null-expression1-job.json", assert_ok=False)
        self._assert_status_code_is(run_object.run_response, 400)

    @skip_without_tool("null-expression2-tool")
    def test_null_expression_any_bad_2(self):
        """Test Any without defaults can be unspecified."""
        run_object = self.cwl_populator.run_cwl_artifact("null-expression2-tool", "test/functional/tools/cwl_tools/v1.0/v1.0/empty.json", assert_ok=False)
        self._assert_status_code_is(run_object.run_response, 400)

    @skip_without_tool("default_path")
    def test_default_path_override(self):
        run_object = self.cwl_populator.run_cwl_artifact("default_path", "test/functional/tools/cwl_tools/v1.0/v1.0/default_path_job.yml")
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        assert output1_content.strip() == "Hello world!", output1_content

    @skip_without_tool("default_path_custom_1")
    def test_default_path(self):
        # produces no output - just test the job runs okay.
        # later come back and verify standard output of the job.
        run_object = self.cwl_populator.run_cwl_artifact("default_path_custom_1", job={})
        stdout = self._get_job_stdout(run_object.job_id)
        assert "this is the test file that will be used when calculating an md5sum" in stdout

    @skip_without_tool("params")
    def test_params1(self):
        run_object = self.cwl_populator.run_cwl_artifact("params", "test/functional/tools/cwl_tools/v1.0/v1.0/empty.json")
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id)
        assert output1_content == '"b b"', output1_content

    @skip_without_tool("parseInt-tool")
    def test_parse_int_tool(self):
        run_object = self.cwl_populator.run_cwl_artifact("parseInt-tool", "test/functional/tools/cwl_tools/v1.0/v1.0/parseInt-job.json")
        output1 = self.dataset_populator.get_history_dataset_details(run_object.history_id, hid=2)
        assert output1["state"] == "ok"
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id, hid=2)
        self.assertEquals(output1_content, '42')
        self.assertEquals(output1["extension"], "expression.json")

    @skip_without_tool("record-output")
    def test_record_output(self):
        run_object = self.cwl_populator.run_cwl_artifact("record-output", "test/functional/tools/cwl_tools/v1.0/v1.0/record-output-job.json")
        result_record = run_object.output_collection(0)
        assert result_record["collection_type"] == "record"
        record_elements = result_record["elements"]
        first_element = record_elements[0]
        assert first_element["element_identifier"] == "ofoo"
        first_hda = first_element["object"]
        output1_content = self.dataset_populator.get_history_dataset_content(run_object.history_id, hid=first_hda["hid"])
        assert "Call me Ishmael." in output1_content, "Expected contents of whale.txt, got [%s]" % output1_content

    # def test_dynamic_tool_execution( self ):
    #     workflow_tool_json = {
    #         'inputs': [{'inputBinding': {}, 'type': 'File', 'id': 'file:///home/john/workspace/galaxy/test/unit/tools/cwl_tools/v1.0/v1.0/count-lines2-wf.cwl#step1/wc/wc_file1'}],
    #         'stdout': 'output.txt',
    #         'id': 'file:///home/john/workspace/galaxy/test/unit/tools/cwl_tools/v1.0/v1.0/count-lines2-wf.cwl#step1/wc',
    #         'outputs': [{'outputBinding': {'glob': 'output.txt'}, 'type': 'File', 'id': 'file:///home/john/workspace/galaxy/test/unit/tools/cwl_tools/v1.0/v1.0/count-lines2-wf.cwl#step1/wc/wc_output'}],
    #         'baseCommand': 'wc',
    #         'class': 'CommandLineTool'
    #     }

    #     create_payload = dict(
    #         representation=json.dumps(workflow_tool_json),
    #     )
    #     create_response = self._post( "dynamic_tools", data=create_payload, admin=True )
    #     self._assert_status_code_is( create_response, 200 )

    # TODO: Use mixin so this can be shared with tools test case.
    def _run(self, tool_id, history_id, inputs, assert_ok=False, tool_version=None, inputs_representation=None):
        payload = self.dataset_populator.run_tool_payload(
            tool_id=tool_id,
            inputs=inputs,
            history_id=history_id,
            inputs_representation=inputs_representation,
        )
        if tool_version is not None:
            payload["tool_version"] = tool_version
        create_response = self._post("tools", data=payload)
        if assert_ok:
            self._assert_status_code_is(create_response, 200)
            create = create_response.json()
            self._assert_has_keys(create, 'outputs')
            return create
        else:
            return create_response


def whale_text():
    return open("test/functional/tools/cwl_tools/v1.0/v1.0/whale.txt").read()


def _dataset_to_param(dataset):
    return dict(
        src='hda',
        id=dataset['id']
    )
