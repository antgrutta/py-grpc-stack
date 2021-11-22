#!/usr/bin/env bash

# Run service
source .venv/bin/activate
export PYTHONPATH=./service:./messages:$PYTHONPATH
.venv/bin/python app.py
