"""Test CWL workflow functionality."""
import json
import os
import re

from base.populators import (
    CWL_TOOL_DIRECTORY,
    CwlPopulator,
)

from .test_workflows import BaseWorkflowsApiTestCase


class BaseCwlWorklfowTestCase(BaseWorkflowsApiTestCase):

    require_admin_user = True

    def setUp(self):
        super(BaseCwlWorklfowTestCase, self).setUp()
        self.history_id = self.dataset_populator.new_history()
        self.cwl_populator = CwlPopulator(
            self.dataset_populator, self.workflow_populator
        )


class CwlWorkflowsTestCase(BaseCwlWorklfowTestCase):
    """Test case encompassing CWL workflow tests."""

    def test_simplest_wf(self):
        """Test simplest workflow."""
        workflow_id = self._load_workflow("v1.0_custom/just-wc-wf.cwl")
        workflow_content = self._download_workflow(workflow_id)
        for step_index, step in workflow_content["steps"].items():
            if "tool_representation" in step:
                del step["tool_representation"]

        hda1 = self.dataset_populator.new_dataset(self.history_id, content="hello world\nhello all\nhello all in world\nhello")
        inputs_map = {
            "file1": {"src": "hda", "id": hda1["id"]}
        }
        invocation_id = self._invoke(inputs_map, workflow_id)
        self.wait_for_invocation_and_jobs(self.history_id, workflow_id, invocation_id)
        output = self.dataset_populator.get_history_dataset_content(self.history_id, hid=2)
        assert re.search(r"\s+4\s+9\s+47\s+", output)

    def test_load_ids(self):
        workflow_id = self._load_workflow("v1.0/search.cwl#main")
        workflow_content = self._download_workflow(workflow_id)
        for step_index, step in workflow_content["steps"].items():
            if "tool_representation" in step:
                del step["tool_representation"]

        print(workflow_content)
        steps = workflow_content["steps"]
        step_3 = steps["3"]
        step_4 = steps["4"]

        assert step_3["label"] == "index", step_3
        assert step_4["label"] == "search", step_4

        print(step_3)
        print(step_4)

    def test_count_line1_v1(self):
        """Test simple workflow v1.0/count-lines1-wf.cwl."""
        self._run_count_lines_wf("v1.0/count-lines1-wf.cwl")

    def test_count_line1_v1_json(self):
        run_object = self.cwl_populator.run_workflow_job("v1.0/count-lines1-wf.cwl", "v1.0/wc-job.json", history_id=self.history_id)
        self._check_countlines_wf(run_object.invocation_id, run_object.workflow_id, expected_count=16)

    def test_count_line1_draft3(self):
        """Test simple workflow draft3/count-lines1-wf.cwl."""
        self._run_count_lines_wf("draft3/count-lines1-wf.cwl")

    def test_count_line2_v1(self):
        """Test simple workflow v1.0/count-lines2-wf.cwl."""
        self._run_count_lines_wf("v1.0/count-lines2-wf.cwl")

    def test_count_lines3_v1(self):
        workflow_id = self._load_workflow("v1.0/count-lines3-wf.cwl")
        hdca = self.dataset_collection_populator.create_list_in_history(self.history_id).json()
        inputs_map = {
            "file1": {"src": "hdca", "id": hdca["id"]}
        }
        invocation_id = self._invoke(inputs_map, workflow_id)
        self.wait_for_invocation_and_jobs(self.history_id, workflow_id, invocation_id)
        hdca = self.dataset_populator.get_history_collection_details(self.history_id, hid=8)
        assert hdca["collection_type"] == "list"
        elements = hdca["elements"]
        assert len(elements) == 3
        element0 = elements[0]["object"]
        assert element0["history_content_type"] == "dataset"
        assert element0["state"] == "ok"
        assert element0["file_ext"] == "expression.json"
        # TODO: ensure this looks like an int[] - it doesn't currently...

    def test_count_lines3_ct(self):
        self.run_conformance_test("v1.0", "Test single step workflow with Scatter step")

    def test_count_lines4_v1(self):
        workflow_id = self._load_workflow("v1.0/count-lines4-wf.cwl")
        hda1 = self.dataset_populator.new_dataset(self.history_id, content="hello world\nhello all\nhello all in world\nhello")
        hda2 = self.dataset_populator.new_dataset(self.history_id, content="moo\ncow\nthat\nis\nall")
        inputs_map = {
            "file1": {"src": "hda", "id": hda1["id"]},
            "file2": {"src": "hda", "id": hda2["id"]}
        }
        invocation_id = self._invoke(inputs_map, workflow_id)
        self.wait_for_invocation_and_jobs(self.history_id, workflow_id, invocation_id)
        self.dataset_populator.get_history_collection_details(self.history_id, hid=5)

    def test_count_lines4_json(self):
        self.cwl_populator.run_workflow_job("v1.0/count-lines4-wf.cwl", "v1.0/count-lines4-job.json", history_id=self.history_id)
        self.dataset_populator.get_history_collection_details(self.history_id, hid=5)

    def test_scatter_wf1_v1(self):
        self.cwl_populator.run_workflow_job("v1.0/scatter-wf1.cwl", "v1.0/scatter-job1.json", history_id=self.history_id)
        self.dataset_populator.get_history_collection_details(self.history_id, hid=5)

    def test_record_io(self):
        self.run_conformance_test("v1.0_custom", "Test record type inputs to and outputs from workflows.")

    def test_workflow_int_io(self):
        self.run_conformance_test("v1.0_custom", "Test integer workflow input and outputs")

    def test_workflow_int_io_opt_spec(self):
        self.run_conformance_test("v1.0_custom", "Test optional integer workflow inputs (specified)")

    def test_workflow_int_io_opt_unspec(self):
        self.run_conformance_test("v1.0_custom", "Test optional integer workflow inputs (unspecified)")

    def test_workflow_any_int(self):
        self.run_conformance_test("v1.0_custom", "Test any parameter with integer input to a workflow")

    def test_workflow_any_string(self):
        self.run_conformance_test("v1.0_custom", "Test any parameter with string input to a workflow")

    def test_workflow_any_file(self):
        self.run_conformance_test("v1.0_custom", "Test any parameter with file input to a workflow")

    def test_file_input_default_unspecified(self):
        self.run_conformance_test("v1.0_custom", "Test File input with default unspecified")

    def test_io_input_optional_unspecified(self):
        self.run_conformance_test("v1.0_custom", "Test default integer workflow inputs (unspecified)")

    def test_union_input_optional_unspecified(self):
        self.run_conformance_test("v1.0_custom", "Test union type input to workflow with default unspecified")

    def test_union_input_optional_specified_file(self):
        self.run_conformance_test("v1.0_custom", "Test union type input to workflow with default specified as file")

    def _run_count_lines_wf(self, wf_path):
        workflow_id = self._load_workflow(wf_path)
        hda1 = self.dataset_populator.new_dataset(self.history_id, content="hello world\nhello all\nhello all in world\nhello")
        inputs_map = {
            "file1": {"src": "hda", "id": hda1["id"]}
        }
        invocation_id = self._invoke(inputs_map, workflow_id)
        self._check_countlines_wf(invocation_id, workflow_id)

    def _check_countlines_wf(self, invocation_id, workflow_id, expected_count=4):
        self.wait_for_invocation_and_jobs(self.history_id, workflow_id, invocation_id)
        output = self.dataset_populator.get_history_dataset_content(self.history_id, hid=3)
        self.dataset_populator._summarize_history_errors(self.history_id)
        assert str(expected_count) == output, output

    def _invoke(self, inputs, workflow_id):
        workflow_request = dict(
            history="hist_id=%s" % self.history_id,
            workflow_id=workflow_id,
            inputs=json.dumps(inputs),
            inputs_by="name",
        )
        url = "workflows/%s/invocations" % workflow_id
        invocation_response = self._post(url, data=workflow_request)
        self._assert_status_code_is(invocation_response, 200)
        invocation_id = invocation_response.json()["id"]
        return invocation_id

    def _load_workflow(self, rel_path):
        path = os.path.join(CWL_TOOL_DIRECTORY, rel_path)
        data = dict(
            from_path=path,
        )
        route = "workflows"
        upload_response = self._post(route, data=data)
        self._assert_status_code_is(upload_response, 200)
        workflow = upload_response.json()
        workflow_id = workflow["id"]
        return workflow_id
