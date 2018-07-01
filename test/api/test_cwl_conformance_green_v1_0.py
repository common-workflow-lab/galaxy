
"""Test CWL conformance for version $version."""

from .test_workflows_cwl import BaseCwlWorklfowTestCase


class CwlConformanceTestCase(BaseCwlWorklfowTestCase):
    """Test case mapping to CWL conformance tests for version $version."""

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

    def test_conformance_v1_0_170(self):
        """Test use of size in expressions for an empty file

        Generated from::

            job: v1.0/job-input-array-one-empty-file.json
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

