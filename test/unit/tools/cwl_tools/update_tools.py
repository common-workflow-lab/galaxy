"""Manage the files in this directory."""
import os
import urllib2

SCHEMAS_URL = "https://raw.githubusercontent.com/common-workflow-language/common-workflow-language/master/"

CWL_FILES = {
    "draft-3": [
        "args.py",
        "bwa-mem-tool.cwl",
        "cat-job.json",
        "cat1-tool.cwl",
        "cat3-tool.cwl",
        "cat2-tool.cwl",
        "cat4-tool.cwl",
        "cat-n-job.json",
        "count-lines1-wf.cwl",
        "count-lines2-wf.cwl",
        "empty.json",
        "env-tool1.cwl",
        "env-tool2.cwl",
        "env-job.json",
        "hello.txt",
        "index.py",
        "optional-output.cwl",
        "number.txt",
        "null-expression1-job.json",
        "null-expression2-job.json",
        "null-expression1-tool.cwl",
        "null-expression2-tool.cwl",
        "params.cwl",
        "params2.cwl",
        "params_inc.yml",
        "parseInt-job.json",
        "parseInt-tool.cwl",
        "rename.cwl",
        "rename-job.json",
        "sorttool.cwl",
        "wc-tool.cwl",
        "wc2-tool.cwl",
        "wc3-tool.cwl",
        "wc4-tool.cwl",
        "wc-job.json",
        "whale.txt",
    ],
    "v1.0": [
        "cat-job.json",
        "cat3-tool.cwl",
        "count-lines1-wf.cwl",
        "count-lines2-wf.cwl",
        "count-lines3-job.json",  # needs whale.txt and hello.txt
        "count-lines3-wf.cwl",  # ScatterFeatureRequirement - File[] -> int[]
        "count-lines4-job.json",
        "count-lines4-wf.cwl",  # ScatterFeatureRequirement, MultipleInputFeatureRequirement (File, File) -> int[]
        "count-lines5-wf.cwl",  # default input file :(
        "default_path.cwl",
        "hello.txt",
        "parseInt-tool.cwl",
        "record-output-job.json",
        "record-output.cwl",  # record inputs and outputs
        "ref.fasta",  # Used by record-output-job.json...
        "scatter-job1.json",
        "scatter-job2.json",
        "scatter-wf1.cwl",  # ScatterFeatureRequirement - string[] -> string[]
        "scatter-wf2.cwl",  # ScatterFeatureRequirement, scatterMethod: nested_crossproduct
        "scatter-wf3.cwl",  # ScatterFreatureRequirement, scatterMethod: flat_crossproduct , $graph
        "scatter-wf4.cwl",  # ScatterFreatureRequirement, scatterMethod: dotproduct , $graph
        "wc-tool.cwl",
        "wc2-tool.cwl",
        "wc3-tool.cwl",
        "wc4-tool.cwl",
        "wc-job.json",
        "whale.txt",
    ]
}

# TODO: v1/
#     scatter stuff: wc2-tool.cwl, wc3-tool.cwl, wc4-tool.cwl, count-lines3-wf.cwl, count-lines4-wf.cwl, count-lines5-wf.cwl
#     record stuff:  record-output.cwl


for version in CWL_FILES.keys():
    directory = version.replace("-", "")
    if not os.path.exists(directory):
        os.makedirs(directory)

    url = SCHEMAS_URL + ("%s/conformance_test_%s.yaml" % (version, version))
    response = urllib2.urlopen(url)
    open("%s/%s" % (directory, "conformance_tests.yaml"), "w").write(response.read())

    for cwl_file in CWL_FILES[version]:
        url = SCHEMAS_URL + ("%s/%s/%s" % (version, version, cwl_file))
        response = urllib2.urlopen(url)
        open("%s/%s" % (directory, cwl_file), "w").write(response.read())
