#!/bin/bash
# Master script.

source ~/.virtualenvs/notibday/bin/activate
cd "$(dirname "$0")"
exec python main.py $1
