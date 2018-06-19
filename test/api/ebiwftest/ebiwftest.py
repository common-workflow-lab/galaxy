
"""Test CWL conformance for version $version."""

from ..test_workflows_cwl import BaseCwlWorklfowTestCase


class CwlConformanceTestCase(BaseCwlWorklfowTestCase):
    """Test case mapping to CWL conformance tests for version $version."""

    def test_conformance_v1_0_17(self):
        """Test command execution in with stdin and stdout redirection

        Generated from::

            job: v1.0/wc-job.json
            output:
              output:
                checksum: sha1$3596ea087bfdaf52380eae441077572ed289d657
                class: File
                location: output
                size: 3
            tool: v1.0/wc-tool.cwl
        """
        self.cwl_populator.run_conformance_test("""v1.0""", """Test command execution in with stdin and stdout redirection""")
