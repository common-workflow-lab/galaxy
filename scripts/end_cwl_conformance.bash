#!/bin/bash

set +x

: ${GALAXY_BOOTSTRAP_DATABASE:=1}

if [ $GALAXY_BOOTSTRAP_DATABASE -eq 1 ]; then
  docker stop "${GALAXY_BOOTSTRAP_DATABASE_CONTAINER}" || /bin/true
  docker rm "${GALAXY_BOOTSTRAP_DATABASE_CONTAINER}" || /bin/true
fi

export GALAXY_SKIP_CLIENT_BUILD=1
export GALAXY_PID=cwl.pid
./run.sh --stop-daemon
