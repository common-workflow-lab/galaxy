"""Test CWL conformance for version v1.2."""

from ..test_workflows_cwl import BaseCwlWorklfowTestCase


class CwlConformanceTestCase(BaseCwlWorklfowTestCase):
    """Test case mapping to CWL conformance tests for version v1.2."""

    def test_conformance_v1_2_wf_wc_parseInt(self):
        """Test two step workflow with imported tools

        Generated from::

            id: 24
            job: tests/wc-job.json
            label: wf_wc_parseInt
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines1-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.2""", """Test two step workflow with imported tools""")

    def test_conformance_v1_2_wf_wc_expressiontool(self):
        """Test two step workflow with inline tools

        Generated from::

            id: 25
            job: tests/wc-job.json
            label: wf_wc_expressiontool
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines2-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.2""", """Test two step workflow with inline tools""")

    def test_conformance_v1_2_wf_wc_scatter(self):
        """Test single step workflow with Scatter step

        Generated from::

            id: 26
            job: tests/count-lines3-job.json
            label: wf_wc_scatter
            output:
              count_output:
              - 16
              - 1
            tags:
            - scatter
            - inline_javascript
            - workflow
            tool: tests/count-lines3-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.2""", """Test single step workflow with Scatter step""")

    def test_conformance_v1_2_wf_wc_scatter_multiple_merge(self):
        """Test single step workflow with Scatter step and two data links connected to same input, default merge behavior

        Generated from::

            id: 27
            job: tests/count-lines4-job.json
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
            tool: tests/count-lines4-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.2""", """Test single step workflow with Scatter step and two data links connected to same input, default merge behavior""")

    def test_conformance_v1_2_wf_wc_scatter_multiple_flattened(self):
        """Test single step workflow with Scatter step and two data links connected to same input, flattened merge behavior

        Generated from::

            id: 29
            job: tests/count-lines6-job.json
            label: wf_wc_scatter_multiple_flattened
            output:
              count_output: 34
            tags:
            - multiple_input
            - inline_javascript
            - workflow
            tool: tests/count-lines7-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.2""", """Test single step workflow with Scatter step and two data links connected to same input, flattened merge behavior""")

    def test_conformance_v1_2_wf_wc_nomultiple(self):
        """Test when step source is a single-item list and there is no linkMerge, then it not wrapped in a list, and that MultipleInputFeatureRequirement is not required.

        Generated from::

            id: 30
            job: tests/count-lines4-job.json
            label: wf_wc_nomultiple
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines13-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.2""", """Test when step source is a single-item list and there is no linkMerge, then it not wrapped in a list, and that MultipleInputFeatureRequirement is not required.""")

    def test_conformance_v1_2_wf_wc_nomultiple(self):
        """Test when step source is a single-item list and linkMerge is listed, then it is wrapped in a list.

        Generated from::

            id: count-lines19-wf
            job: tests/count-lines4-job.json
            label: wf_wc_nomultiple
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines19-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.2""", """Test when step source is a single-item list and linkMerge is listed, then it is wrapped in a list.""")

    def test_conformance_v1_2_wf_input_default_missing(self):
        """Test workflow with default value for input parameter (missing)

        Generated from::

            id: 31
            job: tests/empty.json
            label: wf_input_default_missing
            output:
              count_output: 1
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines5-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.2""", """Test workflow with default value for input parameter (missing)""")

    def test_conformance_v1_2_wf_input_default_provided(self):
        """Test workflow with default value for input parameter (provided)

        Generated from::

            id: 32
            job: tests/wc-job.json
            label: wf_input_default_provided
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines5-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.2""", """Test workflow with default value for input parameter (provided)""")

    def test_conformance_v1_2_wf_scatter_emptylist(self):
        """Test workflow scatter with single empty list parameter

        Generated from::

            id: 39
            job: tests/scatter-empty-job1.json
            label: wf_scatter_emptylist
            output:
              out: []
            tags:
            - scatter
            - workflow
            tool: tests/scatter-wf1.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.2""", """Test workflow scatter with single empty list parameter""")

    def test_conformance_v1_2_wf_scatter_dotproduct_twoempty(self):
        """Test workflow scatter with two empty scatter parameters and dotproduct join method

        Generated from::

            id: 43
            job: tests/scatter-empty-job4.json
            label: wf_scatter_dotproduct_twoempty
            output:
              out: []
            tags:
            - scatter
            - workflow
            tool: tests/scatter-wf4.cwl#main
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.2""", """Test workflow scatter with two empty scatter parameters and dotproduct join method""")

    def test_conformance_v1_2_step_input_default_value_nosource(self):
        """Test use default value on step input parameter with empty source

        Generated from::

            id: 50
            job: tests/empty.json
            label: step_input_default_value_nosource
            output:
              count_output: 16
            tags:
            - inline_javascript
            - workflow
            tool: tests/count-lines11-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.2""", """Test use default value on step input parameter with empty source""")

    def test_conformance_v1_2_wf_two_inputfiles_namecollision(self):
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
        self.cwl_populator.run_conformance_test("""v1.2""", """Test workflow two input files with same name.""")

    def test_conformance_v1_2_directory_output(self):
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
        self.cwl_populator.run_conformance_test("""v1.2""", """Test directory output""")

    def test_conformance_v1_2_wf_compound_doc(self):
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
        self.cwl_populator.run_conformance_test("""v1.2""", """Test compound workflow document""")

    def test_conformance_v1_2_wf_step_connect_undeclared_param(self):
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
        self.cwl_populator.run_conformance_test("""v1.2""", """Test that it is not an error to connect a parameter to a workflow step, even if the parameter doesn't appear in the `run` process inputs.""")

    def test_conformance_v1_2_workflow_union_default_input_unspecified(self):
        """Test union type input to workflow with default unspecified

        Generated from::

            id: 167
            job: tests/empty.json
            label: workflow_union_default_input_unspecified
            output:
              o: the default value
            tags:
            - workflow
            - inline_javascript
            - expression_tool
            tool: tests/io-union-input-default-wf.cwl
        """  # noqa: W293
        self.cwl_populator.run_conformance_test("""v1.2""", """Test union type input to workflow with default unspecified""")
