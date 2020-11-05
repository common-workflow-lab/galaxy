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

from galaxy.tool_util.cwl.parser import get_outputs
from galaxy.version import VERSION

from base.populators import (  # noqa: I100,I202
    CwlPopulator,
    GiDatasetPopulator,
    GiPostGetMixin,
    GiWorkflowPopulator,
)

DESCRIPTION = """Simple CWL runner script."""

def collect_outputs(cwl_run, output_names, output_directory=None, outdir=os.getcwd()):

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
        cwl_output = cwl_run.get_output_as_object(output_name, download_folder=outdir)
        outputs[output_name] = cwl_output
    return outputs

def main(argv=None):
    """Entry point for workflow driving."""
    arg_parser = argparse.ArgumentParser(description=DESCRIPTION)
    arg_parser.add_argument("--api_key", default="testmasterapikey")
    arg_parser.add_argument("--host", default="http://localhost:8080/")
    arg_parser.add_argument("--outdir", default=".")
    arg_parser.add_argument("--quiet", action="store_true")
    arg_parser.add_argument("--version", action='version', version='%(prog)s {}~CWL'.format(VERSION))
    arg_parser.add_argument("--cwd", default=os.getcwd())
    arg_parser.add_argument('tool', metavar='TOOL', help='tool or workflow')
    arg_parser.add_argument('job', metavar='JOB', help='job')

    args = arg_parser.parse_args(argv)

    gi = galaxy.GalaxyInstance(args.host, args.api_key)
    i = GiPostGetMixin()
    i._gi = gi
    response = i._get("whoami")
    if response.json() is None:
        email = "cwluser@example.com"
        all_users = i._get('users').json()
        try:
            test_user = [user for user in all_users if user["email"] == email][0]
        except IndexError:
            data = dict(
                email=email,
                password="testpass",
                username="cwluser",
            )
            test_user = i._post('users', data).json()

        api_key = i._post("users/%s/api_key" % test_user['id']).json()
        gi = galaxy.GalaxyInstance(args.host, api_key)

    dataset_populator = GiDatasetPopulator(gi)
    workflow_populator = GiWorkflowPopulator(gi)
    cwl_populator = CwlPopulator(dataset_populator, workflow_populator)

    abs_cwd = os.path.abspath(args.cwd)

    tool = args.tool
    if not os.path.isabs(tool):
        tool = os.path.join(abs_cwd, tool)

    job = args.job
    if not os.path.isabs(job):
        job = os.path.join(abs_cwd, job)

    run = cwl_populator.run_cwl_job(tool, job)

    outputs = get_outputs(tool)
    output_names = [o.get_id() for o in outputs]
    outputs = collect_outputs(run, output_names, outdir=args.outdir)
    print(json.dumps(outputs, indent=4))
    #for output_dataset in output_datasets.values():
    #    name = output_dataset.name
    #    print(run.get_output_as_object(name))


if __name__ == "__main__":
    main()
