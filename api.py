#!/usr/bin/env python3
from flask import Flask, jsonify, request
import gunicorn_config
from flask_cors import CORS


CONFIG_FILE_PATH = 'config.json'
BAD_REQUEST = 400
SUCCESS = 200


app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello, World!', SUCCESS


if __name__ == '__main__':
    app.run(host='0.0.0.0',
            debug=gunicorn_config.DEBUG_MODE,
            port=gunicorn_config.PORT)
