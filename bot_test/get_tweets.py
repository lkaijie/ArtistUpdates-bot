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
        

    async def get_art(self,user_id, last_tweet_id):
        
        # Get User's Tweets

        # This endpoint/method returns Tweets composed by a single user, specified by
        # the requested user ID

        # user_id = "askziye"

        # response = client.get_users_tweets(user_id,max_results=1)

        response = self.api.user_timeline(screen_name=user_id, count=30, exclude_replies=True, include_rts=False)
        print("------------------------------------------------------------------")
        print("------------------------------------------------------------------")
        if response == []:
            print("No tweets")
            return None
        # exclude_replies
        # |exclude_replies|
        # include_rts

        # use stream lsitener instead

        # By default, only the ID and text fields of each Tweet will be returned
        directory = "imgs/"

        return_image = ""
        return_url = ""
        return_favourite_count = 0
        for tweet in response: # TODO: make it check from the last tweet instead, so -1 or something, so if multiple tweets it can still work )
            if str(tweet.id) == last_tweet_id:
                print("No new tweet")
                return None
            print(last_tweet_id)
            print("-------------------")
            print(tweet.id)
            print("-------------------")
            print(str(tweet.id) == last_tweet_id)
            # print(tweet.text)
            # get likes
            return_favourite_count = tweet.favorite_count

            
            # Check if the tweet has any images
            if 'media' in tweet.entities:
                if tweet.id == last_tweet_id:
                    print("No new tweet")
                    return None
                for index, image in enumerate(tweet.entities['media']):
                    # Print the image URL
                    print(image['media_url'])
                    return_image = image['media_url']
                    # Retrieve the image data using the requests library
                    # Save the image data to a file
    
                    # Print the path to the saved file
                print(f"Original tweet URL: https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
                return_url = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"

            
                return return_image, return_url, return_favourite_count, tweet.id
            else:
                return None

    # async def get_art(self,user_id, last_tweet_id):
        
    #     # Get User's Tweets

    #     # This endpoint/method returns Tweets composed by a single user, specified by
    #     # the requested user ID

    #     # user_id = "askziye"

    #     # response = client.get_users_tweets(user_id,max_results=1)

    #     response = self.api.user_timeline(screen_name=user_id, count=30, exclude_replies=True, include_rts=False)
    #     # exclude_replies
    #     # |exclude_replies|
    #     # include_rts

    #     # use stream lsitener instead

    #     # By default, only the ID and text fields of each Tweet will be returned
    #     directory = "imgs/"

    #     return_image = ""
    #     return_url = ""
    #     return_favourite_count = 0
    #     for tweet in response:
    #         if str(tweet.id) == last_tweet_id:
    #             print("No new tweet")
    #             return None
    #         print(last_tweet_id)
    #         print("-------------------")
    #         print(tweet.id)
    #         print("-------------------")
    #         print(str(tweet.id) == last_tweet_id)
    #         # print(tweet.text)
    #         # get likes
    #         return_favourite_count = tweet.favorite_count

            
    #         # Check if the tweet has any images
    #         if 'media' in tweet.entities:
    #             if tweet.id == last_tweet_id:
    #                 print("No new tweet")
    #                 return None
    #             for index, image in enumerate(tweet.entities['media']):
    #                 # Print the image URL
    #                 print(image['media_url'])
    #                 return_image = image['media_url']
    #                 # Retrieve the image data using the requests library
    #                 image_data = urllib.request.urlopen(image['media_url']).read()
    #                 # Save the image data to a file
    #                 filename = f"{tweet.id}_image{index+1}.jpg"
    #                 with open(directory + filename, 'wb') as f:
    #                     f.write(image_data)
    #                 # Print the path to the saved file
    #                 print(f"Saved image to {os.path.abspath(directory + filename)}")
    #             print(f"Original tweet URL: https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}")
    #             return_url = f"https://twitter.com/{tweet.user.screen_name}/status/{tweet.id}"
    #             break
            
    #     return return_image, return_url, return_favourite_count, tweet.id

# ")
