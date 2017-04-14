#!/bin/bash
# Master script.

cd "$(dirname "$0")"
source ~/.bashrc
source ~/.virtualenvs/notibday/bin/activate
exec python main.py
