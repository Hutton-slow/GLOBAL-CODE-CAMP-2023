import tweepy

consumer_key = "i4p8wpnT5d7m5lw4s8WtJDpVE"
consumer_secret = "LBgfRQYkvl23td76mj0t2pbrGdumw8xVpyDfxod7OnhObIjmVi"
access_token =  "1032251174207057921-JfenHQY5Zkz6y6X1qMihzEB4lmmgU4"
access_token_secret = "WzXqocvDAHYBvGDws31uFC3tiLn9UrwlQW4sfx9JXKhBE"
bearer_token ="AAAAAAAAAAAAAAAAAAAAAGdPpgEAAAAAtE6fE8%2Fbov%2B%2BtasSLHFbdls8jLk%3DYr1yrJG85H6oeIQOrIrGC3boWRop0WUUwz0bi1dUOduja9u9zk"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret
)

auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

user = api.get_user(screen_name = "DodziZormelo")
trends = api.available_trends()

print(user)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)