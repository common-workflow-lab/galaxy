
"""Test CWL conformance for version $version."""

from .test_workflows_cwl import BaseCwlWorklfowTestCase


class CwlConformanceTestCase(BaseCwlWorklfowTestCase):
    """Test case mapping to CWL conformance tests for version $version."""

    def test_conformance_v1_0_cl_basic_generation(self):
        """General test of command line generation

        Generated from::

            job: v1.0/bwa-mem-job.json
            label: cl_basic_generation
            output:
              args:
              - bwa
              - mem
              - -t
              - '2'
              - -I
              - 1,2,3,4
              - -m
              - '3'
              - chr20.fa
              - example_human_Illumina.pe_1.fastq
              - example_human_Illumina.pe_2.fastq
            tags:
            - required
            - command_line_tool
            tool: v1.0/bwa-mem-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """General test of command line generation""")

    def test_conformance_v1_0_nested_prefixes_arrays(self):
        """Test nested prefixes with arrays

        Generated from::

            job: v1.0/bwa-mem-job.json
            label: nested_prefixes_arrays
            output:
              args:
              - bwa
              - mem
              - chr20.fa
              - -XXX
              - -YYY
              - example_human_Illumina.pe_1.fastq
              - -YYY
              - example_human_Illumina.pe_2.fastq
            tags:
            - required
            - command_line_tool
            tool: v1.0/binding-test.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test nested prefixes with arrays""")

    def test_conformance_v1_0_nested_cl_bindings(self):
        """Test nested command line bindings

        Generated from::

            job: v1.0/tmap-job.json
            label: nested_cl_bindings
            output:
              args:
              - tmap
              - mapall
              - stage1
              - map1
              - --min-seq-length
              - '20'
              - map2
              - --min-seq-length
              - '20'
              - stage2
              - map1
              - --max-seq-length
              - '20'
              - --min-seq-length
              - '10'
              - --seed-length
              - '16'
              - map2
              - --max-seed-hits
              - '-1'
              - --max-seq-length
              - '20'
              - --min-seq-length
              - '10'
            tags:
            - schema_def
            - command_line_tool
            tool: v1.0/tmap-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test nested command line bindings""")

    def test_conformance_v1_0_cl_optional_inputs_missing(self):
        """Test command line with optional input (missing)

        Generated from::

            job: v1.0/cat-job.json
            label: cl_optional_inputs_missing
            output:
              args:
              - cat
              - hello.txt
            tags:
            - required
            - command_line_tool
            tool: v1.0/cat1-testcli.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test command line with optional input (missing)""")

    def test_conformance_v1_0_cl_optional_bindings_provided(self):
        """Test command line with optional input (provided)

        Generated from::

            job: v1.0/cat-n-job.json
            label: cl_optional_bindings_provided
            output:
              args:
              - cat
              - -n
              - hello.txt
            tags:
            - required
            - command_line_tool
            tool: v1.0/cat1-testcli.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test command line with optional input (provided)""")

    def test_conformance_v1_0_initworkdir_expreng_requirements(self):
        """Test InitialWorkDirRequirement ExpressionEngineRequirement.engineConfig feature

        Generated from::

            job: v1.0/cat-job.json
            label: initworkdir_expreng_requirements
            output:
              foo:
                checksum: sha1$63da67422622fbf9251a046d7a34b7ea0fd4fead
                class: File
                location: foo.txt
                size: 22
            tags:
            - initial_work_dir
            - inline_javascript
            - command_line_tool
            tool: v1.0/template-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test InitialWorkDirRequirement ExpressionEngineRequirement.engineConfig feature""")

    def test_conformance_v1_0_stdout_redirect_docker(self):
        """Test command execution in Docker with stdout redirection

        Generated from::

            job: v1.0/cat-job.json
            label: stdout_redirect_docker
            output:
              output_file:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: output.txt
                size: 13
            tags:
            - required
            - command_line_tool
            tool: v1.0/cat3-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test command execution in Docker with stdout redirection""")

    def test_conformance_v1_0_stdout_redirect_shortcut_docker(self):
        """Test command execution in Docker with shortcut stdout redirection

        Generated from::

            job: v1.0/cat-job.json
            label: stdout_redirect_shortcut_docker
            output:
              output_file:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: Any
                size: 13
            tags:
            - required
            - command_line_tool
            tool: v1.0/cat3-tool-shortcut.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test command execution in Docker with shortcut stdout redirection""")

    def test_conformance_v1_0_stdout_redirect_mediumcut_docker(self):
        """Test command execution in Docker with mediumcut stdout redirection

        Generated from::

            job: v1.0/cat-job.json
            label: stdout_redirect_mediumcut_docker
            output:
              output_file:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: cat-out
                size: 13
            tags:
            - required
            - command_line_tool
            tool: v1.0/cat3-tool-mediumcut.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test command execution in Docker with mediumcut stdout redirection""")

    def test_conformance_v1_0_stderr_redirect(self):
        """Test command line with stderr redirection

        Generated from::

            job: v1.0/empty.json
            label: stderr_redirect
            output:
              output_file:
                checksum: sha1$f1d2d2f924e986ac86fdf7b36c94bcdf32beec15
                class: File
                location: error.txt
                size: 4
            tags:
            - shell_command
            - command_line_tool
            tool: v1.0/stderr.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test command line with stderr redirection""")

    def test_conformance_v1_0_stderr_redirect_shortcut(self):
        """Test command line with stderr redirection, brief syntax

        Generated from::

            job: v1.0/empty.json
            label: stderr_redirect_shortcut
            output:
              output_file:
                checksum: sha1$f1d2d2f924e986ac86fdf7b36c94bcdf32beec15
                class: File
                location: Any
                size: 4
            tags:
            - shell_command
            - command_line_tool
            tool: v1.0/stderr-shortcut.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test command line with stderr redirection, brief syntax""")

    def test_conformance_v1_0_stderr_redirect_mediumcut(self):
        """Test command line with stderr redirection, named brief syntax

        Generated from::

            job: v1.0/empty.json
            label: stderr_redirect_mediumcut
            output:
              output_file:
                checksum: sha1$f1d2d2f924e986ac86fdf7b36c94bcdf32beec15
                class: File
                location: std.err
                size: 4
            tags:
            - shell_command
            - command_line_tool
            tool: v1.0/stderr-mediumcut.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test command line with stderr redirection, named brief syntax""")

    def test_conformance_v1_0_stdinout_redirect_docker(self):
        """Test command execution in Docker with stdin and stdout redirection

        Generated from::

            job: v1.0/cat-job.json
            label: stdinout_redirect_docker
            output:
              output_txt:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: output.txt
                size: 13
            tags:
            - required
            - command_line_tool
            tool: v1.0/cat4-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test command execution in Docker with stdin and stdout redirection""")

    def test_conformance_v1_0_expression_any(self):
        """Test default usage of Any in expressions.

        Generated from::

            job: v1.0/empty.json
            label: expression_any
            output:
              output: 1
            tags:
            - inline_javascript
            - expression_tool
            tool: v1.0/null-expression1-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test default usage of Any in expressions.""")

    def test_conformance_v1_0_expression_any_null(self):
        """Test explicitly passing null to Any type inputs with default values.

        Generated from::

            job: v1.0/null-expression1-job.json
            label: expression_any_null
            output:
              output: 1
            tags:
            - inline_javascript
            - expression_tool
            tool: v1.0/null-expression1-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test explicitly passing null to Any type inputs with default values.""")

    def test_conformance_v1_0_expression_any_string(self):
        """Testing the string 'null' does not trip up an Any with a default value.

        Generated from::

            job: v1.0/null-expression2-job.json
            label: expression_any_string
            output:
              output: 2
            tags:
            - inline_javascript
            - expression_tool
            tool: v1.0/null-expression1-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Testing the string 'null' does not trip up an Any with a default value.""")

    def test_conformance_v1_0_expression_any_nodefaultany(self):
        """Test Any without defaults cannot be unspecified.

        Generated from::

            job: v1.0/empty.json
            label: expression_any_nodefaultany
            should_fail: true
            tags:
            - inline_javascript
            - expression_tool
            tool: v1.0/null-expression2-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test Any without defaults cannot be unspecified.""")

    def test_conformance_v1_0_expression_any_null_nodefaultany(self):
        """Test explicitly passing null to Any type without a default value.

        Generated from::

            job: v1.0/null-expression1-job.json
            label: expression_any_null_nodefaultany
            should_fail: true
            tags:
            - inline_javascript
            - expression_tool
            tool: v1.0/null-expression2-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test explicitly passing null to Any type without a default value.""")

    def test_conformance_v1_0_expression_any_nullstring_nodefaultany(self):
        """Testing the string 'null' does not trip up an Any without a default value.

        Generated from::

            job: v1.0/null-expression2-job.json
            label: expression_any_nullstring_nodefaultany
            output:
              output: 2
            tags:
            - inline_javascript
            - expression_tool
            tool: v1.0/null-expression2-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Testing the string 'null' does not trip up an Any without a default value.""")

    def test_conformance_v1_0_any_outputSource_compatibility(self):
        """Testing Any type compatibility in outputSource

        Generated from::

            job: v1.0/any-type-job.json
            label: any_outputSource_compatibility
            output:
              output1:
              - hello
              - world
              output2:
              - foo
              - bar
              output3: hello
            tags:
            - required
            - workflow
            tool: v1.0/any-type-compat.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Testing Any type compatibility in outputSource""")

    def test_conformance_v1_0_stdinout_redirect(self):
        """Test command execution in with stdin and stdout redirection

        Generated from::

            job: v1.0/cat-job.json
            label: stdinout_redirect
            output:
              output:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: output
                size: 13
            tags:
            - required
            - command_line_tool
            tool: v1.0/cat-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test command execution in with stdin and stdout redirection""")

    def test_conformance_v1_0_expression_parseint(self):
        """Test ExpressionTool with Docker-based expression engine

        Generated from::

            job: v1.0/parseInt-job.json
            label: expression_parseint
            output:
              output: 42
            tags:
            - inline_javascript
            - expression_tool
            tool: v1.0/parseInt-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test ExpressionTool with Docker-based expression engine""")

    def test_conformance_v1_0_expression_outputEval(self):
        """Test outputEval to transform output

        Generated from::

            job: v1.0/wc-job.json
            label: expression_outputEval
            output:
              output: 16
            tags:
            - inline_javascript
            - command_line_tool
            tool: v1.0/wc2-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test outputEval to transform output""")

    def test_conformance_v1_0_wf_wc_parseInt(self):
        """Test two step workflow with imported tools

        Generated from::

            job: v1.0/wc-job.json
            label: wf_wc_parseInt
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: v1.0/count-lines1-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test two step workflow with imported tools""")

    def test_conformance_v1_0_wf_wc_expressiontool(self):
        """Test two step workflow with inline tools

        Generated from::

            job: v1.0/wc-job.json
            label: wf_wc_expressiontool
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: v1.0/count-lines2-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test two step workflow with inline tools""")

    def test_conformance_v1_0_wf_wc_scatter(self):
        """Test single step workflow with Scatter step

        Generated from::

            job: v1.0/count-lines3-job.json
            label: wf_wc_scatter
            output:
              count_output:
              - 16
              - 1
            tags:
            - scatter
            - inline_javascript
            - workflow
            tool: v1.0/count-lines3-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test single step workflow with Scatter step""")

    def test_conformance_v1_0_wf_wc_scatter_multiple_merge(self):
        """Test single step workflow with Scatter step and two data links connected to
same input, default merge behavior


        Generated from::

            job: v1.0/count-lines4-job.json
            label: wf_wc_scatter_multiple_merge
            output:
              count_output:
              - 16
              - 1
            tags:
            - scatter
            - multiple_input
            - inline_javascript
            - workflow
            tool: v1.0/count-lines4-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test single step workflow with Scatter step and two data links connected to
same input, default merge behavior
""")

    def test_conformance_v1_0_wf_wc_scatter_multiple_nested(self):
        """Test single step workflow with Scatter step and two data links connected to
same input, nested merge behavior


        Generated from::

            job: v1.0/count-lines6-job.json
            label: wf_wc_scatter_multiple_nested
            output:
              count_output:
              - 32
              - 2
            tags:
            - scatter
            - multiple_input
            - inline_javascript
            - workflow
            tool: v1.0/count-lines6-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test single step workflow with Scatter step and two data links connected to
same input, nested merge behavior
""")

    def test_conformance_v1_0_wf_wc_scatter_multiple_flattened(self):
        """Test single step workflow with Scatter step and two data links connected to
same input, flattened merge behavior


        Generated from::

            job: v1.0/count-lines6-job.json
            label: wf_wc_scatter_multiple_flattened
            output:
              count_output: 34
            tags:
            - multiple_input
            - inline_javascript
            - workflow
            tool: v1.0/count-lines7-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test single step workflow with Scatter step and two data links connected to
same input, flattened merge behavior
""")

    def test_conformance_v1_0_wf_wc_nomultiple(self):
        """Test that no MultipleInputFeatureRequirement is necessary when
workflow step source is a single-item list


        Generated from::

            job: v1.0/count-lines6-job.json
            label: wf_wc_nomultiple
            output:
              count_output: 32
            tags:
            - inline_javascript
            - workflow
            tool: v1.0/count-lines13-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that no MultipleInputFeatureRequirement is necessary when
workflow step source is a single-item list
""")

    def test_conformance_v1_0_wf_input_default_missing(self):
        """Test workflow with default value for input parameter (missing)

        Generated from::

            job: v1.0/empty.json
            label: wf_input_default_missing
            output:
              count_output: 1
            tags:
            - inline_javascript
            - workflow
            tool: v1.0/count-lines5-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow with default value for input parameter (missing)""")

    def test_conformance_v1_0_wf_input_default_provided(self):
        """Test workflow with default value for input parameter (provided)

        Generated from::

            job: v1.0/wc-job.json
            label: wf_input_default_provided
            output:
              count_output: 16
            tags:
            - inline_javacscript
            - workflow
            tool: v1.0/count-lines5-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow with default value for input parameter (provided)""")

    def test_conformance_v1_0_wf_default_tool_default(self):
        """Test that workflow defaults override tool defaults

        Generated from::

            job: v1.0/empty.json
            label: wf_default_tool_default
            output:
              default_output: workflow_default
            tags:
            - required
            - workflow
            tool: v1.0/echo-wf-default.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that workflow defaults override tool defaults""")

    def test_conformance_v1_0_envvar_req(self):
        """Test EnvVarRequirement

        Generated from::

            job: v1.0/env-job.json
            label: envvar_req
            output:
              out:
                checksum: sha1$b3ec4ed1749c207e52b3a6d08c59f31d83bff519
                class: File
                location: out
                size: 15
            tags:
            - env_var
            - command_line_tool
            tool: v1.0/env-tool1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test EnvVarRequirement""")

    def test_conformance_v1_0_wf_scatter_single_param(self):
        """Test workflow scatter with single scatter parameter

        Generated from::

            job: v1.0/scatter-job1.json
            label: wf_scatter_single_param
            output:
              out:
              - foo one
              - foo two
              - foo three
              - foo four
            tags:
            - scatter
            - workflow
            tool: v1.0/scatter-wf1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with single scatter parameter""")

    def test_conformance_v1_0_wf_scatter_two_nested_crossproduct(self):
        """Test workflow scatter with two scatter parameters and nested_crossproduct join method

        Generated from::

            job: v1.0/scatter-job2.json
            label: wf_scatter_two_nested_crossproduct
            output:
              out:
              - - foo one three
                - foo one four
              - - foo two three
                - foo two four
            tags:
            - scatter
            - workflow
            tool: v1.0/scatter-wf2.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with two scatter parameters and nested_crossproduct join method""")

    def test_conformance_v1_0_wf_scatter_two_flat_crossproduct(self):
        """Test workflow scatter with two scatter parameters and flat_crossproduct join method

        Generated from::

            job: v1.0/scatter-job2.json
            label: wf_scatter_two_flat_crossproduct
            output:
              out:
              - foo one three
              - foo one four
              - foo two three
              - foo two four
            tags:
            - scatter
            - workflow
            tool: v1.0/scatter-wf3.cwl#main
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with two scatter parameters and flat_crossproduct join method""")

    def test_conformance_v1_0_wf_scatter_two_dotproduct(self):
        """Test workflow scatter with two scatter parameters and dotproduct join method

        Generated from::

            job: v1.0/scatter-job2.json
            label: wf_scatter_two_dotproduct
            output:
              out:
              - foo one three
              - foo two four
            tags:
            - scatter
            - workflow
            tool: v1.0/scatter-wf4.cwl#main
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with two scatter parameters and dotproduct join method""")

    def test_conformance_v1_0_wf_scatter_emptylist(self):
        """Test workflow scatter with single empty list parameter

        Generated from::

            job: v1.0/scatter-empty-job1.json
            label: wf_scatter_emptylist
            output:
              out: []
            tags:
            - scatter
            - workflow
            tool: v1.0/scatter-wf1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with single empty list parameter""")

    def test_conformance_v1_0_wf_scatter_nested_crossproduct_secondempty(self):
        """Test workflow scatter with two scatter parameters and nested_crossproduct join method with second list empty

        Generated from::

            job: v1.0/scatter-empty-job2.json
            label: wf_scatter_nested_crossproduct_secondempty
            output:
              out:
              - []
              - []
            tags:
            - scatter
            - workflow
            tool: v1.0/scatter-wf2.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with two scatter parameters and nested_crossproduct join method with second list empty""")

    def test_conformance_v1_0_wf_scatter_nested_crossproduct_firstempty(self):
        """Test workflow scatter with two scatter parameters and nested_crossproduct join method with first list empty

        Generated from::

            job: v1.0/scatter-empty-job3.json
            label: wf_scatter_nested_crossproduct_firstempty
            output:
              out: []
            tags:
            - scatter
            - workflow
            tool: v1.0/scatter-wf3.cwl#main
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with two scatter parameters and nested_crossproduct join method with first list empty""")

    def test_conformance_v1_0_wf_scatter_flat_crossproduct_oneempty(self):
        """Test workflow scatter with two scatter parameters, one of which is empty and flat_crossproduct join method

        Generated from::

            job: v1.0/scatter-empty-job2.json
            label: wf_scatter_flat_crossproduct_oneempty
            output:
              out: []
            tags:
            - scatter
            - workflow
            tool: v1.0/scatter-wf3.cwl#main
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with two scatter parameters, one of which is empty and flat_crossproduct join method""")

    def test_conformance_v1_0_wf_scatter_dotproduct_twoempty(self):
        """Test workflow scatter with two empty scatter parameters and dotproduct join method

        Generated from::

            job: v1.0/scatter-empty-job4.json
            label: wf_scatter_dotproduct_twoempty
            output:
              out: []
            tags:
            - scatter
            - workflow
            tool: v1.0/scatter-wf4.cwl#main
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with two empty scatter parameters and dotproduct join method""")

    def test_conformance_v1_0_any_input_param(self):
        """Test Any type input parameter

        Generated from::

            job: v1.0/env-job.json
            label: any_input_param
            output:
              out: 'hello test env
            
                '
            tags:
            - required
            - command_line_tool
            tool: v1.0/echo-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test Any type input parameter""")

    def test_conformance_v1_0_nested_workflow(self):
        """Test nested workflow

        Generated from::

            job: v1.0/wc-job.json
            label: nested_workflow
            output:
              count_output: 16
            tags:
            - subworkflow
            - workflow
            tool: v1.0/count-lines8-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test nested workflow""")

    def test_conformance_v1_0_requirement_priority(self):
        """Test requirement priority

        Generated from::

            job: v1.0/env-job.json
            label: requirement_priority
            output:
              out:
                checksum: sha1$b3ec4ed1749c207e52b3a6d08c59f31d83bff519
                class: File
                location: out
                size: 15
            tags:
            - env_var
            - workflow
            tool: v1.0/env-wf1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test requirement priority""")

    def test_conformance_v1_0_requirement_override_hints(self):
        """Test requirements override hints

        Generated from::

            job: v1.0/env-job.json
            label: requirement_override_hints
            output:
              out:
                checksum: sha1$cdc1e84968261d6a7575b5305945471f8be199b6
                class: File
                location: out
                size: 9
            tags:
            - env_var
            - workflow
            tool: v1.0/env-wf2.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test requirements override hints""")

    def test_conformance_v1_0_requirement_workflow_steps(self):
        """Test requirements on workflow steps

        Generated from::

            job: v1.0/env-job.json
            label: requirement_workflow_steps
            output:
              out:
                checksum: sha1$cdc1e84968261d6a7575b5305945471f8be199b6
                class: File
                location: out
                size: 9
            tags:
            - env_var
            - workflow
            tool: v1.0/env-wf3.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test requirements on workflow steps""")

    def test_conformance_v1_0_step_input_default_value(self):
        """Test default value on step input parameter

        Generated from::

            job: v1.0/empty.json
            label: step_input_default_value
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: v1.0/count-lines9-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test default value on step input parameter""")

    def test_conformance_v1_0_step_input_default_value_nosource(self):
        """Test use default value on step input parameter with empty source

        Generated from::

            job: v1.0/empty.json
            label: step_input_default_value_nosource
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: v1.0/count-lines11-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test use default value on step input parameter with empty source""")

    def test_conformance_v1_0_step_input_default_value_nullsource(self):
        """Test use default value on step input parameter with null source

        Generated from::

            job: v1.0/file1-null.json
            label: step_input_default_value_nullsource
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: v1.0/count-lines11-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test use default value on step input parameter with null source""")

    def test_conformance_v1_0_step_input_default_value_overriden(self):
        """Test default value on step input parameter overridden by provided source

        Generated from::

            job: v1.0/cat-job.json
            label: step_input_default_value_overriden
            output:
              count_output: 1
            tags:
            - inline_javascript
            - workflow
            tool: v1.0/count-lines11-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test default value on step input parameter overridden by provided source""")

    def test_conformance_v1_0_wf_simple(self):
        """Test simple workflow

        Generated from::

            job: v1.0/revsort-job.json
            label: wf_simple
            output:
              output:
                checksum: sha1$b9214658cc453331b62c2282b772a5c063dbd284
                class: File
                location: output.txt
                size: 1111
            tags:
            - required
            - workflow
            tool: v1.0/revsort.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test simple workflow""")

    def test_conformance_v1_0_hints_unknown_ignored(self):
        """Test unknown hints are ignored.

        Generated from::

            job: v1.0/cat-job.json
            label: hints_unknown_ignored
            output:
              output_file:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: output.txt
                size: 13
            tags:
            - required
            - command_line_tool
            tool: v1.0/cat5-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test unknown hints are ignored.""")

    def test_conformance_v1_0_initial_workdir_secondary_files_expr(self):
        """Test InitialWorkDirRequirement linking input files and capturing secondaryFiles
on input and output. Also tests the use of a variety of parameter references
and expressions in the secondaryFiles field.


        Generated from::

            job: v1.0/search-job.json
            label: initial_workdir_secondary_files_expr
            output:
              indexedfile:
                checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                class: File
                location: input.txt
                secondaryFiles:
                - checksum: sha1$553f3a09003a9f69623f03bec13c0b078d706023
                  class: File
                  location: input.txt.idx1
                  size: 1500
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: input.idx2
                  size: 0
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: input.txt.idx3
                  size: 0
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: input.txt.idx4
                  size: 0
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: input.txt.idx5
                  size: 0
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: input.idx6.txt
                  size: 0
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: input.txt.idx7
                  size: 0
                - checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                  class: File
                  location: hello.txt
                  size: 13
                - class: Directory
                  listing:
                  - basename: index
                    checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                    class: File
                    location: index
                    size: 0
                  location: input.txt_idx8
                size: 1111
              outfile:
                checksum: sha1$e2dc9daaef945ac15f01c238ed2f1660f60909a0
                class: File
                location: result.txt
                size: 142
            tags:
            - initial_work_dir
            - inline_javascript
            - command_line_tool
            tool: v1.0/search.cwl#main
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test InitialWorkDirRequirement linking input files and capturing secondaryFiles
on input and output. Also tests the use of a variety of parameter references
and expressions in the secondaryFiles field.
""")

    def test_conformance_v1_0_rename(self):
        """Test InitialWorkDirRequirement with expression in filename.


        Generated from::

            job: v1.0/rename-job.json
            label: rename
            output:
              outfile:
                checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                class: File
                location: fish.txt
                size: 1111
            tags:
            - initial_work_dir
            - command_line_tool
            tool: v1.0/rename.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test InitialWorkDirRequirement with expression in filename.
""")

    def test_conformance_v1_0_initial_workdir_trailingnl(self):
        """Test if trailing newline is present in file entry in InitialWorkDir

        Generated from::

            job: v1.0/string-job.json
            label: initial_workdir_trailingnl
            output:
              out:
                checksum: sha1$6a47aa22b2a9d13a66a24b3ee5eaed95ce4753cf
                class: File
                location: example.conf
                size: 16
            tags:
            - initial_work_dir
            - command_line_tool
            tool: v1.0/iwdr-entry.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test if trailing newline is present in file entry in InitialWorkDir""")

    def test_conformance_v1_0_inline_expressions(self):
        """Test inline expressions


        Generated from::

            job: v1.0/wc-job.json
            label: inline_expressions
            output:
              output: 16
            tags:
            - inline_javascript
            - command_line_tool
            tool: v1.0/wc4-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test inline expressions
""")

    def test_conformance_v1_0_schemadef_req_tool_param(self):
        """Test SchemaDefRequirement definition used in tool parameter


        Generated from::

            job: v1.0/schemadef-job.json
            label: schemadef_req_tool_param
            output:
              output:
                checksum: sha1$f12e6cfe70f3253f70b0dbde17c692e7fb0f1e5e
                class: File
                location: output.txt
                size: 12
            tags:
            - schema_def
            - command_line_tool
            tool: v1.0/schemadef-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test SchemaDefRequirement definition used in tool parameter
""")

    def test_conformance_v1_0_schemadef_req_wf_param(self):
        """Test SchemaDefRequirement definition used in workflow parameter


        Generated from::

            job: v1.0/schemadef-job.json
            label: schemadef_req_wf_param
            output:
              output:
                checksum: sha1$f12e6cfe70f3253f70b0dbde17c692e7fb0f1e5e
                class: File
                location: output.txt
                size: 12
            tags:
            - schema_def
            - workflow
            tool: v1.0/schemadef-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test SchemaDefRequirement definition used in workflow parameter
""")

    def test_conformance_v1_0_param_evaluation_noexpr(self):
        """Test parameter evaluation, no support for JS expressions


        Generated from::

            job: v1.0/empty.json
            label: param_evaluation_noexpr
            output:
              t1:
                bar:
                  b az: 2
                  b"az: null
                  b'az: true
                  baz: zab1
                  buz:
                  - a
                  - b
                  - c
              t10: true
              t11: true
              t12: null
              t13: -zab1
              t14: -zab1
              t15: -zab1
              t16: -zab1
              t17: zab1 zab1
              t18: zab1 zab1
              t19: zab1 zab1
              t2:
                b az: 2
                b"az: null
                b'az: true
                baz: zab1
                buz:
                - a
                - b
                - c
              t20: zab1 zab1
              t21: 2 2
              t22: true true
              t23: true true
              t24: null null
              t25: b
              t26: b b
              t27: null
              t28: 3
              t3:
                b az: 2
                b"az: null
                b'az: true
                baz: zab1
                buz:
                - a
                - b
                - c
              t4:
                b az: 2
                b"az: null
                b'az: true
                baz: zab1
                buz:
                - a
                - b
                - c
              t5: zab1
              t6: zab1
              t7: zab1
              t8: zab1
              t9: 2
            tags:
            - required
            - command_line_tool
            tool: v1.0/params.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test parameter evaluation, no support for JS expressions
""")

    def test_conformance_v1_0_param_evaluation_expr(self):
        """Test parameter evaluation, with support for JS expressions


        Generated from::

            job: v1.0/empty.json
            label: param_evaluation_expr
            output:
              t1:
                bar:
                  b az: 2
                  b"az: null
                  b'az: true
                  baz: zab1
                  buz:
                  - a
                  - b
                  - c
              t10: true
              t11: true
              t12: null
              t13: -zab1
              t14: -zab1
              t15: -zab1
              t16: -zab1
              t17: zab1 zab1
              t18: zab1 zab1
              t19: zab1 zab1
              t2:
                b az: 2
                b"az: null
                b'az: true
                baz: zab1
                buz:
                - a
                - b
                - c
              t20: zab1 zab1
              t21: 2 2
              t22: true true
              t23: true true
              t24: null null
              t25: b
              t26: b b
              t27: null
              t28: 3
              t3:
                b az: 2
                b"az: null
                b'az: true
                baz: zab1
                buz:
                - a
                - b
                - c
              t4:
                b az: 2
                b"az: null
                b'az: true
                baz: zab1
                buz:
                - a
                - b
                - c
              t5: zab1
              t6: zab1
              t7: zab1
              t8: zab1
              t9: 2
            tags:
            - inline_javascript
            - command_line_tool
            tool: v1.0/params2.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test parameter evaluation, with support for JS expressions
""")

    def test_conformance_v1_0_metadata(self):
        """Test metadata

        Generated from::

            job: v1.0/cat-job.json
            label: metadata
            output: {}
            tags:
            - required
            tool: v1.0/metadata.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test metadata""")

    def test_conformance_v1_0_format_checking(self):
        """Test simple format checking.


        Generated from::

            job: v1.0/formattest-job.json
            label: format_checking
            output:
              output:
                checksum: sha1$97fe1b50b4582cebc7d853796ebd62e3e163aa3f
                class: File
                format: http://edamontology.org/format_2330
                location: output.txt
                size: 1111
            tags:
            - required
            - command_line_tool
            tool: v1.0/formattest.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test simple format checking.
""")

    def test_conformance_v1_0_format_checking_subclass(self):
        """Test format checking against ontology using subclassOf.


        Generated from::

            job: v1.0/formattest2-job.json
            label: format_checking_subclass
            output:
              output:
                checksum: sha1$971d88faeda85a796752ecf752b7e2e34f1337ce
                class: File
                format: http://edamontology.org/format_1929
                location: output.txt
                size: 12010
            tags:
            - required
            - command_line_tool
            tool: v1.0/formattest2.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test format checking against ontology using subclassOf.
""")

    def test_conformance_v1_0_format_checking_equivalentclass(self):
        """Test format checking against ontology using equivalentClass.


        Generated from::

            job: v1.0/formattest2-job.json
            label: format_checking_equivalentclass
            output:
              output:
                checksum: sha1$971d88faeda85a796752ecf752b7e2e34f1337ce
                class: File
                format: http://edamontology.org/format_1929
                location: output.txt
                size: 12010
            tags:
            - required
            - command_line_tool
            tool: v1.0/formattest3.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test format checking against ontology using equivalentClass.
""")

    def test_conformance_v1_0_output_secondaryfile_optional(self):
        """Test optional output file and optional secondaryFile on output.


        Generated from::

            job: v1.0/cat-job.json
            label: output_secondaryfile_optional
            output:
              optional_file: null
              output_file:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: output.txt
                size: 13
            tags:
            - docker
            - command_line_tool
            tool: v1.0/optional-output.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test optional output file and optional secondaryFile on output.
""")

    def test_conformance_v1_0_valuefrom_ignored_null(self):
        """Test that valueFrom is ignored when the parameter is null

        Generated from::

            job: v1.0/empty.json
            label: valuefrom_ignored_null
            output:
              out: '
            
                '
            tags:
            - inline_javascript
            - command_line_tool
            tool: v1.0/vf-concat.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that valueFrom is ignored when the parameter is null""")

    def test_conformance_v1_0_valuefrom_secondexpr_ignored(self):
        """Test that second expression in concatenated valueFrom is not ignored

        Generated from::

            job: v1.0/cat-job.json
            label: valuefrom_secondexpr_ignored
            output:
              out: 'a string
            
                '
            tags:
            - inline_javascript
            - command_line_tool
            tool: v1.0/vf-concat.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that second expression in concatenated valueFrom is not ignored""")

    def test_conformance_v1_0_valuefrom_wf_step(self):
        """Test valueFrom on workflow step.

        Generated from::

            job: v1.0/step-valuefrom-wf.json
            label: valuefrom_wf_step
            output:
              count_output: 16
            tags:
            - step_input
            - inline_javascript
            - workflow
            tool: v1.0/step-valuefrom-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test valueFrom on workflow step.""")

    def test_conformance_v1_0_valuefrom_wf_step_multiple(self):
        """Test valueFrom on workflow step with multiple sources

        Generated from::

            job: v1.0/step-valuefrom-job.json
            label: valuefrom_wf_step_multiple
            output:
              val: '3
            
                '
            tags:
            - step_input
            - inline_javascript
            - multiple_input
            - workflow
            tool: v1.0/step-valuefrom2-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test valueFrom on workflow step with multiple sources""")

    def test_conformance_v1_0_valuefrom_wf_step_other(self):
        """Test valueFrom on workflow step referencing other inputs

        Generated from::

            job: v1.0/step-valuefrom-job.json
            label: valuefrom_wf_step_other
            output:
              val: '3
            
                '
            tags:
            - step_input
            - inline_javascript
            - workflow
            tool: v1.0/step-valuefrom3-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test valueFrom on workflow step referencing other inputs""")

    def test_conformance_v1_0_record_output_binding(self):
        """Test record type output binding.

        Generated from::

            job: v1.0/record-output-job.json
            label: record_output_binding
            output:
              orec:
                obar:
                  checksum: sha1$aeb3d11bdf536511649129f4077d5cda6a324118
                  class: File
                  location: bar
                  size: 12010
                ofoo:
                  checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                  class: File
                  location: foo
                  size: 1111
            tags:
            - shell_command
            - command_line_tool
            tool: v1.0/record-output.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test record type output binding.""")

    def test_conformance_v1_0_docker_json_output_path(self):
        """Test support for reading cwl.output.json when running in a Docker container
and just 'path' is provided.


        Generated from::

            job: v1.0/empty.json
            label: docker_json_output_path
            output:
              foo:
                checksum: sha1$f1d2d2f924e986ac86fdf7b36c94bcdf32beec15
                class: File
                location: foo
                size: 4
            tags:
            - shell_command
            - command_line_tool
            tool: v1.0/test-cwl-out.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test support for reading cwl.output.json when running in a Docker container
and just 'path' is provided.
""")

    def test_conformance_v1_0_docker_json_output_location(self):
        """Test support for reading cwl.output.json when running in a Docker container
and just 'location' is provided.


        Generated from::

            job: v1.0/empty.json
            label: docker_json_output_location
            output:
              foo:
                checksum: sha1$f1d2d2f924e986ac86fdf7b36c94bcdf32beec15
                class: File
                location: foo
                size: 4
            tags:
            - shell_command
            - command_line_tool
            tool: v1.0/test-cwl-out2.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test support for reading cwl.output.json when running in a Docker container
and just 'location' is provided.
""")

    def test_conformance_v1_0_multiple_glob_expr_list(self):
        """Test support for returning multiple glob patterns from expression

        Generated from::

            job: v1.0/abc.json
            label: multiple_glob_expr_list
            output:
              files:
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: a
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: b
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: c
                size: 0
            tags:
            - required
            - command_line_tool
            tool: v1.0/glob-expr-list.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test support for returning multiple glob patterns from expression""")

    def test_conformance_v1_0_wf_scatter_oneparam_valuefrom(self):
        """Test workflow scatter with single scatter parameter and two valueFrom on step input (first and current el)

        Generated from::

            job: v1.0/scatter-valuefrom-job1.json
            label: wf_scatter_oneparam_valuefrom
            output:
              out:
              - foo one one
              - foo one two
              - foo one three
              - foo one four
            tags:
            - scatter
            - step_input
            - workflow
            tool: v1.0/scatter-valuefrom-wf1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with single scatter parameter and two valueFrom on step input (first and current el)""")

    def test_conformance_v1_0_wf_scatter_twoparam_nested_crossproduct_valuefrom(self):
        """Test workflow scatter with two scatter parameters and nested_crossproduct join method and valueFrom on step input

        Generated from::

            job: v1.0/scatter-valuefrom-job2.json
            label: wf_scatter_twoparam_nested_crossproduct_valuefrom
            output:
              out:
              - - foo one one three
                - foo one one four
              - - foo one two three
                - foo one two four
            tags:
            - scatter
            - step_input
            - workflow
            tool: v1.0/scatter-valuefrom-wf2.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with two scatter parameters and nested_crossproduct join method and valueFrom on step input""")

    def test_conformance_v1_0_wf_scatter_twoparam_flat_crossproduct_valuefrom(self):
        """Test workflow scatter with two scatter parameters and flat_crossproduct join method and valueFrom on step input

        Generated from::

            job: v1.0/scatter-valuefrom-job2.json
            label: wf_scatter_twoparam_flat_crossproduct_valuefrom
            output:
              out:
              - foo one one three
              - foo one one four
              - foo one two three
              - foo one two four
            tags:
            - scatter
            - step_input
            - workflow
            tool: v1.0/scatter-valuefrom-wf3.cwl#main
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with two scatter parameters and flat_crossproduct join method and valueFrom on step input""")

    def test_conformance_v1_0_wf_scatter_twoparam_dotproduct_valuefrom(self):
        """Test workflow scatter with two scatter parameters and dotproduct join method and valueFrom on step input

        Generated from::

            job: v1.0/scatter-valuefrom-job2.json
            label: wf_scatter_twoparam_dotproduct_valuefrom
            output:
              out:
              - foo one one three
              - foo one two four
            tags:
            - scatter
            - step_input
            - workflow
            tool: v1.0/scatter-valuefrom-wf4.cwl#main
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with two scatter parameters and dotproduct join method and valueFrom on step input""")

    def test_conformance_v1_0_wf_scatter_oneparam_valuefrom_twice_current_el(self):
        """Test workflow scatter with single scatter parameter and two valueFrom on step input (current el twice)

        Generated from::

            job: v1.0/scatter-valuefrom-job1.json
            label: wf_scatter_oneparam_valuefrom_twice_current_el
            output:
              out:
              - foo one one
              - foo two two
              - foo three three
              - foo four four
            tags:
            - scatter
            - step_input
            - workflow
            tool: v1.0/scatter-valuefrom-wf5.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow scatter with single scatter parameter and two valueFrom on step input (current el twice)""")

    def test_conformance_v1_0_wf_scatter_oneparam_valueFrom(self):
        """Test valueFrom eval on scattered input parameter

        Generated from::

            job: v1.0/scatter-valuefrom-job3.json
            label: wf_scatter_oneparam_valueFrom
            output:
              out_message:
              - checksum: sha1$98030575f6fc40e5021be5a8803a6bef94aee11f
                class: File
                location: Any
                size: 16
              - checksum: sha1$edcacd50778d98ae113015406b3195c165059dd8
                class: File
                location: Any
                size: 16
            tags:
            - scatter
            - step_input
            - workflow
            tool: v1.0/scatter-valuefrom-wf6.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test valueFrom eval on scattered input parameter""")

    def test_conformance_v1_0_wf_two_inputfiles_namecollision(self):
        """Test workflow two input files with same name.

        Generated from::

            job: v1.0/conflict-job.json
            label: wf_two_inputfiles_namecollision
            output:
              fileout:
                checksum: sha1$a2d8d6e7b28295dc9977dc3bdb652ddd480995f0
                class: File
                location: out.txt
                size: 25
            tags:
            - required
            - workflow
            tool: v1.0/conflict-wf.cwl#collision
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test workflow two input files with same name.""")

    def test_conformance_v1_0_directory_input_param_ref(self):
        """Test directory input with parameter reference

        Generated from::

            job: v1.0/dir-job.yml
            label: directory_input_param_ref
            output:
              outlist:
                checksum: sha1$13cda8661796ae241da3a18668fb552161a72592
                class: File
                location: output.txt
                size: 20
            tags:
            - shell_command
            - command_line_tool
            tool: v1.0/dir.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test directory input with parameter reference""")

    def test_conformance_v1_0_directory_input_docker(self):
        """Test directory input in Docker

        Generated from::

            job: v1.0/dir-job.yml
            label: directory_input_docker
            output:
              outlist:
                checksum: sha1$13cda8661796ae241da3a18668fb552161a72592
                class: File
                location: output.txt
                size: 20
            tags:
            - required
            - command_line_tool
            tool: v1.0/dir2.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test directory input in Docker""")

    def test_conformance_v1_0_directory_output(self):
        """Test directory output

        Generated from::

            job: v1.0/dir3-job.yml
            label: directory_output
            output:
              outdir:
                class: Directory
                listing:
                - checksum: sha1$dd0a4c4c49ba43004d6611771972b6cf969c1c01
                  class: File
                  location: goodbye.txt
                  size: 24
                - checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                  class: File
                  location: hello.txt
                  size: 13
            tags:
            - required
            - command_line_tool
            tool: v1.0/dir3.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test directory output""")

    def test_conformance_v1_0_directory_secondaryfiles(self):
        """Test directories in secondaryFiles

        Generated from::

            job: v1.0/dir4-job.yml
            label: directory_secondaryfiles
            output:
              outlist:
                checksum: sha1$13cda8661796ae241da3a18668fb552161a72592
                class: File
                location: output.txt
                size: 20
            tags:
            - shell_command
            - command_line_tool
            tool: v1.0/dir4.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test directories in secondaryFiles""")

    def test_conformance_v1_0_87(self):
        """Test specifying secondaryFiles in subdirectories of the job input document.

        Generated from::

            job: v1.0/dir4-subdir-1-job.yml
            output:
              outlist:
                checksum: sha1$9d9bc8f5252d39274b5dfbac64216c6e888f5dfc
                class: File
                location: output.txt
                size: 14
            tool: v1.0/dir4.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test specifying secondaryFiles in subdirectories of the job input document.""")

    def test_conformance_v1_0_88(self):
        """Test specifying secondaryFiles in same subdirectory of the job input as the primary input file.

        Generated from::

            job: v1.0/dir4-subdir-2-job.yml
            output:
              outlist:
                checksum: sha1$9d9bc8f5252d39274b5dfbac64216c6e888f5dfc
                class: File
                location: output.txt
                size: 14
            tool: v1.0/dir4.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test specifying secondaryFiles in same subdirectory of the job input as the primary input file.""")

    def test_conformance_v1_0_dynamic_initial_workdir(self):
        """Test dynamic initial work dir

        Generated from::

            job: v1.0/dir-job.yml
            label: dynamic_initial_workdir
            output:
              outlist:
                checksum: sha1$13cda8661796ae241da3a18668fb552161a72592
                class: File
                location: output.txt
                size: 20
            tags:
            - shell_command
            - initial_work_dir
            - command_line_tool
            tool: v1.0/dir5.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test dynamic initial work dir""")

    def test_conformance_v1_0_writable_stagedfiles(self):
        """Test writable staged files.

        Generated from::

            job: v1.0/stagefile-job.yml
            label: writable_stagedfiles
            output:
              outfile:
                checksum: sha1$b769c7b2e316edd4b5eb2d24799b2c1f9d8c86e6
                class: File
                location: bob.txt
                size: 1111
            tags:
            - initial_work_dir
            - command_line_tool
            tool: v1.0/stagefile.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test writable staged files.""")

    def test_conformance_v1_0_input_file_literal(self):
        """Test file literal as input

        Generated from::

            job: v1.0/file-literal.yml
            label: input_file_literal
            output:
              output_file:
                checksum: sha1$d0e04ff6c413c7d57f9a0ca0a33cd3ab52e2dd9c
                class: File
                location: output.txt
                size: 18
            tags:
            - required
            - command_line_tool
            tool: v1.0/cat3-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test file literal as input""")

    def test_conformance_v1_0_initial_workdir_expr(self):
        """Test expression in InitialWorkDir listing

        Generated from::

            job: v1.0/arguments-job.yml
            label: initial_workdir_expr
            output:
              classfile:
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: Hello.class
                size: 0
            tags:
            - initial_work_dir
            - command_line_tool
            tool: v1.0/linkfile.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test expression in InitialWorkDir listing""")

    def test_conformance_v1_0_nameroot_nameext_stdout_expr(self):
        """Test nameroot/nameext expression in arguments, stdout

        Generated from::

            job: v1.0/wc-job.json
            label: nameroot_nameext_stdout_expr
            output:
              b:
                checksum: sha1$c4cfd130e7578714e3eef91c1d6d90e0e0b9db3e
                class: File
                location: whale.xtx
                size: 21
            tags:
            - required
            - command_line_tool
            tool: v1.0/nameroot.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test nameroot/nameext expression in arguments, stdout""")

    def test_conformance_v1_0_input_dir_inputbinding(self):
        """Test directory input with inputBinding

        Generated from::

            job: v1.0/dir-job.yml
            label: input_dir_inputbinding
            output:
              outlist:
                checksum: sha1$13cda8661796ae241da3a18668fb552161a72592
                class: File
                location: output.txt
                size: 20
            tags:
            - shell_command
            - command_line_tool
            tool: v1.0/dir6.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test directory input with inputBinding""")

    def test_conformance_v1_0_cl_gen_arrayofarrays(self):
        """Test command line generation of array-of-arrays

        Generated from::

            job: v1.0/nested-array-job.yml
            label: cl_gen_arrayofarrays
            output:
              echo:
                checksum: sha1$3f786850e387550fdab836ed7e6dc881de23001b
                class: File
                location: echo.txt
                size: 2
            tags:
            - required
            - command_line_tool
            tool: v1.0/nested-array.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test command line generation of array-of-arrays""")

    def test_conformance_v1_0_env_home_tmpdir(self):
        """Test $HOME and $TMPDIR are set correctly

        Generated from::

            job: v1.0/empty.json
            label: env_home_tmpdir
            output: {}
            tags:
            - shell_command
            - command_line_tool
            tool: v1.0/envvar.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test $HOME and $TMPDIR are set correctly""")

    def test_conformance_v1_0_env_home_tmpdir_docker(self):
        """Test $HOME and $TMPDIR are set correctly in Docker

        Generated from::

            job: v1.0/empty.json
            label: env_home_tmpdir_docker
            output: {}
            tags:
            - shell_command
            - command_line_tool
            tool: v1.0/envvar2.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test $HOME and $TMPDIR are set correctly in Docker""")

    def test_conformance_v1_0_expressionlib_tool_wf_override(self):
        """Test that expressionLib requirement of individual tool step overrides expressionLib of workflow.

        Generated from::

            job: v1.0/empty.json
            label: expressionlib_tool_wf_override
            output:
              out:
                checksum: sha1$7448d8798a4380162d4b56f9b452e2f6f9e24e7a
                class: File
                location: whatever.txt
                size: 2
            tags:
            - inline_javascript
            - workflow
            tool: v1.0/js-expr-req-wf.cwl#wf
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that expressionLib requirement of individual tool step overrides expressionLib of workflow.""")

    def test_conformance_v1_0_initial_workdir_output(self):
        """Test output of InitialWorkDir

        Generated from::

            job: v1.0/initialworkdirrequirement-docker-out-job.json
            label: initial_workdir_output
            output:
              OUTPUT:
                checksum: sha1$aeb3d11bdf536511649129f4077d5cda6a324118
                class: File
                location: ref.fasta
                secondaryFiles:
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: ref.fasta.fai
                  size: 0
                size: 12010
            tags:
            - docker
            - initial_work_dir
            - command_line_tool
            tool: v1.0/initialworkdirrequirement-docker-out.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test output of InitialWorkDir""")

    def test_conformance_v1_0_embedded_subworkflow(self):
        """Test embedded subworkflow

        Generated from::

            job: v1.0/wc-job.json
            label: embedded_subworkflow
            output:
              count_output: 16
            tags:
            - subworkflow
            - workflow
            tool: v1.0/count-lines10-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test embedded subworkflow""")

    def test_conformance_v1_0_filesarray_secondaryfiles(self):
        """Test secondaryFiles on array of files.

        Generated from::

            job: v1.0/docker-array-secondaryfiles-job.json
            label: filesarray_secondaryfiles
            output:
              bai_list:
                checksum: sha1$081fc0e57d6efa5f75eeb237aab1d04031132be6
                class: File
                location: fai.list
                size: 386
            tags:
            - docker
            - inline_javascript
            - shell_command
            - command_line_tool
            tool: v1.0/docker-array-secondaryfiles.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test secondaryFiles on array of files.""")

    def test_conformance_v1_0_exprtool_directory_literal(self):
        """Test directory literal output created by ExpressionTool

        Generated from::

            job: v1.0/dir7.yml
            label: exprtool_directory_literal
            output:
              dir:
                class: Directory
                listing:
                - checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                  class: File
                  location: whale.txt
                  size: 1111
                - checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                  class: File
                  location: hello.txt
                  size: 13
                location: a_directory
            tags:
            - inline_javascript
            - expression_tool
            tool: v1.0/dir7.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test directory literal output created by ExpressionTool""")

    def test_conformance_v1_0_exprtool_file_literal(self):
        """Test file literal output created by ExpressionTool

        Generated from::

            job: v1.0/empty.json
            label: exprtool_file_literal
            output:
              lit:
                checksum: sha1$fea23663b9c8ed71968f86415b5ec091bb111448
                class: File
                location: a_file
                size: 19
            tags:
            - inline_javascript
            - expression_tool
            tool: v1.0/file-literal-ex.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test file literal output created by ExpressionTool""")

    def test_conformance_v1_0_dockeroutputdir(self):
        """Test dockerOutputDirectory

        Generated from::

            job: v1.0/empty.json
            label: dockeroutputdir
            output:
              thing:
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: thing
                size: 0
            tags:
            - docker
            - command_line_tool
            tool: v1.0/docker-output-dir.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test dockerOutputDirectory""")

    def test_conformance_v1_0_hints_import(self):
        """Test hints with $import

        Generated from::

            job: v1.0/empty.json
            label: hints_import
            output:
              out:
                checksum: sha1$b3ec4ed1749c207e52b3a6d08c59f31d83bff519
                class: File
                location: out
                size: 15
            tags:
            - required
            - command_line_tool
            tool: v1.0/imported-hint.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test hints with $import""")

    def test_conformance_v1_0_default_path_notfound_warning(self):
        """Test warning instead of error when default path is not found

        Generated from::

            job: v1.0/default_path_job.yml
            label: default_path_notfound_warning
            output: {}
            tags:
            - required
            - command_line_tool
            tool: v1.0/default_path.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test warning instead of error when default path is not found""")

    def test_conformance_v1_0_inlinejs_req_expressions(self):
        """Test InlineJavascriptRequirement with multiple expressions in the same tool

        Generated from::

            job: v1.0/empty.json
            label: inlinejs_req_expressions
            output:
              args:
              - -A
              - '2'
              - -B
              - baz
              - -C
              - '10'
              - '9'
              - '8'
              - '7'
              - '6'
              - '5'
              - '4'
              - '3'
              - '2'
              - '1'
              - -D
            tags:
            - inline_javascript
            - command_line_tool
            tool: v1.0/inline-js.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test InlineJavascriptRequirement with multiple expressions in the same tool""")

    def test_conformance_v1_0_input_dir_recurs_copy_writable(self):
        """Test if a writable input directory is recursively copied and writable

        Generated from::

            job: v1.0/recursive-input-directory.yml
            label: input_dir_recurs_copy_writable
            output:
              output_dir:
                basename: work_dir
                class: Directory
                listing:
                - basename: a
                  checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: work_dir/a
                  size: 0
                - basename: b
                  checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: work_dir/b
                  size: 0
                - basename: c
                  class: Directory
                  listing:
                  - basename: d
                    checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                    class: File
                    location: work_dir/c/d
                    size: 0
                  location: work_dir/c
                - basename: e
                  checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: work_dir/e
                  size: 0
                location: work_dir
              test_result:
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: output.txt
                size: 0
            tags:
            - initial_work_dir
            - shell_command
            - command_line_tool
            tool: v1.0/recursive-input-directory.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test if a writable input directory is recursively copied and writable""")

    def test_conformance_v1_0_null_missing_params(self):
        """Test that missing parameters are null (not undefined) in expression

        Generated from::

            job: v1.0/empty.json
            label: null_missing_params
            output:
              out: 't
            
                '
            tags:
            - inline_javascript
            - command_line_tool
            tool: v1.0/null-defined.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that missing parameters are null (not undefined) in expression""")

    def test_conformance_v1_0_param_notnull_expr(self):
        """Test that provided parameter is not null in expression

        Generated from::

            job: v1.0/cat-job.json
            label: param_notnull_expr
            output:
              out: 'f
            
                '
            tags:
            - inline_javascript
            - command_line_tool
            tool: v1.0/null-defined.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that provided parameter is not null in expression""")

    def test_conformance_v1_0_wf_compound_doc(self):
        """Test compound workflow document

        Generated from::

            job: v1.0/revsort-job.json
            label: wf_compound_doc
            output:
              output:
                checksum: sha1$b9214658cc453331b62c2282b772a5c063dbd284
                class: File
                location: output.txt
                size: 1111
            tags:
            - required
            - workflow
            tool: v1.0/revsort-packed.cwl#main
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test compound workflow document""")

    def test_conformance_v1_0_nameroot_nameext_generated(self):
        """Test that nameroot and nameext are generated from basename at execution time by the runner

        Generated from::

            job: v1.0/basename-fields-job.yml
            label: nameroot_nameext_generated
            output:
              extFile:
                checksum: sha1$301a72c82a835e1737caf30f94d0eec210c4d9f1
                class: File
                location: Any
                path: Any
                size: 5
              rootFile:
                checksum: sha1$b4a583c391e234cf210e1d576f68f674c8ad7ecd
                class: File
                location: Any
                path: Any
                size: 10
            tags:
            - step_input_expression
            - workflow
            tool: v1.0/basename-fields-test.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that nameroot and nameext are generated from basename at execution time by the runner""")

    def test_conformance_v1_0_initialworkpath_output(self):
        """Test that file path in $(inputs) for initialworkdir is in $(outdir).

        Generated from::

            job: v1.0/wc-job.json
            label: initialworkpath_output
            output: {}
            tags:
            - initial_work_dir
            - command_line_tool
            tool: v1.0/initialwork-path.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that file path in $(inputs) for initialworkdir is in $(outdir).""")

    def test_conformance_v1_0_wf_scatter_twopar_oneinput_flattenedmerge(self):
        """Test single step workflow with Scatter step and two data links connected to
same input, flattened merge behavior. Workflow inputs are set as list


        Generated from::

            job: v1.0/count-lines6-job.json
            label: wf_scatter_twopar_oneinput_flattenedmerge
            output:
              count_output: 34
            tags:
            - multiple_input
            - inline_javascript
            - workflow
            tool: v1.0/count-lines12-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test single step workflow with Scatter step and two data links connected to
same input, flattened merge behavior. Workflow inputs are set as list
""")

    def test_conformance_v1_0_wf_multiplesources_multipletypes(self):
        """Test step input with multiple sources with multiple types

        Generated from::

            job: v1.0/sum-job.json
            label: wf_multiplesources_multipletypes
            output:
              result: 12
            tags:
            - step_input
            - inline_javascript
            - multiple_input
            - workflow
            tool: v1.0/sum-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test step input with multiple sources with multiple types""")

    def test_conformance_v1_0_shelldir_notinterpreted(self):
        """Test that shell directives are not interpreted.

        Generated from::

            job: v1.0/empty.json
            label: shelldir_notinterpreted
            output:
              stderr_file:
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: Any
                size: 0
              stdout_file:
                checksum: sha1$1555252d52d4ec3262538a4426a83a99cfff4402
                class: File
                location: Any
                size: 9
            tags:
            - required
            - command_line_tool
            tool: v1.0/shellchar.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that shell directives are not interpreted.""")

    def test_conformance_v1_0_shelldir_quoted(self):
        """Test that shell directives are quoted.

        Generated from::

            job: v1.0/empty.json
            label: shelldir_quoted
            output:
              stderr_file:
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: Any
                size: 0
              stdout_file:
                checksum: sha1$1555252d52d4ec3262538a4426a83a99cfff4402
                class: File
                location: Any
                size: 9
            tags:
            - shell_command
            - command_line_tool
            tool: v1.0/shellchar2.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that shell directives are quoted.""")

    def test_conformance_v1_0_initial_workdir_empty_writable(self):
        """Test empty writable dir with InitialWorkDirRequirement

        Generated from::

            job: v1.0/empty.json
            label: initial_workdir_empty_writable
            output:
              out:
                basename: emptyWritableDir
                class: Directory
                listing:
                - basename: blurg
                  checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: blurg
                  size: 0
                location: emptyWritableDir
            tags:
            - inline_javascript
            - initial_work_dir
            - command_line_tool
            tool: v1.0/writable-dir.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test empty writable dir with InitialWorkDirRequirement""")

    def test_conformance_v1_0_initial_workdir_empty_writable_docker(self):
        """Test empty writable dir with InitialWorkDirRequirement inside Docker

        Generated from::

            job: v1.0/empty.json
            label: initial_workdir_empty_writable_docker
            output:
              out:
                basename: emptyWritableDir
                class: Directory
                listing:
                - basename: blurg
                  checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: blurg
                  size: 0
                location: emptyWritableDir
            tags:
            - inline_javascript
            - initial_work_dir
            - command_line_tool
            tool: v1.0/writable-dir-docker.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test empty writable dir with InitialWorkDirRequirement inside Docker""")

    def test_conformance_v1_0_dynamic_resreq_inputs(self):
        """Test dynamic resource reqs referencing inputs

        Generated from::

            job: v1.0/dynresreq-job.yaml
            label: dynamic_resreq_inputs
            output:
              output:
                checksum: sha1$7448d8798a4380162d4b56f9b452e2f6f9e24e7a
                class: File
                location: cores.txt
                size: 2
            tags:
            - resource
            - command_line_tool
            tool: v1.0/dynresreq.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test dynamic resource reqs referencing inputs""")

    def test_conformance_v1_0_fileliteral_input_docker(self):
        """Test file literal as input without Docker

        Generated from::

            job: v1.0/file-literal.yml
            label: fileliteral_input_docker
            output:
              output_file:
                checksum: sha1$d0e04ff6c413c7d57f9a0ca0a33cd3ab52e2dd9c
                class: File
                location: output.txt
                size: 18
            tags:
            - required
            - command_line_tool
            tool: v1.0/cat3-nodocker.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test file literal as input without Docker""")

    def test_conformance_v1_0_outputbinding_glob_sorted(self):
        """Test that OutputBinding.glob is sorted as specified by POSIX

        Generated from::

            job: v1.0/empty.json
            label: outputbinding_glob_sorted
            output:
              letters:
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: a
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: b
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: c
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: w
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: x
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: y
                size: 0
              - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: z
                size: 0
            tags:
            - required
            - command_line_tool
            tool: v1.0/glob_test.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that OutputBinding.glob is sorted as specified by POSIX""")

    def test_conformance_v1_0_initialworkdir_nesteddir(self):
        """Test InitialWorkDirRequirement with a nested directory structure from another step

        Generated from::

            job: v1.0/empty.json
            label: initialworkdir_nesteddir
            output:
              ya_empty:
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: ya
                size: 0
            tags:
            - initial_work_dir
            - workflow
            tool: v1.0/iwdr_with_nested_dirs.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test InitialWorkDirRequirement with a nested directory structure from another step""")

    def test_conformance_v1_0_booleanflags_cl_noinputbinding(self):
        """Test that boolean flags do not appear on command line if inputBinding is empty and not null

        Generated from::

            job: v1.0/bool-empty-inputbinding-job.json
            label: booleanflags_cl_noinputbinding
            output:
              args: []
            tags:
            - required
            - command_line_tool
            tool: v1.0/bool-empty-inputbinding.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that boolean flags do not appear on command line if inputBinding is empty and not null""")

    def test_conformance_v1_0_expr_reference_self_noinput(self):
        """Test that expression engine does not fail to evaluate reference to self with unprovided input

        Generated from::

            job: v1.0/empty.json
            label: expr_reference_self_noinput
            output:
              args: []
            tags:
            - required
            - command_line_tool
            tool: v1.0/stage-unprovided-file.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that expression engine does not fail to evaluate reference to self with unprovided input""")

    def test_conformance_v1_0_success_codes(self):
        """Test successCodes

        Generated from::

            job: v1.0/empty.json
            label: success_codes
            output: {}
            tags:
            - required
            - command_line_tool
            tool: v1.0/exit-success.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test successCodes""")

    def test_conformance_v1_0_dynamic_resreq_wf(self):
        """Test simple workflow with a dynamic resource requirement

        Generated from::

            job: v1.0/dynresreq-job.yaml
            label: dynamic_resreq_wf
            output:
              cores:
                checksum: sha1$7448d8798a4380162d4b56f9b452e2f6f9e24e7a
                class: File
                location: output
                size: 2
            tags:
            - resource
            - workflow
            tool: v1.0/dynresreq-workflow.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test simple workflow with a dynamic resource requirement""")

    def test_conformance_v1_0_cl_empty_array_input(self):
        """Test that empty array input does not add anything to command line

        Generated from::

            job: v1.0/empty-array-job.json
            label: cl_empty_array_input
            output:
              args: []
            tags:
            - required
            - command_line_tool
            tool: v1.0/empty-array-input.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that empty array input does not add anything to command line""")

    def test_conformance_v1_0_resreq_step_overrides_wf(self):
        """Test that ResourceRequirement on a step level redefines requirement on the workflow level

        Generated from::

            job: v1.0/empty.json
            label: resreq_step_overrides_wf
            output:
              out:
                checksum: sha1$e5fa44f2b31c1fb553b6021e7360d07d5d91ff5e
                class: File
                location: cores.txt
                size: 2
            tags:
            - resource
            - workflow
            tool: v1.0/steplevel-resreq.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that ResourceRequirement on a step level redefines requirement on the workflow level""")

    def test_conformance_v1_0_valuefrom_constant_overrides_inputs(self):
        """Test valueFrom with constant value overriding provided array inputs

        Generated from::

            job: v1.0/array-of-strings-job.yml
            label: valuefrom_constant_overrides_inputs
            output:
              args:
              - replacementValue
            tags:
            - required
            - command_line_tool
            tool: v1.0/valueFrom-constant.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test valueFrom with constant value overriding provided array inputs""")

    def test_conformance_v1_0_dynamic_resreq_filesizes(self):
        """Test dynamic resource reqs referencing the size of Files inside a Directory

        Generated from::

            job: v1.0/dynresreq-dir-job.yaml
            label: dynamic_resreq_filesizes
            output:
              output:
                checksum: sha1$7448d8798a4380162d4b56f9b452e2f6f9e24e7a
                class: File
                location: cores.txt
                size: 2
            tags:
            - resource
            - command_line_tool
            tool: v1.0/dynresreq-dir.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test dynamic resource reqs referencing the size of Files inside a Directory""")

    def test_conformance_v1_0_wf_step_connect_undeclared_param(self):
        """Test that it is not an error to connect a parameter to a workflow
step, even if the parameter doesn't appear in the `run` process
inputs.


        Generated from::

            job: v1.0/empty.json
            label: wf_step_connect_undeclared_param
            output:
              out: 'hello inp1
            
                '
            tags:
            - required
            - workflow
            tool: v1.0/pass-unconnected.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that it is not an error to connect a parameter to a workflow
step, even if the parameter doesn't appear in the `run` process
inputs.
""")

    def test_conformance_v1_0_wf_step_access_undeclared_param(self):
        """Test that parameters that don't appear in the `run` process
inputs are not present in the input object used to run the tool.


        Generated from::

            job: v1.0/empty.json
            label: wf_step_access_undeclared_param
            should_fail: true
            tags:
            - required
            - workflow
            tool: v1.0/fail-unconnected.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test that parameters that don't appear in the `run` process
inputs are not present in the input object used to run the tool.
""")

    def test_conformance_v1_0_wf_scatter_embedded_subwf(self):
        """Test simple scatter over an embedded subworkflow

        Generated from::

            job: v1.0/count-lines3-job.json
            label: wf_scatter_embedded_subwf
            output:
              count_output:
              - 16
              - 1
            tool: v1.0/count-lines13-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test simple scatter over an embedded subworkflow""")

    def test_conformance_v1_0_wf_multiple_param_embedded_subwf(self):
        """Test simple multiple input scatter over an embedded subworkflow

        Generated from::

            job: v1.0/count-lines4-job.json
            label: wf_multiple_param_embedded_subwf
            output:
              count_output:
              - 16
              - 1
            tool: v1.0/count-lines14-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test simple multiple input scatter over an embedded subworkflow""")

    def test_conformance_v1_0_wf_double_nested_subwf(self):
        """Test twice nested subworkflow

        Generated from::

            job: v1.0/wc-job.json
            label: wf_double_nested_subwf
            output:
              count_output: 16
            tool: v1.0/count-lines15-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test twice nested subworkflow""")

    def test_conformance_v1_0_wf_subwf_tool_then_wf(self):
        """Test subworkflow of mixed depth with tool first

        Generated from::

            job: v1.0/wc-job.json
            label: wf_subwf_tool_then_wf
            output:
              count_output: 16
            tool: v1.0/count-lines16-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test subworkflow of mixed depth with tool first""")

    def test_conformance_v1_0_wf_subwf_wf_then_tool(self):
        """Test subworkflow of mixed depth with tool after

        Generated from::

            job: v1.0/wc-job.json
            label: wf_subwf_wf_then_tool
            output:
              count_output: 16
            tool: v1.0/count-lines17-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test subworkflow of mixed depth with tool after""")

    def test_conformance_v1_0_wf_output_record(self):
        """Test record type inputs to and outputs from workflows.

        Generated from::

            job: v1.0/record-output-job.json
            label: wf_output_record
            output:
              orec:
                obar:
                  checksum: sha1$aeb3d11bdf536511649129f4077d5cda6a324118
                  class: File
                  location: bar
                  size: 12010
                ofoo:
                  checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                  class: File
                  location: foo
                  size: 1111
            tool: v1.0/record-output-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test record type inputs to and outputs from workflows.""")

    def test_conformance_v1_0_wf_input_output_int(self):
        """Test integer workflow input and outputs

        Generated from::

            job: v1.0/io-int.json
            label: wf_input_output_int
            output:
              o: 10
            tool: v1.0/io-int-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test integer workflow input and outputs""")

    def test_conformance_v1_0_wf_input_int_opt_spec(self):
        """Test optional integer workflow inputs (specified)

        Generated from::

            job: v1.0/io-int.json
            label: wf_input_int_opt_spec
            output:
              o: 10
            tool: v1.0/io-int-optional-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test optional integer workflow inputs (specified)""")

    def test_conformance_v1_0_wf_input_int_opt_unspec(self):
        """Test optional integer workflow inputs (unspecified)

        Generated from::

            job: v1.0/empty.json
            label: wf_input_int_opt_unspec
            output:
              o: 4
            tool: v1.0/io-int-optional-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test optional integer workflow inputs (unspecified)""")

    def test_conformance_v1_0_wf_input_int_default_spec(self):
        """Test default integer workflow inputs (specified)

        Generated from::

            job: v1.0/io-int.json
            label: wf_input_int_default_spec
            output:
              o: 10
            tool: v1.0/io-int-default-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test default integer workflow inputs (specified)""")

    def test_conformance_v1_0_wf_input_int_default_unspec(self):
        """Test default integer workflow inputs (unspecified)

        Generated from::

            job: v1.0/empty.json
            label: wf_input_int_default_unspec
            output:
              o: 8
            tool: v1.0/io-int-default-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test default integer workflow inputs (unspecified)""")

    def test_conformance_v1_0_wf_input_int_default_tool_wf_unspec(self):
        """Test default integer tool and workflow inputs (unspecified)

        Generated from::

            job: v1.0/empty.json
            label: wf_input_int_default_tool_wf_unspec
            output:
              o: 13
            tool: v1.0/io-int-default-tool-and-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test default integer tool and workflow inputs (unspecified)""")

    def test_conformance_v1_0_wf_input_file_default_unspec(self):
        """Test File input with default unspecified to workflow

        Generated from::

            job: v1.0/empty.json
            label: wf_input_file_default_unspec
            output:
              o:
                basename: output
                checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                class: File
                location: Any
                size: 1111
            tool: v1.0/io-file-default-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test File input with default unspecified to workflow""")

    def test_conformance_v1_0_wf_input_file_default_spec(self):
        """Test File input with default specified to workflow

        Generated from::

            job: v1.0/default_path_job.yml
            label: wf_input_file_default_spec
            output:
              o:
                basename: output
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: Any
                size: 13
            tool: v1.0/io-file-default-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test File input with default specified to workflow""")

    def test_conformance_v1_0_wf_input_union_file_filearray_onefilearray(self):
        """Test input union type or File or File array to a tool with one file in array specified.

        Generated from::

            job: v1.0/job-input-array-one-empty-file.json
            label: wf_input_union_file_filearray_onefilearray
            output:
              output_file:
                basename: output.txt
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: Any
                size: 0
            tool: v1.0/io-file-or-files.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test input union type or File or File array to a tool with one file in array specified.""")

    def test_conformance_v1_0_wf_input_union_file_filearray_fewfilesarray(self):
        """Test input union type or File or File array to a tool with a few files in array specified.

        Generated from::

            job: v1.0/job-input-array-few-files.json
            label: wf_input_union_file_filearray_fewfilesarray
            output:
              output_file:
                basename: output.txt
                checksum: sha1$6d1723861ad5a1260f1c3c07c93076c5a215f646
                class: File
                location: Any
                size: 1114
            tool: v1.0/io-file-or-files.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test input union type or File or File array to a tool with a few files in array specified.""")

    def test_conformance_v1_0_wf_input_union_file_filearray_onefile(self):
        """Test input union type or File or File array to a tool with one file specified.

        Generated from::

            job: v1.0/job-input-one-file.json
            label: wf_input_union_file_filearray_onefile
            output:
              output_file:
                basename: output.txt
                checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                class: File
                location: Any
                size: 1111
            tool: v1.0/io-file-or-files.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test input union type or File or File array to a tool with one file specified.""")

    def test_conformance_v1_0_wf_input_union_file_filearray_null(self):
        """Test input union type or File or File array to a tool with null specified.

        Generated from::

            job: v1.0/job-input-null.json
            label: wf_input_union_file_filearray_null
            output:
              output_file:
                basename: output.txt
                checksum: sha1$503458abf7614be3fb26d85ff5d8f3e17aa0a552
                class: File
                location: Any
                size: 10
            tool: v1.0/io-file-or-files.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test input union type or File or File array to a tool with null specified.""")

    def test_conformance_v1_0_wf_input_any_integer_tool(self):
        """Test Any parameter with integer input to a tool

        Generated from::

            job: v1.0/io-any-int.json
            label: wf_input_any_integer_tool
            output:
              t1: 7
            tool: v1.0/io-any-1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test Any parameter with integer input to a tool""")

    def test_conformance_v1_0_wf_input_any_string_tool(self):
        """Test Any parameter with string input to a tool

        Generated from::

            job: v1.0/io-any-string.json
            label: wf_input_any_string_tool
            output:
              t1: '7'
            tool: v1.0/io-any-1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test Any parameter with string input to a tool""")

    def test_conformance_v1_0_wf_input_any_file_tool(self):
        """Test Any parameter with file input to a tool

        Generated from::

            job: v1.0/io-any-file.json
            label: wf_input_any_file_tool
            output:
              t1: File
            tool: v1.0/io-any-1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test Any parameter with file input to a tool""")

    def test_conformance_v1_0_wf_input_any_array_tool(self):
        """Test Any parameter with array input to a tool

        Generated from::

            job: v1.0/io-any-array.json
            label: wf_input_any_array_tool
            output:
              t1:
              - 1
              - moocow
            tool: v1.0/io-any-1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test Any parameter with array input to a tool""")

    def test_conformance_v1_0_wf_input_any_record_tool(self):
        """Test Any parameter with record input to a tool

        Generated from::

            job: v1.0/io-any-record.json
            label: wf_input_any_record_tool
            output:
              t1:
                cow: 5
                moo: 1
            tool: v1.0/io-any-1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test Any parameter with record input to a tool""")

    def test_conformance_v1_0_wf_input_any_integer_wf(self):
        """Test Any parameter with integer input to a workflow

        Generated from::

            job: v1.0/io-any-int.json
            label: wf_input_any_integer_wf
            output:
              t1: 7
            tool: v1.0/io-any-wf-1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test Any parameter with integer input to a workflow""")

    def test_conformance_v1_0_wf_input_any_string_wf(self):
        """Test Any parameter with string input to a workflow

        Generated from::

            job: v1.0/io-any-string.json
            label: wf_input_any_string_wf
            output:
              t1: '7'
            tool: v1.0/io-any-wf-1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test Any parameter with string input to a workflow""")

    def test_conformance_v1_0_wf_input_any_file_wf(self):
        """Test Any parameter with file input to a workflow

        Generated from::

            job: v1.0/io-any-file.json
            label: wf_input_any_file_wf
            output:
              t1: File
            tool: v1.0/io-any-wf-1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test Any parameter with file input to a workflow""")

    def test_conformance_v1_0_wf_input_any_array_wf(self):
        """Test Any parameter with array input to a workflow

        Generated from::

            job: v1.0/io-any-array.json
            label: wf_input_any_array_wf
            output:
              t1:
              - 1
              - moocow
            tool: v1.0/io-any-wf-1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test Any parameter with array input to a workflow""")

    def test_conformance_v1_0_wf_input_any_record_wf(self):
        """Test Any parameter with record input to a tool

        Generated from::

            job: v1.0/io-any-record.json
            label: wf_input_any_record_wf
            output:
              t1:
                cow: 5
                moo: 1
            tool: v1.0/io-any-wf-1.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test Any parameter with record input to a tool""")

    def test_conformance_v1_0_wf_input_union_default_unspec(self):
        """Test union type input to workflow with default unspecified

        Generated from::

            job: v1.0/empty.json
            label: wf_input_union_default_unspec
            output:
              o: the default value
            tool: v1.0/io-union-input-default-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test union type input to workflow with default unspecified""")

    def test_conformance_v1_0_wf_input_union_default_file(self):
        """Test union type input to workflow with default specified as file

        Generated from::

            job: v1.0/io-any-file.json
            label: wf_input_union_default_file
            output:
              o: File
            tool: v1.0/io-union-input-default-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test union type input to workflow with default specified as file""")

    def test_conformance_v1_0_wf_step_valuefrom_literal(self):
        """Test valueFrom on workflow step from literal (string).

        Generated from::

            job: v1.0/empty.json
            label: wf_step_valuefrom_literal
            output:
              val: 'moocow
            
                '
            tool: v1.0/step-valuefrom4-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test valueFrom on workflow step from literal (string).""")

    def test_conformance_v1_0_wf_step_valuefrom_basename(self):
        """Test valueFrom on workflow step using basename.

        Generated from::

            job: v1.0/wc-job.json
            label: wf_step_valuefrom_basename
            output:
              val1: 'whale.txt
            
                '
              val2: 'step1_out
            
                '
            tool: v1.0/step-valuefrom5-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test valueFrom on workflow step using basename.""")

    def test_conformance_v1_0_tool_output_arrays_ints(self):
        """Test output arrays in a tool (with ints).

        Generated from::

            job: v1.0/output-arrays-int-job.json
            label: tool_output_arrays_ints
            output:
              o:
              - 0
              - 1
              - 2
            tool: v1.0/output-arrays-int.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test output arrays in a tool (with ints).""")

    def test_conformance_v1_0_wf_output_arrays_ints(self):
        """Test output arrays in a workflow (with ints).

        Generated from::

            job: v1.0/output-arrays-int-job.json
            label: wf_output_arrays_ints
            output:
              o: 12
            tool: v1.0/output-arrays-int-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test output arrays in a workflow (with ints).""")

    def test_conformance_v1_0_wf_output_arrays_files(self):
        """Test output arrays in a workflow (with Files).

        Generated from::

            job: v1.0/output-arrays-file-job.json
            label: wf_output_arrays_files
            output:
              o:
              - basename: moo
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: Any
                size: 0
              - basename: cow
                checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                class: File
                location: Any
                size: 0
            tool: v1.0/output-arrays-file-wf.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test output arrays in a workflow (with Files).""")

    def test_conformance_v1_0_tool_docker_entrypoint(self):
        """Test Docker ENTRYPOINT usage

        Generated from::

            job: v1.0/empty.json
            label: tool_docker_entrypoint
            output:
              cow:
                basename: cow
                checksum: sha1$7a788f56fa49ae0ba5ebde780efe4d6a89b5db47
                class: File
                location: Any
                size: 4
            tool: v1.0/docker-run-cmd.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test Docker ENTRYPOINT usage""")

    def test_conformance_v1_0_tool_expressions_size_emptyfile(self):
        """Test use of size in expressions for an empty file

        Generated from::

            job: v1.0/job-input-array-one-empty-file.json
            label: tool_expressions_size_emptyfile
            output:
              output_file:
                basename: output.txt
                checksum: sha1$dad5a8472b87f6c5ef87d8fc6ef1458defc57250
                class: File
                location: Any
                size: 11
            tool: v1.0/size-expression-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test use of size in expressions for an empty file""")

    def test_conformance_v1_0_tool_expressions_size_fewfiles(self):
        """Test use of size in expressions for a few files

        Generated from::

            job: v1.0/job-input-array-few-files.json
            label: tool_expressions_size_fewfiles
            output:
              output_file:
                basename: output.txt
                checksum: sha1$9def39730e8012bd09bf8387648982728501737d
                class: File
                location: Any
                size: 31
            tool: v1.0/size-expression-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test use of size in expressions for a few files""")

