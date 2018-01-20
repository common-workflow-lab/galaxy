#!/usr/bin/env python
from __future__ import absolute_import, print_function

import argparse
import json
import os
import sys
import tempfile

from bioblend import galaxy

sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'test')))
sys.path.insert(1, os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir, 'lib')))

from galaxy.tools.parser import get_tool_source

from base.populators import (  # noqa: I100,I202
    CwlPopulator,
    GiDatasetPopulator,
    GiWorkflowPopulator,
)

DESCRIPTION = """Simple CWL runner script."""

def collect_outputs(cwl_run, output_names, output_directory=None):

    def get_dataset(dataset_details, filename=None):
        parent_basename = dataset_details.get("cwl_file_name")
        if not parent_basename:
            parent_basename = dataset_details.get("name")
        file_ext = dataset_details["file_ext"]
        if file_ext == "directory":
            # TODO: rename output_directory to outputs_directory because we can have output directories
            # and this is confusing...
            the_output_directory = os.path.join(output_directory, parent_basename)
            safe_makedirs(the_output_directory)
            destination = self.download_output_to(dataset_details, the_output_directory, filename=filename)
        else:
            destination = self.download_output_to(dataset_details, output_directory, filename=filename)
        if filename is None:
            basename = parent_basename
        else:
            basename = os.path.basename(filename)
        return {"path": destination, "basename": basename}

    outputs = {}
    for output_name in output_names:
        cwl_output = cwl_run.get_output_as_object(output_name, download_folder=os.getcwd())
        outputs[output_name] = cwl_output
    return outputs

def main(argv=None):
    """Entry point for workflow driving."""
    arg_parser = argparse.ArgumentParser(description=DESCRIPTION)
    arg_parser.add_argument("--api_key", default="testmasterapikey")
    arg_parser.add_argument("--host", default="http://localhost:8080/")
    arg_parser.add_argument('tool', metavar='TOOL', help='tool or workflow')
    arg_parser.add_argument('job', metavar='JOB', help='job')

    args = arg_parser.parse_args(argv)

    gi = galaxy.GalaxyInstance(args.host, args.api_key)
    dataset_populator = GiDatasetPopulator(gi)
    workflow_populator = GiWorkflowPopulator(gi)
    cwl_populator = CwlPopulator(dataset_populator, workflow_populator)
    tool = os.path.abspath(args.tool)
    job = os.path.abspath(args.job)
    run = cwl_populator.run_cwl_job(tool, job)

    tool_source = get_tool_source(tool)
    # TODO: do something with collections at some point
    output_datasets, _ = tool_source.parse_outputs(None)
    output_names = [output_dataset.name for output_dataset in output_datasets.values()]
    outputs = collect_outputs(run, output_names)
    print(json.dumps(outputs, indent=4)) 
    #for output_dataset in output_datasets.values():
    #    name = output_dataset.name
    #    print(run.get_output_as_object(name))


if __name__ == "__main__":
    main()
