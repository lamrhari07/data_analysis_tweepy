
import tweepy, time
from textblob import TextBlob


str_input = input("Enter HERE: ")

consumer_key = 'p2bh13NnicTppGvr8jhcvqjY2'
consumer_secret = 'hDaHufKh2l4NkAhfZfyz0bYLsqnKJQW3fnInPkxoVqMo4jaCGu'

access_token = '971936335-wXGV3GDS2bYV69vK4yqmW1ApKQYNtpktTJuUnhht'
access_token_secret = 'UU278HqoBdf8NDe1y6BIWwxYhiUZOjvpG2R9xux1j4Mte'


auth = tweepy.OAuthHandler (consumer_key, consumer_secret)
auth.set_access_token (access_token, access_token_secret)

api = tweepy.API (auth)
public_tweets = api.search('%s' % str_input)

for tweet in public_tweets:
    print(str(tweet.text).encode(encoding='UTF-8'))
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)

time.sleep(100)

