#!/usr/bin/env python3

import json
from datetime import datetime
from utils import execute_sql


def load_tweets(filename):
    with open(filename, 'r') as file:
        return [json.loads(line) for line in file]


tweets = load_tweets('three_minutes_tweets.json')


def path(data, fields):
    result = None

    for field in fields:
        if field in data and data[field] is not None and data[field] != '':
            result = data[field]
            data = data[field]
        else:
            return None

    return result


def convert_date(datetime_str):
    if datetime_str is None:
        return None
    return datetime.strptime(datetime_str, '%a %b %d %H:%M:%S %z %Y')


def parse_tweets(tweets):
    return [
        (
            path(item, ['user', 'name']),
            path(item, ['text']),
            path(item, ['place', 'country_code']),
            path(item, ['entities', 'media', 'display_url']),
            path(item, ['lang']),
            convert_date(path(item, ['created_at'])),
            path(item, ['user', 'location'])
        ) for item in tweets
    ]


cleaned_tweets = parse_tweets(tweets)

insert_query = 'INSERT INTO Text (name, tweet_text, country_code, display_url, lang, created_at, location) VALUES (?,?,?,?,?,?,?)'
execute_sql(insert_query, cleaned_tweets)
