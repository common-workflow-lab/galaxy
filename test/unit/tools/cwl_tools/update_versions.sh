#!/bin/sh

cd "$(dirname "$0")"

VERSIONS="1.0
1.1
1.2"
for version in $VERSIONS; do
    if [ "$version" = '1.0' ]; then
        repo_name=common-workflow-language
        conformance_filepath=v1.0/conformance_test_v1.0.yaml
        tests_dir=v1.0/v1.0
    else
        repo_name=cwl-v$version
        conformance_filepath=conformance_tests.yaml
        tests_dir=tests
    fi
    wget "https://github.com/common-workflow-language/${repo_name}/archive/main.zip"
    unzip main.zip
    mkdir -p "v${version}"
    cp "${repo_name}-main/${conformance_filepath}" "v${version}/conformance_tests.yaml"
    cp -r "$repo_name-main/${tests_dir}" "v$version"/
    rm -rf "$repo_name-main"
    rm -rf main.zip
    python conformance_to_test_cases.py "v$version"
done
