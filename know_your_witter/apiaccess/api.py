import tweepy
import os, logging


def get_tweets(user_name):
    logging.info("Connecting to twitter API")
    auth = tweepy.OAuthHandler(os.getenv("TWITTER_CONSUMER_KEY"), os.getenv("TWITTER_CONSUMER_SECRET"))
    api = tweepy.API(auth, wait_on_rate_limit=True)
    logging.info( "Collecting tweets")
    tweets_list = api.user_timeline(screen_name=user_name, exclude_replies=True, count=100)
    output = []
    for tweet in tweets_list:
        output.append(tweet._json["text"])
    return output
