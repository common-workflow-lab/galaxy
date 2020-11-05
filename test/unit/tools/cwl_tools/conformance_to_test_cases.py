import os
import string
import sys

import yaml

THIS_DIRECTORY = os.path.dirname(os.path.realpath(__file__))
GALAXY_ROOT_DIR = os.path.abspath(os.path.join(THIS_DIRECTORY, os.pardir, os.pardir, os.pardir, os.pardir))
API_TEST_DIRECTORY = os.path.join(GALAXY_ROOT_DIR, "lib", "galaxy_test", "api")
CWL_TESTS_DIRECTORY = os.path.join(API_TEST_DIRECTORY, "cwl")

TEST_FILE_TEMPLATE = string.Template('''"""Test CWL conformance for version ${version}."""

import pytest

from ..test_workflows_cwl import BaseCwlWorklfowTestCase


class CwlConformanceTestCase(BaseCwlWorklfowTestCase):
    """Test case mapping to CWL conformance tests for version ${version}."""
$tests''')

TEST_TEMPLATE = string.Template('''
${marks}    def test_conformance_${version_simple}_${label}(self):
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

# Regressions -- hopefully not needed anymore
REGRESSIONS = []
RED_TESTS.update({r: 'bug' for r in REGRESSIONS})

GREEN_TESTS = {
    "v1.0": [
        "wf_simple",
        "embedded_subworkflow",
        "expressionlib_tool_wf_override",
        "nameroot_nameext_generated",
        "scatter_embedded_subworkflow",
        "scatter_multi_input_embedded_subworkflow",
        "step_input_default_value_overriden_2nd_step_null",
        "valuefrom_wf_step_other",
        "wf_scatter_oneparam_valueFrom",
        "wf_scatter_oneparam_valuefrom_twice_current_el",
        "wf_scatter_single_param",
        "wf_scatter_two_dotproduct",
        "wf_scatter_twopar_oneinput_flattenedmerge",
        "wf_wc_scatter_multiple_nested",
        "workflow_any_input_with_file_provided",
        "workflow_any_input_with_integer_provided",
        "workflow_any_input_with_mixed_array_provided",
        "workflow_any_input_with_string_provided",
        "workflow_embedded_subworkflow_embedded_subsubworkflow",
        "workflow_embedded_subworkflow_with_tool_and_subsubworkflow",
        "workflow_file_input_default_specified",
        "workflow_integer_input",
        "workflow_integer_input_default_and_tool_integer_input_default",
        "workflow_integer_input_default_specified",
        "workflow_integer_input_default_unspecified",
        "workflow_integer_input_optional_specified",
        "workflowstep_int_array_input_output",
        "workflowstep_valuefrom_file_basename",
        "workflowstep_valuefrom_string",
        'directory_output',
        'wf_compound_doc',
        'step_input_default_value_nosource',
        "wf_input_default_missing",
        "wf_input_default_provided",
        "wf_scatter_dotproduct_twoempty",
        "wf_scatter_emptylist",
        "wf_step_connect_undeclared_param",
        "wf_two_inputfiles_namecollision",
        "wf_wc_expressiontool",
        "wf_wc_nomultiple",
        "wf_wc_scatter_multiple_merge",
        "wf_wc_scatter_multiple_flattened",
        "wf_wc_scatter",
        "wf_wc_parseInt",
        "workflow_union_default_input_unspecified",
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
        "any_without_defaults_specified_fails",
        "any_without_defaults_unspecified_fails",
        "clt_any_input_with_file_provided",
        "clt_any_input_with_integer_provided",
        "clt_any_input_with_string_provided",
        "clt_file_size_property_with_empty_file",
        "clt_file_size_property_with_multi_file",
        "clt_optional_union_input_file_or_files_with_nothing_provided",
        "clt_optional_union_input_file_or_files_with_single_file_provided",
        "directory_input_param_ref",
        "inlinejs_req_expressions",
        "input_dir_inputbinding",
        "multiple_glob_expr_list",
        "no_outputs_commandlinetool",
        "no_outputs_workflow",
        "output_secondaryfile_optional",
        "param_notnull_expr",
        "shelldir_quoted",
        "valuefrom_ignored_null",
    ],
    "v1.1": [
        "wf_simple",
        'directory_output',
        'wf_compound_doc',
        'step_input_default_value_nosource',
        "wf_input_default_missing",
        "wf_input_default_provided",
        "wf_scatter_dotproduct_twoempty",
        "wf_scatter_emptylist",
        "wf_step_connect_undeclared_param",
        "wf_two_inputfiles_namecollision",
        "wf_wc_expressiontool",
        "wf_wc_nomultiple",
        "wf_wc_scatter_multiple_merge",
        "wf_wc_scatter_multiple_flattened",
        "wf_wc_scatter",
        "wf_wc_parseInt",
        "workflow_union_default_input_unspecified",
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
        "any_without_defaults_specified_fails",
        "any_without_defaults_unspecified_fails",
        "clt_any_input_with_file_provided",
        "clt_any_input_with_integer_provided",
        "clt_any_input_with_string_provided",
        "clt_file_size_property_with_empty_file",
        "clt_file_size_property_with_multi_file",
        "clt_optional_union_input_file_or_files_with_nothing_provided",
        "clt_optional_union_input_file_or_files_with_single_file_provided",
        "directory_input_param_ref",
        "inlinejs_req_expressions",
        "input_dir_inputbinding",
        "multiple_glob_expr_list",
        "no_outputs_commandlinetool",
        "no_outputs_workflow",
        "output_secondaryfile_optional",
        "param_notnull_expr",
        "shelldir_quoted",
        "valuefrom_ignored_null",
        "dynamic_initial_workdir",
        "glob_full_path",
        "initial_work_dir_output",
        "inputBinding_position_expr",
        "input_records_file_entry_with_format_and_bad_entry_array_file_format",
        "input_records_file_entry_with_format_and_bad_entry_file_format",
        "input_records_file_entry_with_format_and_bad_regular_input_file_format",
        "listing_default_none",
        "listing_loadListing_deep",
        "listing_loadListing_none",
        "listing_loadListing_shallow",
        "optional_numerical_output_returns_0_not_null",
        "secondary_files_workflow_propagation",
        "timelimit_basic",
        "timelimit_basic_wf",
        "timelimit_from_expression",
        "timelimit_from_expression_wf",
        "timelimit_invalid",
    ],
    "v1.2": [
        "wf_simple",
        'directory_output',
        'wf_compound_doc',
        'step_input_default_value_nosource',
        "wf_input_default_missing",
        "wf_input_default_provided",
        "wf_scatter_dotproduct_twoempty",
        "wf_scatter_emptylist",
        "wf_step_connect_undeclared_param",
        "wf_two_inputfiles_namecollision",
        "wf_wc_expressiontool",
        "wf_wc_nomultiple",
        "wf_wc_scatter_multiple_merge",
        "wf_wc_scatter_multiple_flattened",
        "wf_wc_scatter",
        "wf_wc_parseInt",
        "workflow_union_default_input_unspecified",
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
        "any_without_defaults_specified_fails",
        "any_without_defaults_unspecified_fails",
        "clt_any_input_with_file_provided",
        "clt_any_input_with_integer_provided",
        "clt_any_input_with_string_provided",
        "clt_file_size_property_with_empty_file",
        "clt_file_size_property_with_multi_file",
        "clt_optional_union_input_file_or_files_with_nothing_provided",
        "clt_optional_union_input_file_or_files_with_single_file_provided",
        "directory_input_param_ref",
        "inlinejs_req_expressions",
        "input_dir_inputbinding",
        "multiple_glob_expr_list",
        "no_outputs_commandlinetool",
        "no_outputs_workflow",
        "output_secondaryfile_optional",
        "param_notnull_expr",
        "shelldir_quoted",
        "valuefrom_ignored_null",
        "dynamic_initial_workdir",
        "inputBinding_position_expr",
        "input_records_file_entry_with_format_and_bad_entry_array_file_format",
        "input_records_file_entry_with_format_and_bad_entry_file_format",
        "input_records_file_entry_with_format_and_bad_regular_input_file_format",
        "listing_default_none",
        "listing_loadListing_deep",
        "listing_loadListing_none",
        "listing_loadListing_shallow",
        "optional_numerical_output_returns_0_not_null",
        "secondary_files_workflow_propagation",
        "timelimit_basic",
        "timelimit_basic_wf",
        "timelimit_from_expression",
        "timelimit_from_expression_wf",
        "timelimit_invalid",
    ],
}


def load_conformance_tests(directory, path="conformance_tests.yaml"):
    conformance_tests_path = os.path.join(directory, path)
    with open(conformance_tests_path) as f:
        conformance_tests = yaml.safe_load(f)

    expanded_conformance_tests = []
    for conformance_test in conformance_tests:
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
    green_tests_found = set()
    all_tests_found = set()

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
        cwl_test_def = "\n".join([f"            {line}" for line in cwl_test_def.splitlines()])
        label = conformance_test.get("label", str(i))
        tags = conformance_test.get("tags", [])
        is_required = "required" in tags
        is_green = label in green_tests_list
        is_regression = label in REGRESSIONS

        marks = "    @pytest.mark.cwl_conformance\n"
        marks += f"    @pytest.mark.cwl_conformance_{version_simple}\n"
        for tag in tags:
            marks += f"    @pytest.mark.{tag}\n"
        if is_green:
            marks += "    @pytest.mark.green\n"
        else:
            marks += "    @pytest.mark.red\n"
        if is_regression:
            marks += "    @pytest.mark.regression\n"

        if "command_line_tool" not in tags and "workflow" not in tags and "expression_tool" not in tags:
            print("PROBLEM - test tagged with neither command_line_tool, expression_tool, nor workflow [%s]" % label)

        template_kwargs = {
            'version_simple': version_simple,
            'version': version,
            'doc': conformance_test['doc'],
            'cwl_test_def': cwl_test_def,
            'label': label.replace("-", "_"),
            'marks': marks,
        }
        test_body = TEST_TEMPLATE.safe_substitute(template_kwargs)

        tests += test_body
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

        if label in all_tests_found:
            print("PROBLEM - Duplicate label found [%s]" % label)
        all_tests_found.add(label)
        if is_green:
            green_tests_found.add(label)

    def generate_test_file(tests):
        return TEST_FILE_TEMPLATE.safe_substitute({
            'version': version,
            'version_simple': version_simple,
            'tests': tests,
        })

    test_file_contents = generate_test_file(tests)

    def write_test_cases(contents, suffix=None):
        if suffix is None:
            test_file = f"test_cwl_conformance_{version_simple}.py"
        else:
            test_file = f"test_cwl_conformance_{suffix}_{version_simple}.py"

        with open(os.path.join(CWL_TESTS_DIRECTORY, test_file), "w") as f:
            f.write(contents)

    write_test_cases(test_file_contents)
    for green_test in green_tests_list:
        if green_test not in green_tests_found:
            print("PROBLEM - Failed to find annotated green test [%s]" % green_test)


if __name__ == "__main__":
    main()
