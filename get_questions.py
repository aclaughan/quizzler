#!/usr/local/bin/python3
# ------------------------------------------------------------------------------
#        name : get_questions.py
#      author : alan claughan
#     version : 1.0.0
#        date : 21-04-2021
# description : pulls int(amount) questions from the open test database.
#             : each result looks as follows
#   {
#     "category": CATEGORY,
#     "type": BOOLEAN,
#     "difficulty": DIFFICULTY,
#     "question": QUESTION,
#     "correct_answer": ANSWER,
#     "incorrect_answers": [
#       INCORRECT_ANSWER
#     ]
#   },
#
# ==============================================================================
#

import json
import logging
from urllib.parse import urlencode

import requests as requests

# logging.basicConfig(level=logging.INFO)

OTDB_URL = "https://opentdb.com/api.php"


def get_questions(amount: int) -> list:
    endpoint = OTDB_URL
    params = \
        {
            "amount": amount,
            "type": "boolean"
        }
    url_params = urlencode(params)
    url = f"{endpoint}?{url_params}"

    logging.info(url)

    response = requests.get(url)
    json_data = response.json()

    return json_data['results']


if __name__ == '__main__':
    print(json.dumps(get_questions(10), indent=2))
