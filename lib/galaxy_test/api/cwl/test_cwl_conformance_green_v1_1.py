"""Test CWL conformance for version v1.1."""

from ..test_workflows_cwl import BaseCwlWorklfowTestCase


class CwlConformanceTestCase(BaseCwlWorklfowTestCase):
    """Test case mapping to CWL conformance tests for version v1.1."""

    def test_conformance_v1_1_cl_basic_generation(self):
        """General test of command line generation

        Generated from::

            id: 1
            job: tests/bwa-mem-job.json
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
            tool: tests/bwa-mem-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """General test of command line generation""")

    def test_conformance_v1_1_nested_prefixes_arrays(self):
        """Test nested prefixes with arrays

        Generated from::

            id: 2
            job: tests/bwa-mem-job.json
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
            tool: tests/binding-test.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test nested prefixes with arrays""")

    def test_conformance_v1_1_nested_cl_bindings(self):
        """Test nested command line bindings

        Generated from::

            id: 3
            job: tests/tmap-job.json
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
            tool: tests/tmap-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test nested command line bindings""")

    def test_conformance_v1_1_cl_optional_inputs_missing(self):
        """Test command line with optional input (missing)

        Generated from::

            id: 4
            job: tests/cat-job.json
            label: cl_optional_inputs_missing
            output:
              args:
              - cat
              - hello.txt
            tags:
            - required
            - command_line_tool
            tool: tests/cat1-testcli.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command line with optional input (missing)""")

    def test_conformance_v1_1_cl_optional_bindings_provided(self):
        """Test command line with optional input (provided)

        Generated from::

            id: 5
            job: tests/cat-n-job.json
            label: cl_optional_bindings_provided
            output:
              args:
              - cat
              - -n
              - hello.txt
            tags:
            - required
            - command_line_tool
            tool: tests/cat1-testcli.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command line with optional input (provided)""")

    def test_conformance_v1_1_initworkdir_expreng_requirements(self):
        """Test InitialWorkDirRequirement ExpressionEngineRequirement.engineConfig feature

        Generated from::

            id: 6
            job: tests/cat-job.json
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
            tool: tests/template-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test InitialWorkDirRequirement ExpressionEngineRequirement.engineConfig feature""")

    def test_conformance_v1_1_stdout_redirect_docker(self):
        """Test command execution in Docker with stdout redirection

        Generated from::

            id: 7
            job: tests/cat-job.json
            label: stdout_redirect_docker
            output:
              output_file:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: output.txt
                size: 13
            tags:
            - docker
            - command_line_tool
            tool: tests/cat3-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command execution in Docker with stdout redirection""")

    def test_conformance_v1_1_stdout_redirect_shortcut_docker(self):
        """Test command execution in Docker with shortcut stdout redirection

        Generated from::

            id: 8
            job: tests/cat-job.json
            label: stdout_redirect_shortcut_docker
            output:
              output_file:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: Any
                size: 13
            tags:
            - docker
            - command_line_tool
            tool: tests/cat3-tool-shortcut.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command execution in Docker with shortcut stdout redirection""")

    def test_conformance_v1_1_stdout_redirect_mediumcut_docker(self):
        """Test command execution in Docker with mediumcut stdout redirection

        Generated from::

            id: 9
            job: tests/cat-job.json
            label: stdout_redirect_mediumcut_docker
            output:
              output_file:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                location: cat-out
                size: 13
            tags:
            - docker
            - command_line_tool
            tool: tests/cat3-tool-mediumcut.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command execution in Docker with mediumcut stdout redirection""")

    def test_conformance_v1_1_stderr_redirect(self):
        """Test command line with stderr redirection

        Generated from::

            id: 10
            job: tests/empty.json
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
            tool: tests/stderr.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command line with stderr redirection""")

    def test_conformance_v1_1_stderr_redirect_shortcut(self):
        """Test command line with stderr redirection, brief syntax

        Generated from::

            id: 11
            job: tests/empty.json
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
            tool: tests/stderr-shortcut.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command line with stderr redirection, brief syntax""")

    def test_conformance_v1_1_stderr_redirect_mediumcut(self):
        """Test command line with stderr redirection, named brief syntax

        Generated from::

            id: 12
            job: tests/empty.json
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
            tool: tests/stderr-mediumcut.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command line with stderr redirection, named brief syntax""")

    def test_conformance_v1_1_stdinout_redirect_docker(self):
        """Test command execution in Docker with stdin and stdout redirection

        Generated from::

            id: 13
            job: tests/cat-job.json
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
            tool: tests/cat4-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command execution in Docker with stdin and stdout redirection""")

    def test_conformance_v1_1_expression_any(self):
        """Test default usage of Any in expressions.

        Generated from::

            id: 14
            job: tests/empty.json
            label: expression_any
            output:
              output: 1
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/null-expression1-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default usage of Any in expressions.""")

    def test_conformance_v1_1_expression_any_null(self):
        """Test explicitly passing null to Any type inputs with default values.

        Generated from::

            id: 15
            job: tests/null-expression1-job.json
            label: expression_any_null
            output:
              output: 1
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/null-expression1-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test explicitly passing null to Any type inputs with default values.""")

    def test_conformance_v1_1_expression_any_string(self):
        """Testing the string 'null' does not trip up an Any with a default value.

        Generated from::

            id: 16
            job: tests/null-expression2-job.json
            label: expression_any_string
            output:
              output: 2
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/null-expression1-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Testing the string 'null' does not trip up an Any with a default value.""")

    def test_conformance_v1_1_expression_any_nodefaultany(self):
        """Test Any without defaults cannot be unspecified.

        Generated from::

            id: 17
            job: tests/empty.json
            label: expression_any_nodefaultany
            should_fail: true
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/null-expression2-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any without defaults cannot be unspecified.""")

    def test_conformance_v1_1_expression_any_null_nodefaultany(self):
        """Test explicitly passing null to Any type without a default value.

        Generated from::

            id: 18
            job: tests/null-expression1-job.json
            label: expression_any_null_nodefaultany
            should_fail: true
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/null-expression2-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test explicitly passing null to Any type without a default value.""")

    def test_conformance_v1_1_expression_any_nullstring_nodefaultany(self):
        """Testing the string 'null' does not trip up an Any without a default value.

        Generated from::

            id: 19
            job: tests/null-expression2-job.json
            label: expression_any_nullstring_nodefaultany
            output:
              output: 2
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/null-expression2-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Testing the string 'null' does not trip up an Any without a default value.""")

    def test_conformance_v1_1_any_outputSource_compatibility(self):
        """Testing Any type compatibility in outputSource

        Generated from::

            id: 20
            job: tests/any-type-job.json
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
            tool: tests/any-type-compat.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Testing Any type compatibility in outputSource""")

    def test_conformance_v1_1_stdinout_redirect(self):
        """Test command execution in with stdin and stdout redirection

        Generated from::

            id: 21
            job: tests/cat-job.json
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
            tool: tests/cat-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command execution in with stdin and stdout redirection""")

    def test_conformance_v1_1_expression_parseint(self):
        """Test ExpressionTool with Javascript engine

        Generated from::

            id: 22
            job: tests/parseInt-job.json
            label: expression_parseint
            output:
              output: 42
            tags:
            - inline_javascript
            - expression_tool
            tool: tests/parseInt-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test ExpressionTool with Javascript engine""")

    def test_conformance_v1_1_expression_outputEval(self):
        """Test outputEval to transform output

        Generated from::

            id: 23
            job: tests/wc-job.json
            label: expression_outputEval
            output:
              output: 16
            tags:
            - inline_javascript
            - command_line_tool
            tool: tests/wc2-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test outputEval to transform output""")

    def test_conformance_v1_1_wf_default_tool_default(self):
        """Test that workflow defaults override tool defaults

        Generated from::

            id: 33
            job: tests/empty.json
            label: wf_default_tool_default
            output:
              default_output: workflow_default
            tags:
            - required
            - workflow
            tool: tests/echo-wf-default.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that workflow defaults override tool defaults""")

    def test_conformance_v1_1_envvar_req(self):
        """Test EnvVarRequirement

        Generated from::

            id: 34
            job: tests/env-job.json
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
            tool: tests/env-tool1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test EnvVarRequirement""")

    def test_conformance_v1_1_any_input_param(self):
        """Test Any type input parameter

        Generated from::

            id: 44
            job: tests/env-job.json
            label: any_input_param
            output:
              out: 'hello test env
            
                '
            tags:
            - required
            - command_line_tool
            tool: tests/echo-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any type input parameter""")

    def test_conformance_v1_1_nested_workflow(self):
        """Test nested workflow

        Generated from::

            id: 45
            job: tests/wc-job.json
            label: nested_workflow
            output:
              count_output: 16
            tags:
            - subworkflow
            - workflow
            - inline_javascript
            tool: tests/count-lines8-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test nested workflow""")

    def test_conformance_v1_1_requirement_priority(self):
        """Test requirement priority

        Generated from::

            id: 46
            job: tests/env-job.json
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
            tool: tests/env-wf1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test requirement priority""")

    def test_conformance_v1_1_requirement_override_hints(self):
        """Test requirements override hints

        Generated from::

            id: 47
            job: tests/env-job.json
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
            tool: tests/env-wf2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test requirements override hints""")

    def test_conformance_v1_1_requirement_workflow_steps(self):
        """Test requirements on workflow steps

        Generated from::

            id: 48
            job: tests/env-job.json
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
            tool: tests/env-wf3.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test requirements on workflow steps""")

    def test_conformance_v1_1_step_input_default_value(self):
        """Test default value on step input parameter

        Generated from::

            id: 49
            job: tests/empty.json
            label: step_input_default_value
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines9-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default value on step input parameter""")

    def test_conformance_v1_1_step_input_default_value_nullsource(self):
        """Test use default value on step input parameter with null source

        Generated from::

            id: 51
            job: tests/file1-null.json
            label: step_input_default_value_nullsource
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines11-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test use default value on step input parameter with null source""")

    def test_conformance_v1_1_hints_unknown_ignored(self):
        """Test unknown hints are ignored.

        Generated from::

            id: 54
            job: tests/cat-job.json
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
            tool: tests/cat5-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test unknown hints are ignored.""")

    def test_conformance_v1_1_initial_workdir_secondary_files_expr(self):
        """Test InitialWorkDirRequirement linking input files and capturing secondaryFiles on input and output. Also tests the use of a variety of parameter references and expressions in the secondaryFiles field.

        Generated from::

            id: 55
            job: tests/search-job.json
            label: initial_workdir_secondary_files_expr
            output:
              indexedfile:
                checksum: sha1$327fc7aedf4f6b69a42a7c8b808dc5a7aff61376
                class: File
                location: input.txt
                secondaryFiles:
                - checksum: sha1$1f6fe811644355974cdd06d9eb695d6e859f3b44
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
            tool: tests/search.cwl#main
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test InitialWorkDirRequirement linking input files and capturing secondaryFiles on input and output. Also tests the use of a variety of parameter references and expressions in the secondaryFiles field.""")

    def test_conformance_v1_1_rename(self):
        """Test InitialWorkDirRequirement with expression in filename.

        Generated from::

            id: 56
            job: tests/rename-job.json
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
            tool: tests/rename.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test InitialWorkDirRequirement with expression in filename.""")

    def test_conformance_v1_1_initial_workdir_trailingnl(self):
        """Test if trailing newline is present in file entry in InitialWorkDir

        Generated from::

            id: 57
            job: tests/string-job.json
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
            tool: tests/iwdr-entry.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test if trailing newline is present in file entry in InitialWorkDir""")

    def test_conformance_v1_1_inline_expressions(self):
        """Test inline expressions

        Generated from::

            id: 58
            job: tests/wc-job.json
            label: inline_expressions
            output:
              output: 16
            tags:
            - inline_javascript
            - command_line_tool
            tool: tests/wc4-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test inline expressions""")

    def test_conformance_v1_1_schemadef_req_tool_param(self):
        """Test SchemaDefRequirement definition used in tool parameter

        Generated from::

            id: 59
            job: tests/schemadef-job.json
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
            tool: tests/schemadef-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test SchemaDefRequirement definition used in tool parameter""")

    def test_conformance_v1_1_schemadef_req_wf_param(self):
        """Test SchemaDefRequirement definition used in workflow parameter

        Generated from::

            id: 60
            job: tests/schemadef-job.json
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
            tool: tests/schemadef-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test SchemaDefRequirement definition used in workflow parameter""")

    def test_conformance_v1_1_param_evaluation_noexpr(self):
        """Test parameter evaluation, no support for JS expressions

        Generated from::

            id: 61
            job: tests/empty.json
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
            tool: tests/params.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test parameter evaluation, no support for JS expressions""")

    def test_conformance_v1_1_param_evaluation_expr(self):
        """Test parameter evaluation, with support for JS expressions

        Generated from::

            id: 62
            job: tests/empty.json
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
            tool: tests/params2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test parameter evaluation, with support for JS expressions""")

    def test_conformance_v1_1_metadata(self):
        """Test metadata

        Generated from::

            id: 63
            job: tests/cat-job.json
            label: metadata
            output: {}
            tags:
            - required
            tool: tests/metadata.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test metadata""")

    def test_conformance_v1_1_valuefrom_secondexpr_ignored(self):
        """Test that second expression in concatenated valueFrom is not ignored

        Generated from::

            id: 69
            job: tests/cat-job.json
            label: valuefrom_secondexpr_ignored
            output:
              out: 'a string
            
                '
            tags:
            - inline_javascript
            - command_line_tool
            tool: tests/vf-concat.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that second expression in concatenated valueFrom is not ignored""")

    def test_conformance_v1_1_docker_json_output_path(self):
        """Test support for reading cwl.output.json when running in a Docker container and just 'path' is provided.

        Generated from::

            id: 74
            job: tests/empty.json
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
            tool: tests/test-cwl-out.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test support for reading cwl.output.json when running in a Docker container and just 'path' is provided.""")

    def test_conformance_v1_1_docker_json_output_location(self):
        """Test support for reading cwl.output.json when running in a Docker container and just 'location' is provided.

        Generated from::

            id: 75
            job: tests/empty.json
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
            tool: tests/test-cwl-out2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test support for reading cwl.output.json when running in a Docker container and just 'location' is provided.""")

    def test_conformance_v1_1_directory_input_docker(self):
        """Test directory input in Docker

        Generated from::

            id: 85
            job: tests/dir-job.yml
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
            - shell_command
            tool: tests/dir2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test directory input in Docker""")

    def test_conformance_v1_1_writable_stagedfiles(self):
        """Test writable staged files.

        Generated from::

            id: 89
            job: tests/stagefile-job.yml
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
            tool: tests/stagefile.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test writable staged files.""")

    def test_conformance_v1_1_input_file_literal(self):
        """Test file literal as input

        Generated from::

            id: 90
            job: tests/file-literal.yml
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
            tool: tests/cat3-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test file literal as input""")

    def test_conformance_v1_1_initial_workdir_expr(self):
        """Test expression in InitialWorkDir listing

        Generated from::

            id: 91
            job: tests/arguments-job.yml
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
            tool: tests/linkfile.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test expression in InitialWorkDir listing""")

    def test_conformance_v1_1_nameroot_nameext_stdout_expr(self):
        """Test nameroot/nameext expression in arguments, stdout

        Generated from::

            id: 92
            job: tests/wc-job.json
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
            tool: tests/nameroot.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test nameroot/nameext expression in arguments, stdout""")

    def test_conformance_v1_1_cl_gen_arrayofarrays(self):
        """Test command line generation of array-of-arrays

        Generated from::

            id: 94
            job: tests/nested-array-job.yml
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
            tool: tests/nested-array.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test command line generation of array-of-arrays""")

    def test_conformance_v1_1_initial_workdir_output(self):
        """Test output of InitialWorkDir

        Generated from::

            id: 98
            job: tests/initialworkdirrequirement-docker-out-job.json
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
            tool: tests/initialworkdirrequirement-docker-out.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test output of InitialWorkDir""")

    def test_conformance_v1_1_exprtool_directory_literal(self):
        """Test directory literal output created by ExpressionTool

        Generated from::

            id: 102
            job: tests/dir7.yml
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
            tool: tests/dir7.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test directory literal output created by ExpressionTool""")

    def test_conformance_v1_1_exprtool_file_literal(self):
        """Test file literal output created by ExpressionTool

        Generated from::

            id: 103
            job: tests/empty.json
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
            tool: tests/file-literal-ex.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test file literal output created by ExpressionTool""")

    def test_conformance_v1_1_hints_import(self):
        """Test hints with $import

        Generated from::

            id: 105
            job: tests/empty.json
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
            tool: tests/imported-hint.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test hints with $import""")

    def test_conformance_v1_1_default_path_notfound_warning(self):
        """Test warning instead of error when default path is not found

        Generated from::

            id: 106
            job: tests/default_path_job.yml
            label: default_path_notfound_warning
            output: {}
            tags:
            - required
            - command_line_tool
            tool: tests/default_path.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test warning instead of error when default path is not found""")

    def test_conformance_v1_1_null_missing_params(self):
        """Test that missing parameters are null (not undefined) in expression

        Generated from::

            id: 109
            job: tests/empty.json
            label: null_missing_params
            output:
              out: 't
            
                '
            tags:
            - inline_javascript
            - command_line_tool
            tool: tests/null-defined.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that missing parameters are null (not undefined) in expression""")

    def test_conformance_v1_1_initialworkpath_output(self):
        """Test that file path in $(inputs) for initialworkdir is in $(outdir).

        Generated from::

            id: 113
            job: tests/wc-job.json
            label: initialworkpath_output
            output: {}
            tags:
            - initial_work_dir
            - command_line_tool
            tool: tests/initialwork-path.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that file path in $(inputs) for initialworkdir is in $(outdir).""")

    def test_conformance_v1_1_shelldir_notinterpreted(self):
        """Test that shell directives are not interpreted.

        Generated from::

            id: 116
            job: tests/empty.json
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
            tool: tests/shellchar.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that shell directives are not interpreted.""")

    def test_conformance_v1_1_initial_workdir_empty_writable(self):
        """Test empty writable dir with InitialWorkDirRequirement

        Generated from::

            id: 118
            job: tests/empty.json
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
            tool: tests/writable-dir.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test empty writable dir with InitialWorkDirRequirement""")

    def test_conformance_v1_1_initial_workdir_empty_writable_docker(self):
        """Test empty writable dir with InitialWorkDirRequirement inside Docker

        Generated from::

            id: 119
            job: tests/empty.json
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
            tool: tests/writable-dir-docker.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test empty writable dir with InitialWorkDirRequirement inside Docker""")

    def test_conformance_v1_1_fileliteral_input_docker(self):
        """Test file literal as input without Docker

        Generated from::

            id: 121
            job: tests/file-literal.yml
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
            tool: tests/cat3-nodocker.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test file literal as input without Docker""")

    def test_conformance_v1_1_outputbinding_glob_sorted(self):
        """Test that OutputBinding.glob is sorted as specified by POSIX

        Generated from::

            id: 122
            job: tests/empty.json
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
            tool: tests/glob_test.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that OutputBinding.glob is sorted as specified by POSIX""")

    def test_conformance_v1_1_booleanflags_cl_noinputbinding(self):
        """Test that boolean flags do not appear on command line if inputBinding is empty and not null

        Generated from::

            id: 124
            job: tests/bool-empty-inputbinding-job.json
            label: booleanflags_cl_noinputbinding
            output:
              args: []
            tags:
            - required
            - command_line_tool
            tool: tests/bool-empty-inputbinding.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that boolean flags do not appear on command line if inputBinding is empty and not null""")

    def test_conformance_v1_1_expr_reference_self_noinput(self):
        """Test that expression engine does not fail to evaluate reference to self with unprovided input

        Generated from::

            id: 125
            job: tests/empty.json
            label: expr_reference_self_noinput
            output:
              args: []
            tags:
            - required
            - command_line_tool
            tool: tests/stage-unprovided-file.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that expression engine does not fail to evaluate reference to self with unprovided input""")

    def test_conformance_v1_1_success_codes(self):
        """Test successCodes

        Generated from::

            id: 126
            job: tests/empty.json
            label: success_codes
            output: {}
            tags:
            - required
            - command_line_tool
            tool: tests/exit-success.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test successCodes""")

    def test_conformance_v1_1_cl_empty_array_input(self):
        """Test that empty array input does not add anything to command line

        Generated from::

            id: 128
            job: tests/empty-array-job.json
            label: cl_empty_array_input
            output:
              args: []
            tags:
            - required
            - command_line_tool
            tool: tests/empty-array-input.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that empty array input does not add anything to command line""")

    def test_conformance_v1_1_resreq_step_overrides_wf(self):
        """Test that ResourceRequirement on a step level redefines requirement on the workflow level

        Generated from::

            id: 129
            job: tests/empty.json
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
            tool: tests/steplevel-resreq.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that ResourceRequirement on a step level redefines requirement on the workflow level""")

    def test_conformance_v1_1_valuefrom_constant_overrides_inputs(self):
        """Test valueFrom with constant value overriding provided array inputs

        Generated from::

            id: 130
            job: tests/array-of-strings-job.yml
            label: valuefrom_constant_overrides_inputs
            output:
              args:
              - replacementValue
            tags:
            - required
            - command_line_tool
            tool: tests/valueFrom-constant.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test valueFrom with constant value overriding provided array inputs""")

    def test_conformance_v1_1_wf_step_access_undeclared_param(self):
        """Test that parameters that don't appear in the `run` process inputs are not present in the input object used to run the tool.

        Generated from::

            id: 133
            job: tests/empty.json
            label: wf_step_access_undeclared_param
            should_fail: true
            tags:
            - required
            - workflow
            tool: tests/fail-unconnected.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that parameters that don't appear in the `run` process inputs are not present in the input object used to run the tool.""")

    def test_conformance_v1_1_workflow_union_default_input_with_file_provided(self):
        """Test union type input to workflow with default specified as file

        Generated from::

            id: 168
            job: tests/io-any-file.json
            label: workflow_union_default_input_with_file_provided
            output:
              o: File
            tags:
            - workflow
            - inline_javascript
            - expression_tool
            tool: tests/io-union-input-default-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test union type input to workflow with default specified as file""")

    def test_conformance_v1_1_expression_tool_int_array_output(self):
        """Test output arrays in a tool (with ints).

        Generated from::

            id: 171
            job: tests/output-arrays-int-job.json
            label: expression_tool_int_array_output
            output:
              o:
              - 0
              - 1
              - 2
            tags:
            - expression_tool
            - inline_javascript
            tool: tests/output-arrays-int.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test output arrays in a tool (with ints).""")
