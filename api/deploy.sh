#!/bin/bash

pip install -r ../requirements.txt

gunicorn api:app --config=gunicorn_config.py
