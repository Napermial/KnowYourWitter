import twitter


def connect_to_api(func):
    def wrapper(*args, **kwargs):
        # api = twitter.Api(consumer_key='',
        #          consumer_secret='',
        #          access_token_key='',
        #          access_token_secret='')
        api = twitter.NoAuth()
        func(api, *args, **kwargs)

    return wrapper()


@connect_to_api
def get_tweets_of_user(api, user):
    user = api.GetUserTimeline(user)
    return user.get_tweets()


@connect_to_api
def validate_username(api, username):
    try:
        api.get_user(username)
        return True
    except:
        ValueError


def main():
    validate_username(username="a")
    get_tweets_of_user(user="a")


if __name__ == '__main__':
    main()
