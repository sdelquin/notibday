#!/bin/bash
# Master script.
# To be launched only in production machine.

cd "$(dirname "$0")"
source ~/.bashrc
source ~/.virtualenvs/notibday/bin/activate
exec python main.py
