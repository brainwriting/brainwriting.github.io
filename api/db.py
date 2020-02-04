#!/usr/bin/env python3
"""A module to talk to the brainwriting.github.io database

The database is Google Sheets.

There exists a table `ALL_DATA` that looks like this:

Index:       0             1          2                 3               4

|   |        A        |    B   |      C       |         D         |     E     |
|---|-----------------|--------|--------------|-------------------|-----------|
|`1`|     username    |  idea  | topic_name   | topic_description | published |
|`2`| Bob             | idea_1 | TOPIC_NAME   | TOPIC_DESC        | FALSE     |
|`3`| anonymous_panda | idea_2 | TOPIC_NAME_2 | TOPIC_DESC        | FALSE     |


The Pandas representation looks like this:
```
                 0       1             2                  3          4
0         username    idea    topic_name  topic_description  published
1              Bob  idea_1    TOPIC_NAME         TOPIC_DESC      FALSE
2  anonymous_panda  idea_2  TOPIC_NAME_2         TOPIC_DESC      FALSE
```
"""
import json
import os.path
import pickle
from typing import List

import pandas as pd
from pandas import DataFrame
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ["https://www.googleapis.com/auth/spreadsheets.readonly"]

with open("config.json", "r") as json_file:
    config = json.load(json_file)

# The ID and range of a sample spreadsheet.
SPREADSHEET_ID = config["spreadsheet_id"]
SPREADSHEET_RANGE = config["spreadsheet_range"]
TOPIC_NAME_COLUMN = "topic_name"
IDEAS_COLUMN = "idea"
DESC_COLUMN = "topic_description"

# Build a Google Sheets API v4 service object thing
service = build("sheets", "v4", developerKey=config["api_key"])


def get_sheet_as_pandas() -> DataFrame:
    """Returns a Pandas DataFrame of the whole spreadsheet"""
    result = (
        service.spreadsheets()
        .values()
        .get(spreadsheetId=SPREADSHEET_ID, range=SPREADSHEET_RANGE)
        .execute()
    )
    rows = result.get("values", [])
    df = DataFrame(rows)
    new_header = df.iloc[0]  # grab the first row for the header
    df = df[1:]  # take the data less the header row
    df.columns = new_header  # set the header row as the df header
    return df


def get_unique_topics(sheet_df: DataFrame) -> dict:
    return sheet_df[TOPIC_NAME_COLUMN].unique()


def get_ideas_for_topic(sheet_df: DataFrame, topic: str) -> List[str]:
    return sheet_df[sheet_df[TOPIC_NAME_COLUMN] == topic][IDEAS_COLUMN].tolist()


def get_description_for_topic(sheet_df: DataFrame, topic: str) -> str:
    return sheet_df[sheet_df[TOPIC_NAME_COLUMN] == topic][DESC_COLUMN].iloc[0]


def get_topic_dict(sheet_df: DataFrame, topic_list: List[str]) -> dict:
    """
    {
        "TOPIC_NAME": {
            "description": "DESC",
            "ideas": ["idea_1", ...]
        },
        "TOPIC_NAME_2: {...}
    }
    """
    result = {}
    for t in topic_list:
        result[t] = {
            "description": get_description_for_topic(sheet_df=sheet_df, topic=t),
            "ideas": get_ideas_for_topic(sheet_df=sheet_df, topic=t)
        }
    return result


def get_all_data():
    df = get_sheet_as_pandas()
    lst = get_unique_topics(sheet_df=df)
    return get_topic_dict(sheet_df=df, topic_list=lst)

if __name__ == "__main__":
    print("hello world")
