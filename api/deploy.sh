#!/bin/bash

pip3 install -r ../requirements.txt


./setup_config_from_env.py


gunicorn api:app --config=gunicorn_config.py
