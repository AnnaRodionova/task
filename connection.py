import sqlite3
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime

engine = create_engine('sqlite:///session.db', echo=True)

meta = MetaData()

text_table = Table(
    'Text', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('tweet_text', String),
    Column('country_code', String),
    Column('display_url', String),
    Column('lang', String),
    Column('created_at', DateTime),
    Column('location', String),
    Column('tweet_sentiment', Integer)
)

meta.create_all(engine)

conn = sqlite3.connect('session.db')

cur = conn.cursor()
