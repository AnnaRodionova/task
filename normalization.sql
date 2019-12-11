CREATE TABLE Texts
(
    id              int NOT NULL AUTO_INCREMENT,
    name            varchar(255),
    tweet_text      varchar(255),
    country_code    varchar(255),
    display_url     varchar(255),
    lang            varchar(255),
    created_at      datetime,
    location        varchar(255),
    tweet_sentiment int,
    PRIMARY KEY (id)
);


CREATE TABLE Users
(
    id       int NOT NULL AUTO_INCREMENT,
    name     varchar(255),
    location varchar(255),
    PRIMARY KEY (id)
);


INSERT INTO Users (name, location)
SELECT name, location
FROM Texts;


CREATE TABLE Tweets
(
    id              int NOT NULL AUTO_INCREMENT,
    tweet_text      varchar(255),
    country_code    varchar(255),
    display_url     varchar(255),
    lang            varchar(255),
    created_at      datetime,
    location        varchar(255),
    tweet_sentiment int,
    user_id         int,
    PRIMARY KEY (id),
    FOREIGN KEY (user_id) REFERENCES Users (id)
);

INSERT INTO Tweets (tweet_text, country_code, display_url, lang, created_at, location, tweet_sentiment, user_id)
SELECT t1.tweet_text,
       t1.country_code,
       t1.display_url,
       t1.lang,
       t1.created_at,
       t1.location,
       t1.tweet_sentiment,
       t2.id
FROM Texts AS t1,
     Users as t2
WHERE t1.id = t2.id;