import tweepy

consumer_key = "" #please enter you twitter account details here
consumer_secret = ""
access_key = ""
access_secret = ""


def get_tweets(username):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth)
    tweets = api.user_timeline(screen_name=username)
    tmp = []
    tweets_for_csv = [tweet.text for tweet in tweets]
    for j in tweets_for_csv:
        tmp.append(j)
    print(tmp)
if __name__ == '__main__':
    get_tweets("twitter-handle")