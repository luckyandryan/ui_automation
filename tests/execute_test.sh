#!/bin/sh

export PYTHONPATH=$(pwd)

pytest tests/ --capture=tee-sys --verbose