from config import *
import pandas as pd
import tweepy
import datetime


# Get tweet function, keyword input, related tweets database output
def get_tweets(keyword):
    auth = tweepy.OAuthHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET)
    auth.set_access_token(TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)

    # Collected tweet date period
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)

    # Tweet collection
    tweets_list = tweepy.Cursor(api.search, q=keyword + str(yesterday) + " until:" + str(today), tweet_mode='extended',
                                lang='en').items()

    # convert the raw data into a variable
    output = []
    for tweet in tweets_list:
        text = tweet._json["full_text"]
        print(text)
        favourite_count = tweet.favorite_count
        retweet_count = tweet.retweet_count
        created_at = tweet.created_at

        line = {'text': text, 'favourite_count': favourite_count, 'retweet_count': retweet_count,
                'created_at': created_at}
        output.append(line)

    return pd.DataFrame(output)
