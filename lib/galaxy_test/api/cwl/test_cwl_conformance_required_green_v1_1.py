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
