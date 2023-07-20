import validators
import requests
import json
import os
import sys
import time
import datetime
import pytz
import tweepy
import urllib
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import config
# Twitter API credentials

API_Key = config.API_Key
API_Key_Secret = config.API_Key_Secret
Bearer = config.Bearer
Access_Token = config.Access_Token
Access_Token_Secret = config.Access_Token_Secret

class Twitter_main():
    def __init__(self):
        self.client = tweepy.Client(Bearer,API_Key,API_Key_Secret,Access_Token,Access_Token_Secret)
        self.auth = tweepy.OAuthHandler(API_Key, API_Key_Secret,Access_Token,Access_Token_Secret)
        self.api = tweepy.API(self.auth)
        
    async def get_last_id(self,user_id) -> str:
        '''Returns the id of the last tweet with an image, or None if there are no images in the last 30 tweets'''
        response = self.api.user_timeline(screen_name=user_id, count=30, exclude_replies=True, include_rts=False)
        for tweet in response:
            return_id = ""
            for tweet in response:
                if 'media' in tweet.entities:
                    return_id = str(tweet.id)
                    return return_id
            return None

    async def get_new_tweet(self,user_id, last_tweet_id):
        pass
        
    async def get_pfp(self, user_id):
        '''Returns the url of the profile picture'''
        pfp_url = self.api.get_user(screen_name=user_id).profile_image_url
        return pfp_url

    async def get_art(self,user_id, last_tweet_id):
        '''Returns the url of the image, the url of the tweet, the favourite count, the tweet id, and the date posted'''
        response = self.api.user_timeline(screen_name=user_id, count=30, exclude_replies=True, include_rts=False)
        if response == []:
            print("No tweets")
            return None
        directory = "imgs/"

        return_image = ""
        return_url = ""
        return_favourite_count = 0
        for tweet in response: # TODO: make it check from the last tweet instead, so -1 or something, so if multiple tweets it can still work )
            
            if str(tweet.id) == str(last_tweet_id):
                return None
            return_favourite_count = tweet.favorite_count

            # Check if the tweet has any images
            if 'media' in tweet.entities:
                if tweet.id == last_tweet_id:
                    return None
                for index, image in enumerate(tweet.entities['media']):
                    return_image = image['media_url']
                return_url = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
                date_posted = str(tweet.created_at)

                return return_image, return_url, return_favourite_count, str(tweet.id), date_posted
            
        return None