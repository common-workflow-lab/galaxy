#!/bin/bash

VERSIONS="1.1
1.2"

for version in $VERSIONS; do
    wget "https://github.com/common-workflow-language/cwl-v$version/archive/main.zip"
    unzip main.zip
    ls "cwl-v$version-main"
    mkdir "v$version"
    cp "cwl-v$version-main"/conformance_tests.yaml "v$version"
    cp -r "cwl-v$version-main"/tests "v$version"/tests
    rm -rf "cwl-v$version-main"
    rm -rf main.zip
done
