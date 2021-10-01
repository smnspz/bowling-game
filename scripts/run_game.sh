#!/bin/bash
set -u
SCRIPT_NAME=$( basename $0 )
SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd )"
PRJ_DIR="$( cd "${SCRIPT_DIR}/.." && pwd )"
PRJ_NAME=$( basename ${PRJ_DIR} )

poetry run python bowling_game/main.py