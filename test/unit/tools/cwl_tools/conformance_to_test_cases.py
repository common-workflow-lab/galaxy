import os
import string
import sys

import yaml

THIS_DIRECTORY = os.path.dirname(os.path.normpath(__file__))
API_TEST_DIRECTORY = os.path.join(THIS_DIRECTORY, "..", "..", "..", "..", "lib", "galaxy_test", "api")
CWL_TESTS_DIRECTORY = os.path.join(API_TEST_DIRECTORY, "cwl")

TEST_FILE_TEMPLATE = string.Template('''"""Test CWL conformance for version ${version}."""

from ..test_workflows_cwl import BaseCwlWorklfowTestCase


class CwlConformanceTestCase(BaseCwlWorklfowTestCase):
    """Test case mapping to CWL conformance tests for version ${version}."""
$tests''')

TEST_TEMPLATE = string.Template('''
    def test_conformance_${version_simple}_${label}(self):
        """${doc}

        Generated from::

${cwl_test_def}
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""${version}""", """${doc}""")
''')

RED_TESTS = {
    # NON-required:
    "wf_scatter_two_nested_crossproduct": "cross product not implemented",
    "wf_scatter_two_dotproduct": "AssertionError: Unimplemented scatter type [flat_crossproduct]",
    "wf_scatter_nested_crossproduct_secondempty": "not implemented",
    "wf_scatter_nested_crossproduct_firstempty": "not implemented",
    "wf_scatter_flat_crossproduct_oneempty": "AssertionError: Unimplemented scatter type [flat_crossproduct]",
    "format_checking": "format stuff not implemented",
    "format_checking_subclass": "format stuff not implemented",
    "format_checking_equivalentclass": "format stuff not implemented",
    "output_secondaryfile_optional": "expected null got file of size 4 (maybe null?)",
    "valuefrom_ignored_null": "wrong output, vf-concat.cwl with empty.json",
    "valuefrom_wf_step": "ValidationException: [Errno 2] No such file or directory: '/Users/john/workspace/galaxy/step_input:/1'",
    "valuefrom_wf_step_multiple": "basic.py problem ValueError: invalid literal for int() with base 10: ''",
}

# Regressions
REGRESSIONS = {
    'directory_output': "Bug1: Extra files handling changes.",
    'wf_compound_doc': "Bug4: No clue what is wrong here.",
    'step_input_default_value_nosource': "Bug2: Broken step input defaults?",
    "wf_input_default_missing": "Bug2",
    "wf_input_default_provided": "Bug3: is not a valid workflow invocation id",
    "wf_scatter_dotproduct_twoempty": "Bug3",
    "wf_scatter_emptylist": "Bug3",
    "wf_step_connect_undeclared_param": "Bug2",
    "wf_two_inputfiles_namecollision": "Bug3",
    "wf_wc_expressiontool": "Bug3",
    "wf_wc_nomultiple": "Bug3",
    "wf_wc_scatter_multiple_merge": "Bug3",
    "wf_wc_scatter_multiple_flattened": "Bug3",
    "wf_wc_scatter": "Bug3",
    "wf_wc_parseInt": "Bug3",
    "workflow_union_default_input_unspecified": "Bug2",
}
RED_TESTS.update(REGRESSIONS)

GREEN_TESTS = {
    "v1.0": [
        "expression_tool_int_array_output",
        "cl_gen_arrayofarrays",
        "docker_json_output_location",
        "docker_json_output_path",
        "envvar_req",
        "expression_any",
        "expression_any_null",
        "expression_outputEval",
        "expression_parseint",
        "exprtool_directory_literal",
        "exprtool_file_literal",
        "initial_workdir_empty_writable",
        "initial_workdir_empty_writable_docker",
        "initial_workdir_expr",
        "initial_workdir_output",
        "initial_workdir_trailingnl",
        "initialworkpath_output",
        "inline_expressions",
        "metadata",
        "nameroot_nameext_stdout_expr",
        "null_missing_params",
        "rename",
        "stdinout_redirect",
        "stdinout_redirect_docker",
        "stdout_redirect_docker",
        "stdout_redirect_mediumcut_docker",
        "stdout_redirect_shortcut_docker",
        "writable_stagedfiles",
        "workflow_union_default_input_with_file_provided",
        "any_input_param",
        "cl_optional_inputs_missing",
        "cl_optional_bindings_provided",
        "expression_any_string",
        "expression_any_nodefaultany",
        "expression_any_null_nodefaultany",
        "expression_any_nullstring_nodefaultany",
        "initworkdir_expreng_requirements",
        "nested_cl_bindings",
        "nested_prefixes_arrays",
        "nested_workflow",
        "requirement_priority",
        "requirement_override_hints",
        "requirement_workflow_steps",
        "stderr_redirect",
        "stderr_redirect_shortcut",
        "stderr_redirect_mediumcut",
        "wf_default_tool_default",
        "any_outputSource_compatibility",
        "step_input_default_value",
        "step_input_default_value_nullsource",
        "hints_unknown_ignored",
        "schemadef_req_tool_param",
        "schemadef_req_wf_param",
        "param_evaluation_noexpr",
        "initial_workdir_secondary_files_expr",
        "param_evaluation_expr",
        "valuefrom_secondexpr_ignored",
        "cl_basic_generation",
        "directory_input_docker",
        "input_file_literal",
        "hints_import",
        "default_path_notfound_warning",
        "shelldir_notinterpreted",
        "fileliteral_input_docker",
        "outputbinding_glob_sorted",
        "booleanflags_cl_noinputbinding",
        "outputbinding_glob_sorted",
        "success_codes",
        "cl_empty_array_input",
        "resreq_step_overrides_wf",
        "valuefrom_constant_overrides_inputs",
        "wf_step_access_undeclared_param",
        "expr_reference_self_noinput",
    ],
    "v1.1": [
        "expression_tool_int_array_output",
        "cl_gen_arrayofarrays",
        "docker_json_output_location",
        "docker_json_output_path",
        "envvar_req",
        "expression_any",
        "expression_any_null",
        "expression_outputEval",
        "expression_parseint",
        "exprtool_directory_literal",
        "exprtool_file_literal",
        "initial_workdir_empty_writable",
        "initial_workdir_empty_writable_docker",
        "initial_workdir_expr",
        "initial_workdir_output",
        "initial_workdir_trailingnl",
        "initialworkpath_output",
        "inline_expressions",
        "metadata",
        "nameroot_nameext_stdout_expr",
        "null_missing_params",
        "rename",
        "stdinout_redirect",
        "stdinout_redirect_docker",
        "stdout_redirect_docker",
        "stdout_redirect_mediumcut_docker",
        "stdout_redirect_shortcut_docker",
        "writable_stagedfiles",
        "workflow_union_default_input_with_file_provided",
        "any_input_param",
        "cl_optional_inputs_missing",
        "cl_optional_bindings_provided",
        "expression_any_string",
        "expression_any_nodefaultany",
        "expression_any_null_nodefaultany",
        "expression_any_nullstring_nodefaultany",
        "initworkdir_expreng_requirements",
        "nested_cl_bindings",
        "nested_prefixes_arrays",
        "nested_workflow",
        "requirement_priority",
        "requirement_override_hints",
        "requirement_workflow_steps",
        "stderr_redirect",
        "stderr_redirect_shortcut",
        "stderr_redirect_mediumcut",
        "wf_default_tool_default",
        "any_outputSource_compatibility",
        "step_input_default_value",
        "step_input_default_value_nullsource",
        "hints_unknown_ignored",
        "schemadef_req_tool_param",
        "schemadef_req_wf_param",
        "param_evaluation_noexpr",
        "initial_workdir_secondary_files_expr",
        "param_evaluation_expr",
        "valuefrom_secondexpr_ignored",
        "cl_basic_generation",
        "directory_input_docker",
        "input_file_literal",
        "hints_import",
        "default_path_notfound_warning",
        "shelldir_notinterpreted",
        "fileliteral_input_docker",
        "outputbinding_glob_sorted",
        "booleanflags_cl_noinputbinding",
        "outputbinding_glob_sorted",
        "success_codes",
        "cl_empty_array_input",
        "resreq_step_overrides_wf",
        "valuefrom_constant_overrides_inputs",
        "wf_step_access_undeclared_param",
        "expr_reference_self_noinput",
    ],
    "v1.2": [],
}


def load_conformance_tests(directory, path="conformance_tests.yaml"):
    conformance_tests_path = os.path.join(directory, path)
    with open(conformance_tests_path, "r") as f:
        conformance_tests = yaml.load(f)

    expanded_conformance_tests = []
    for i, conformance_test in enumerate(conformance_tests):
        if "$import" in conformance_test:
            import_path = conformance_test["$import"]
            expanded_conformance_tests.extend(load_conformance_tests(directory, import_path))
        else:
            expanded_conformance_tests.append(conformance_test)
    return expanded_conformance_tests


def main():
    version = "v1.0"
    if len(sys.argv) > 1:
        version = sys.argv[1]
    version_simple = version.replace(".", "_")
    conformance_tests = load_conformance_tests(os.path.join(THIS_DIRECTORY, version))

    green_tests_list = GREEN_TESTS[version]

    tests = ""
    green_tests = ""
    red_tests = ""
    required_tests = ""
    green_required_tests = ""
    red_required_tests = ""
    regression_tests = ""

    for i, conformance_test in enumerate(conformance_tests):
        test_with_doc = conformance_test.copy()
        if 'doc' not in test_with_doc:
            raise Exception("No doc in test %s" % test_with_doc)
        del test_with_doc["doc"]
        cwl_test_def = yaml.dump(test_with_doc, default_flow_style=False)
        cwl_test_def = "\n".join(["            %s" % l for l in cwl_test_def.splitlines()])
        label = conformance_test.get("label", str(i))
        tags = conformance_test.get("tags", [])

        template_kwargs = {
            'version_simple': version_simple,
            'version': version,
            'doc': conformance_test['doc'],
            'cwl_test_def': cwl_test_def,
            'label': label.replace("-", "_"),
        }
        test_body = TEST_TEMPLATE.safe_substitute(template_kwargs)

        tests += test_body
        is_required = "required" in tags
        is_green = label in green_tests_list
        is_regression = label in REGRESSIONS

        if is_green:
            green_tests += test_body
        else:
            red_tests += test_body
        if is_required:
            required_tests += test_body
            if is_green:
                green_required_tests += test_body
            else:
                red_required_tests += test_body
        if is_regression:
            regression_tests += test_body

    def generate_test_file(tests):
        return TEST_FILE_TEMPLATE.safe_substitute({
            'version': version,
            'version_simple': version_simple,
            'tests': tests,
        })

    test_file_contents = generate_test_file(tests)

    green_test_file_contents = generate_test_file(green_tests)

    red_test_file_contents = generate_test_file(red_tests)

    required_test_file_contents = generate_test_file(required_tests)

    required_red_test_file_contents = generate_test_file(red_required_tests)
    required_green_test_file_contents = generate_test_file(green_required_tests)
    regressed_test_file_contents = generate_test_file(regression_tests)

    def write_test_cases(contents, suffix=None):
        if suffix is None:
            test_file = "test_cwl_conformance_%s.py" % version_simple
        else:
            test_file = "test_cwl_conformance_%s_%s.py" % (suffix, version_simple)

        with open(os.path.join(CWL_TESTS_DIRECTORY, test_file), "w") as f:
            f.write(contents)

    write_test_cases(test_file_contents)
    write_test_cases(green_test_file_contents, "green")
    write_test_cases(red_test_file_contents, "red")
    write_test_cases(required_test_file_contents, "required")
    write_test_cases(regressed_test_file_contents, "regressed")
    write_test_cases(required_red_test_file_contents, "required_red")
    write_test_cases(required_green_test_file_contents, "required_green")


if __name__ == "__main__":
    main()
