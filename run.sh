#!/bin/bash
# Master script.

source ~/.pyenv/versions/notibday/bin/activate
cd "$(dirname "$0")"
exec python main.py $1
