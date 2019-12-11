#!/usr/bin/env python3

import re
from sqlalchemy import select

from connection import text_table, engine
from utils import execute_sql

filenameAFINN = 'AFINN-111.txt'
afinn = dict(map(lambda w: (w[0], int(w[1])), [ws.strip().split('\t') for ws in open(filenameAFINN)]))

pattern_split = re.compile(r"\W+")


def get_sentiment(text):
    if text is None:
        return None

    words = pattern_split.split(text.lower())

    sentiments = list(map(lambda word: afinn.get(word, 0), words))
    avg_sentiment = sum(sentiments) / len(list(sentiments))

    return avg_sentiment


select_query = select([text_table.c.id, text_table.c.tweet_text]).order_by(text_table.c.id)

with engine.connect() as connection:
    try:
        query_result = connection.execute(select_query)
        tweet_sent = [(get_sentiment(text), identifier) for identifier, text in query_result]
    except Exception as e:
        print(e)

update_query = 'UPDATE Text SET tweet_sentiment=? WHERE id=?'
execute_sql(update_query, tweet_sent)
