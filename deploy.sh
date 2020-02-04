#!/bin/bash
gunicorn api:app --config=gunicorn_config.py
