"""Manage the files in this directory."""
import os
import urllib2

SCHEMAS_URL = "https://raw.githubusercontent.com/common-workflow-language/common-workflow-language/master/"

CWL_FILES = {
    "v1.0": [
        "cat-job.json",
        "cat3-tool.cwl",
        "hello.txt",
    ]
}


for version in CWL_FILES.keys():
    for cwl_file in CWL_FILES[version]:
        url = SCHEMAS_URL + ("%s/%s/%s" % (version, version, cwl_file))
        response = urllib2.urlopen(url)
        directory = version.replace("-", "")
        if not os.path.exists(directory):
            os.makedirs(directory)
        open("%s/%s" % (directory, cwl_file), "w").write(response.read())
