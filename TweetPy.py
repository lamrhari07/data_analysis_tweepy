
import tweepy, time
from textblob import TextBlob


str_input = input("Enter HERE: ")

consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''


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

