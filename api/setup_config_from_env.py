#!/usr/bin/env python3
from os import environ
import json
import glom

SAMPLE_CONFIG_FILE = "config.json_SAMPLE"
CONFIG_FILE = "config.json"

BAD_CONFIG_MSG = "uh oh, config vars not set, check heroku settings"
assert environ.get("api_key", None) is not None, BAD_CONFIG_MSG
assert environ.get("spreadsheet_id", None) is not None, BAD_CONFIG_MSG
assert environ.get("spreadsheet_range", None) is not None, BAD_CONFIG_MSG
assert environ.get("client_id", None) is not None, BAD_CONFIG_MSG
assert environ.get("project_id", None) is not None, BAD_CONFIG_MSG
assert environ.get("client_secret", None) is not None, BAD_CONFIG_MSG


# This dictionary should look exactly like the `SAMPLE_CONFIG_FILE`
config = {
    "api_key": environ.get("api_key", None),
    "spreadsheet_id": environ.get("spreadsheet_id", None),
    "spreadsheet_range": environ.get("spreadsheet_range", None),
    "installed": {
        "client_id": environ.get("client_id", None),
        "project_id": environ.get("project_id", None),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_secret": environ.get("client_secret", None),
        "redirect_uris": ["urn:ietf:wg:oauth:2.0:oob", "http://localhost"],
    },
}


with open(CONFIG_FILE, "w") as json_file:
    json.dump(config, json_file)
