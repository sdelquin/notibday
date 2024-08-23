#!/bin/bash
# Master script.

cd "$(dirname "$0")"
source .venv/bin/activate
exec python main.py $1
