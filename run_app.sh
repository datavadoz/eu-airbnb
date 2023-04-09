#!/bin/bash
set -eo pipefail

ME=$(readlink -f "${BASH_SOURCE:-$0}")
PROJECT_DIR=$(dirname $ME)

source ${PROJECT_DIR}/sourceme.sh
mage start ${PROJECT_DIR}/airbnb
