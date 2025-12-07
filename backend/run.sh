#!/usr/bin/env bash
# quick run script for development
export PYTHONPATH="${PYTHONPATH}:./"
uvicorn main:app --reload --host 0.0.0.0 --port 8000

