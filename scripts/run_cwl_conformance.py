#!/usr/bin/env python

import argparse
import os
import subprocess

DESCRIPTION = """This script runs CWL conformity tests over a running Galaxy server."""
SCRIPT_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
ROOT_DIRECTORY = os.path.dirname(SCRIPT_DIRECTORY)
CWL_TOOL_DIRECTORY_DEFAULT = os.path.join(ROOT_DIRECTORY, "test", "functional", "tools", "cwl_tools")

EPILOG_MSG = "Note: this script needs the Galaxy server \
to be started with the following command: \
CWL_TOOL_DIRECTORY=<path> GALAXY_RUN_WITH_TEST_TOOLS=1 sh run.sh"


def path_inference(path):
    if os.path.isdir(path):
        return path
    else:
        return os.path.join(ROOT_DIRECTORY, path)


def main(argv=None):
    arg_parser = argparse.ArgumentParser(description=DESCRIPTION,
                                         formatter_class=argparse.ArgumentDefaultsHelpFormatter,
                                         epilog=EPILOG_MSG)
    arg_parser.add_argument("--api_key", required=True, help="Galaxy API key")
    arg_parser.add_argument("--host", default="localhost", help="Galaxy server host")
    arg_parser.add_argument("--port", default="8080", help="Galaxy server port")
    arg_parser.add_argument("--test_path", default="test/api/test_cwl_conformance_v1_0.py:CwlConformanceTestCase.test_conformance_v1_0_17", help="Test path")
    arg_parser.add_argument("--cwl_tool_directory", default=CWL_TOOL_DIRECTORY_DEFAULT)

    args = arg_parser.parse_args(argv)

    cwl_tool_directory = path_inference(args.cwl_tool_directory)
    test_path = path_inference(args.test_path)

    os.environ['GALAXY_TEST_HOST'] = args.host
    os.environ['GALAXY_TEST_PORT'] = args.port
    os.environ['GALAXY_TEST_EXTERNAL'] = f'http://{args.host}:{args.port}'
    os.environ['GALAXY_CONFIG_MASTER_API_KEY'] = args.api_key
    os.environ['GALAXY_TEST_USER_API_KEY'] = args.api_key
    os.environ['CWL_TOOL_DIRECTORY'] = cwl_tool_directory

    test_runner_script = f'{ROOT_DIRECTORY}/run_tests.sh'
    cmd = [test_runner_script, '-api', test_path]
    subprocess.call(cmd)


if __name__ == "__main__":
    main()
