#!/usr/bin/env cwl-runner
$namespaces:
  gx: "http://galaxyproject.org/cwl#"
cwlVersion: v1.0
class: CommandLineTool
id: "seqtk_seq"
gx:version: '1.2'
doc: |
    Convert to FASTA (seqtk)
inputs:
  - id: input1
    type: File
    inputBinding:
      position: 1
outputs:
  - id: output1
    type: File
    outputBinding:
      glob: out
baseCommand: ["cat"]
arguments: []
stdout: out
hints:
  gx:interface:
    inputs:
      - name: input1
        type: data
        format: txt
    outputs:
      output1:
        format: txt
  SoftwareRequirement:
    packages:
    - package: seqtk
      version:
      - "1.2"
