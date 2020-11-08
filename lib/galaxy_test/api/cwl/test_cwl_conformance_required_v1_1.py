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

    def test_conformance_v1_1_wf_simple(self):
        """Test simple workflow

        Generated from::

            id: 53
            job: tests/revsort-job.json
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
            tool: tests/revsort.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test simple workflow""")

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

    def test_conformance_v1_1_format_checking(self):
        """Test simple format checking.

        Generated from::

            id: 64
            job: tests/formattest-job.json
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
            tool: tests/formattest.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test simple format checking.""")

    def test_conformance_v1_1_format_checking_subclass(self):
        """Test format checking against ontology using subclassOf.

        Generated from::

            id: 65
            job: tests/formattest2-job.json
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
            tool: tests/formattest2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test format checking against ontology using subclassOf.""")

    def test_conformance_v1_1_format_checking_equivalentclass(self):
        """Test format checking against ontology using equivalentClass.

        Generated from::

            id: 66
            job: tests/formattest2-job.json
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
            tool: tests/formattest3.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test format checking against ontology using equivalentClass.""")

    def test_conformance_v1_1_multiple_glob_expr_list(self):
        """Test support for returning multiple glob patterns from expression

        Generated from::

            id: 76
            job: tests/abc.json
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
            tool: tests/glob-expr-list.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test support for returning multiple glob patterns from expression""")

    def test_conformance_v1_1_wf_two_inputfiles_namecollision(self):
        """Test workflow two input files with same name.

        Generated from::

            id: 83
            job: tests/conflict-job.json
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
            tool: tests/conflict-wf.cwl#collision
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test workflow two input files with same name.""")

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

    def test_conformance_v1_1_directory_output(self):
        """Test directory output

        Generated from::

            id: 86
            job: tests/dir3-job.yml
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
            tool: tests/dir3.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test directory output""")

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

    def test_conformance_v1_1_wf_compound_doc(self):
        """Test compound workflow document

        Generated from::

            id: 111
            job: tests/revsort-job.json
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
            tool: tests/revsort-packed.cwl#main
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test compound workflow document""")

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

    def test_conformance_v1_1_wf_step_connect_undeclared_param(self):
        """Test that it is not an error to connect a parameter to a workflow step, even if the parameter doesn't appear in the `run` process inputs.

        Generated from::

            id: 132
            job: tests/empty.json
            label: wf_step_connect_undeclared_param
            output:
              out: 'hello inp1
            
                '
            tags:
            - required
            - workflow
            tool: tests/pass-unconnected.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that it is not an error to connect a parameter to a workflow step, even if the parameter doesn't appear in the `run` process inputs.""")

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

    def test_conformance_v1_1_any_without_defaults_unspecified_fails(self):
        """Test Any without defaults, unspecified, should fail.

        Generated from::

            id: 177
            job: tests/null-expression-echo-job.json
            label: any_without_defaults_unspecified_fails
            should_fail: true
            tags:
            - command_line_tool
            - required
            tool: tests/echo-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any without defaults, unspecified, should fail.""")

    def test_conformance_v1_1_any_without_defaults_specified_fails(self):
        """Test Any without defaults, specified, should fail.

        Generated from::

            id: 178
            job: tests/null-expression1-job.json
            label: any_without_defaults_specified_fails
            should_fail: true
            tags:
            - command_line_tool
            - required
            tool: tests/echo-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Any without defaults, specified, should fail.""")

    def test_conformance_v1_1_step_input_default_value_noexp(self):
        """Test default value on step input parameter, no ExpressionTool

        Generated from::

            id: 179
            job: tests/empty.json
            label: step_input_default_value_noexp
            output:
              wc_output:
                checksum: sha1$3596ea087bfdaf52380eae441077572ed289d657
                class: File
                size: 3
            tags:
            - workflow
            - required
            tool: tests/count-lines9-wf-noET.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default value on step input parameter, no ExpressionTool""")

    def test_conformance_v1_1_step_input_default_value_overriden_noexp(self):
        """Test default value on step input parameter overridden by provided source, no ExpressionTool

        Generated from::

            id: 180
            job: tests/cat-job.json
            label: step_input_default_value_overriden_noexp
            output:
              wc_output:
                checksum: sha1$e5fa44f2b31c1fb553b6021e7360d07d5d91ff5e
                class: File
                size: 2
            tags:
            - workflow
            - required
            tool: tests/count-lines11-wf-noET.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default value on step input parameter overridden by provided source, no ExpressionTool""")

    def test_conformance_v1_1_step_input_default_value_overriden_2nd_step_noexp(self):
        """Test default value on step input parameter overridden by provided source. With passthrough first step and no ExpressionTool

        Generated from::

            id: 187
            job: tests/cat-job.json
            label: step_input_default_value_overriden_2nd_step_noexp
            output:
              wc_output:
                checksum: sha1$e5fa44f2b31c1fb553b6021e7360d07d5d91ff5e
                class: File
                size: 2
            tags:
            - workflow
            - required
            tool: tests/count-lines11-extra-step-wf-noET.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default value on step input parameter overridden by provided source. With passthrough first step and no ExpressionTool""")

    def test_conformance_v1_1_step_input_default_value_overriden_2nd_step_null_noexp(self):
        """Test default value on step input parameter overridden by provided source. With null producing first step and no ExpressionTool

        Generated from::

            id: 189
            job: tests/empty.json
            label: step_input_default_value_overriden_2nd_step_null_noexp
            output:
              wc_output:
                checksum: sha1$3596ea087bfdaf52380eae441077572ed289d657
                class: File
                size: 3
            tags:
            - workflow
            - required
            tool: tests/count-lines11-null-step-wf-noET.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test default value on step input parameter overridden by provided source. With null producing first step and no ExpressionTool""")

    def test_conformance_v1_1_stdin_from_directory_literal_with_local_file(self):
        """Pipe to stdin from user provided local File via a Directory literal

        Generated from::

            id: 190
            job: tests/cat-from-dir-job.yaml
            label: stdin_from_directory_literal_with_local_file
            output:
              output:
                checksum: sha1$47a013e660d408619d894b20806b1d5086aab03b
                class: File
                size: 13
            tags:
            - command_line_tool
            - required
            tool: tests/cat-from-dir.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Pipe to stdin from user provided local File via a Directory literal""")

    def test_conformance_v1_1_stdin_from_directory_literal_with_literal_file(self):
        """Pipe to stdin from literal File via a Directory literal

        Generated from::

            id: 191
            job: tests/cat-from-dir-with-literal-file.yaml
            label: stdin_from_directory_literal_with_literal_file
            output:
              output:
                checksum: sha1$ef88e689559565999700d6fea7cf7ba306d04360
                class: File
                size: 26
            tags:
            - command_line_tool
            - required
            tool: tests/cat-from-dir.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Pipe to stdin from literal File via a Directory literal""")

    def test_conformance_v1_1_directory_literal_with_literal_file_nostdin(self):
        """Test non-stdin reference to literal File via a Directory literal

        Generated from::

            id: 192
            job: tests/cat-from-dir-with-literal-file.yaml
            label: directory_literal_with_literal_file_nostdin
            output:
              output_file:
                checksum: sha1$ef88e689559565999700d6fea7cf7ba306d04360
                class: File
                size: 26
            tags:
            - command_line_tool
            - required
            tool: tests/cat3-from-dir.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test non-stdin reference to literal File via a Directory literal""")

    def test_conformance_v1_1_no_inputs_commandlinetool(self):
        """Test CommandLineTool without inputs

        Generated from::

            id: 193
            label: no_inputs_commandlinetool
            output:
              output:
                checksum: sha1$1334e67fe9eb70db8ae14ccfa6cfb59e2cc24eae
                class: File
                location: output
                size: 4
            tags:
            - command_line_tool
            - required
            tool: tests/no-inputs-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test CommandLineTool without inputs""")

    def test_conformance_v1_1_no_outputs_commandlinetool(self):
        """Test CommandLineTool without outputs

        Generated from::

            id: 194
            job: tests/cat-job.json
            label: no_outputs_commandlinetool
            output: {}
            tags:
            - command_line_tool
            - required
            tool: tests/no-outputs-tool.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test CommandLineTool without outputs""")

    def test_conformance_v1_1_no_inputs_workflow(self):
        """Test Workflow without inputs

        Generated from::

            id: 195
            label: no_inputs_workflow
            output:
              output:
                checksum: sha1$1334e67fe9eb70db8ae14ccfa6cfb59e2cc24eae
                class: File
                location: output
                size: 4
            tags:
            - workflow
            - required
            tool: tests/no-inputs-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Workflow without inputs""")

    def test_conformance_v1_1_no_outputs_workflow(self):
        """Test Workflow without outputs

        Generated from::

            id: 196
            job: tests/cat-job.json
            label: no_outputs_workflow
            output: {}
            tags:
            - workflow
            - required
            tool: tests/no-outputs-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test Workflow without outputs""")

    def test_conformance_v1_1_anonymous_enum_in_array(self):
        """Test an anonymous enum inside an array inside a record

        Generated from::

            id: 197
            job: tests/anon_enum_inside_array.yml
            label: anonymous_enum_in_array
            output:
              result:
                checksum: sha1$2132943d72c39423e0b9425cbc40dfd5bf3e9cb2
                class: File
                size: 39
            tags:
            - command_line_tool
            - required
            tool: tests/anon_enum_inside_array.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test an anonymous enum inside an array inside a record""")

    def test_conformance_v1_1_secondary_files_in_unnamed_records(self):
        """Test secondaryFiles on anonymous record fields

        Generated from::

            id: 200
            job: tests/record-secondaryFiles-job.yml
            label: secondary_files_in_unnamed_records
            output: {}
            tags:
            - command_line_tool
            - required
            tool: tests/record-in-secondaryFiles.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test secondaryFiles on anonymous record fields""")

    def test_conformance_v1_1_secondary_files_in_output_records(self):
        """Test secondaryFiles on output record fields

        Generated from::

            id: 202
            job: tests/empty.json
            label: secondary_files_in_output_records
            output:
              record_output:
                f1:
                  checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: A
                  secondaryFiles:
                  - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                    class: File
                    location: A.s2
                    size: 0
                  size: 0
                f2:
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: B
                  secondaryFiles:
                  - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                    class: File
                    location: B.s3
                    size: 0
                  size: 0
                - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                  class: File
                  location: C
                  secondaryFiles:
                  - checksum: sha1$da39a3ee5e6b4b0d3255bfef95601890afd80709
                    class: File
                    location: C.s3
                    size: 0
                  size: 0
            tags:
            - command_line_tool
            - required
            tool: tests/record-out-secondaryFiles.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test secondaryFiles on output record fields""")

    def test_conformance_v1_1_secondary_files_workflow_propagation(self):
        """Test secondaryFiles propagation through workflow

        Generated from::

            id: 203
            job: tests/record-secondaryFiles-job.yml
            label: secondary_files_workflow_propagation
            output: {}
            tags:
            - workflow
            - required
            tool: tests/record-in-secondaryFiles-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test secondaryFiles propagation through workflow""")

    def test_conformance_v1_1_secondary_files_missing(self):
        """Test checking when secondaryFiles are missing

        Generated from::

            id: 204
            job: tests/record-secondaryFiles-job.yml
            label: secondary_files_missing
            should_fail: true
            tags:
            - workflow
            - required
            tool: tests/record-in-secondaryFiles-missing-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test checking when secondaryFiles are missing""")

    def test_conformance_v1_1_input_records_file_entry_with_format(self):
        """Test format on anonymous record fields

        Generated from::

            id: 205
            job: tests/record-format-job.yml
            label: input_records_file_entry_with_format
            output: {}
            tags:
            - command_line_tool
            - required
            tool: tests/record-in-format.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test format on anonymous record fields""")

    def test_conformance_v1_1_fail_glob_outside_output_dir(self):
        """Test fail trying to glob outside output directory

        Generated from::

            id: 232
            job: tests/empty.json
            label: fail_glob_outside_output_dir
            should_fail: true
            tags:
            - required
            tool: tests/glob-path-error.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test fail trying to glob outside output directory""")

    def test_conformance_v1_1_outputbinding_glob_directory(self):
        """Test that OutputBinding.glob accepts Directories

        Generated from::

            id: 237
            job: tests/empty.json
            label: outputbinding_glob_directory
            output:
              directories:
              - basename: a_dir
                class: Directory
                listing: []
              - basename: b_dir
                class: Directory
                listing: []
              - basename: c_dir
                class: Directory
                listing: []
            tags:
            - required
            - command_line_tool
            tool: tests/glob_directory.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that OutputBinding.glob accepts Directories""")

    def test_conformance_v1_1_stage_file_array_to_dir(self):
        """Test that array of input files can be staged to directory with entryname

        Generated from::

            id: 238
            job: tests/stage_file_array.job.json
            label: stage_file_array_to_dir
            output:
              output:
              - basename: sfa-1.txt
                checksum: sha1$4c1cd0638ab3580310823fd1556d27ecb4816df6
                class: File
                size: 49
              - basename: sfa-1.txt.sec
                checksum: sha1$40f4ee1bcd1a9466fcd2e48cf7fc3798025d2f9a
                class: File
                size: 59
              - basename: sfa-2.txt
                checksum: sha1$4c1cd0638ab3580310823fd1556d27ecb4816df6
                class: File
                size: 49
              - basename: sfa-2.txt.sec
                checksum: sha1$40f4ee1bcd1a9466fcd2e48cf7fc3798025d2f9a
                class: File
                size: 59
            tags:
            - required
            - command_line_tool
            tool: tests/stage_file_array.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that array of input files can be staged to directory with entryname""")

    def test_conformance_v1_1_stage_file_array_to_dir_basename(self):
        """Test that array of input files can be staged to directory with basename

        Generated from::

            id: 239
            job: tests/stage_file_array.job.json
            label: stage_file_array_to_dir_basename
            output:
              output:
              - basename: sfa-1.txt
                checksum: sha1$4c1cd0638ab3580310823fd1556d27ecb4816df6
                class: File
                size: 49
              - basename: sfa-1.txt.sec
                checksum: sha1$40f4ee1bcd1a9466fcd2e48cf7fc3798025d2f9a
                class: File
                size: 59
              - basename: sfa-2.txt
                checksum: sha1$4c1cd0638ab3580310823fd1556d27ecb4816df6
                class: File
                size: 49
              - basename: sfa-2.txt.sec
                checksum: sha1$40f4ee1bcd1a9466fcd2e48cf7fc3798025d2f9a
                class: File
                size: 59
            tags:
            - required
            - command_line_tool
            tool: tests/stage_file_array_basename.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that array of input files can be staged to directory with basename""")

    def test_conformance_v1_1_stage_file_array_to_dir_basename_entryname(self):
        """Test that if array of input files are staged to directory with basename and entryname, entryname overrides

        Generated from::

            id: 240
            job: tests/stage_file_array.job.json
            label: stage_file_array_to_dir_basename_entryname
            output:
              output:
              - basename: sfa-1.txt
                checksum: sha1$4c1cd0638ab3580310823fd1556d27ecb4816df6
                class: File
                size: 49
              - basename: sfa-1.txt.sec
                checksum: sha1$40f4ee1bcd1a9466fcd2e48cf7fc3798025d2f9a
                class: File
                size: 59
              - basename: sfa-2.txt
                checksum: sha1$4c1cd0638ab3580310823fd1556d27ecb4816df6
                class: File
                size: 49
              - basename: sfa-2.txt.sec
                checksum: sha1$40f4ee1bcd1a9466fcd2e48cf7fc3798025d2f9a
                class: File
                size: 59
            tags:
            - required
            - command_line_tool
            tool: tests/stage_file_array_basename_and_entryname.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that if array of input files are staged to directory with basename and entryname, entryname overrides""")

    def test_conformance_v1_1_inputBinding_position_expr(self):
        """Test for expression in the InputBinding.position field; also test using emoji in CWL document and tool output


        Generated from::

            id: 249
            job: tests/echo-position-expr-job.yml
            label: inputBinding_position_expr
            output:
              out: "\U0001F57A 1 singular sensation!\n"
            tags:
            - command_line_tool
            - required
            tool: tests/echo-position-expr.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test for expression in the InputBinding.position field; also test using emoji in CWL document and tool output
""")

    def test_conformance_v1_1_outputEval_exitCode(self):
        """Can access exit code in outputEval

        Generated from::

            id: 250
            job: tests/empty.json
            label: outputEval_exitCode
            output:
              code: 7
            tags:
            - command_line_tool
            - required
            tool: tests/exitcode.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Can access exit code in outputEval""")

    def test_conformance_v1_1_any_input_param_graph_no_default(self):
        """Test use of $graph without specifying which process to run

        Generated from::

            id: 251
            job: tests/env-job.json
            label: any_input_param_graph_no_default
            output:
              out: 'hello test env
            
                '
            tags:
            - required
            - command_line_tool
            tool: tests/echo-tool-packed.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test use of $graph without specifying which process to run""")

    def test_conformance_v1_1_any_input_param_graph_no_default_hashmain(self):
        """Test use of $graph without specifying which process to run, hash-prefixed "main"


        Generated from::

            id: 252
            job: tests/env-job.json
            label: any_input_param_graph_no_default_hashmain
            output:
              out: 'hello test env
            
                '
            tags:
            - required
            - command_line_tool
            tool: tests/echo-tool-packed2.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test use of $graph without specifying which process to run, hash-prefixed "main"
""")

    def test_conformance_v1_1_optional_numerical_output_returns_0_not_null(self):
        """Test that optional number output is returned as 0, not null


        Generated from::

            id: 253
            job: tests/empty.json
            label: optional_numerical_output_returns_0_not_null
            output:
              out: 0
            tags:
            - required
            - inline_javascript
            - command_line_tool
            tool: tests/optional-numerical-output-0.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.1""", """Test that optional number output is returned as 0, not null
""")
