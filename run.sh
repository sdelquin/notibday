#!/bin/bash
# Master script.
# To be launched only in production machine.

function get_config {
    cat config.py | grep $1 | cut -d '"' -f 4    
}

VENV=$(get_config VENV)
PROJ=$(get_config PROJ)
BASH=$(get_config BASH)

source $BASH
source "$VENV/bin/activate"
exec python "$PROJ/main.py"
