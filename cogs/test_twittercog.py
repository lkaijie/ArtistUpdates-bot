import discord
from discord.ext import commands, tasks
import tweepy
import config
# from chat gpt, just a placeholder/test
class TwitterCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tracked_users = ["user1", "user2"] # list of Twitter usernames to track
        self.last_tweet_ids = {user: None for user in self.tracked_users} # dictionary to store the last tweet ID for each user

    @tasks.loop(seconds=60)
    async def check_tweets(self):
        auth = tweepy.OAuthHandler(config.API_Key, config.API_Key_Secret)
        auth.set_access_token(config.Access_Token, config.Access_Token_Secret)
        api = tweepy.API(auth)
        for user in self.tracked_users:
            try:
                tweets = api.user_timeline(screen_name=user, count=1)
            except tweepy.TweepError as e:
                print(e)
                continue
            if len(tweets) > 0 and 'media' in tweets[0].entities:
                if tweets[0].id != self.last_tweet_ids[user]:
                    self.last_tweet_ids[user] = tweets[0].id
                    tweet_url = f"https://twitter.com/{user}/status/{tweets[0].id}"
                    embed = discord.Embed(title=f"New tweet by {user}!", url=tweet_url)
                    embed.set_image(url=tweets[0].entities['media'][0]['media_url'])
                    await self.bot.channel.send(embed=embed)

    @check_tweets.before_loop
    async def before_check_tweets(self):
        await self.bot.wait_until_ready()

    @commands.command()
    async def start_tracking(self, ctx):
        self.check_tweets.start()
        await ctx.send("Started tracking Twitter.")

    @commands.command()
    async def stop_tracking(self, ctx):
        self.check_tweets.stop()
        await ctx.send("Stopped tracking Twitter.")
