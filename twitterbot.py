import time
import tweepy
import random #EEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE
import os
from dotenv import load_dotenv
load_dotenv()

# spooky...
os.getenv("api_key")
api_key = os.getenv("api_key")
api_secret_key = os.getenv("api_secret_key")
access_key = os.getenv("access_key")
access_secret_key = os.getenv("access_secret_key")

auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_key, access_secret_key)
api = tweepy.API(auth)

lyrics = open("lyrics.txt", "r", encoding='utf-8')

lines = lyrics.read().splitlines()

while True:
    random_line = random.choice(lines)
    if len(random_line) <= 280: # in case a lyric is too long...
        tweet_text = random_line.replace("|", '\n').lower() # |'s are now linebreaks. lowercases it too
        api.update_status(status=tweet_text) # actually tweets!
        time.sleep(60*60) # waits 60 min
