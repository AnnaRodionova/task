SELECT t1.tweet_text, t1.country_code, t1.location, t2.name 
FROM Tweets as t1, Users as t2
WHERE tweet_sentiment = 
( SELECT MAX(tweet_sentiment)
  FROM Tweets
) and t1.user_id = t2.id
UNION ALL
SELECT t1.tweet_text, t1.country_code, t1.location, t2.name 
FROM Tweets as t1, Users as t2
WHERE tweet_sentiment = 
( SELECT MIN(tweet_sentiment)
  FROM Tweets
) and t1.user_id = t2.id