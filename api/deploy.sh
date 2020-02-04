#!/bin/bash

pip3 install -r ../requirements.txt

gunicorn api:app --config=gunicorn_config.py
