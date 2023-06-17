# This example demonstrates a standalone cog file with the bot instance in a separate file.

import discord
from discord.ext import commands, tasks
from discord import option
from discord.ui import View, button
from ignore.test import Test
from discord.commands import SlashCommandGroup
from utils.firestoreDB import FirestoreDB
from utils import get_tweets

class check_updates(commands.Cog):
    '''Cog for checking for new art TODO: seperate the update loop from the bot at somepoint'''
    def __init__(self, bot):
        self.bot = bot
        # self.db = FirestoreDB()
        self.db = None
        self.twitter_main = get_tweets.Twitter_main()

    @commands.Cog.listener()
    async def on_ready(self):
        print("Update loop cog loaded!")
        self.update_loop.start()

    # during execution of this loop, commands will not be processed.
    loop_time = 10 # minutes
    @tasks.loop(minutes=loop_time)
    async def update_loop(self):
        '''Checks for new art every 10 minutes'''
        async def get_tracked_artists(guild):
            channel = await self.db.get_channel(guild)
            send_channel = self.bot.get_channel(channel)
            artists = await self.db.get_twitter_list(guild)
            return artists, send_channel
    
        guilds = await self.db.get_guilds()
        
        for guild in guilds:
            info = await get_tracked_artists(guild)
            artists = info[0]
            send_channel = info[1]
            print("Checking for new art")
            for artist in artists:
                try:
                    last_work = await self.db.get_last_work(guild, artist)
                    last_work_id = last_work["last_tweet_id"]
                    new_work = await self.twitter_main.get_art(artist, last_work_id) #
                    #return_image, return_url, return_favourite_count, str(tweet.id), date_posted
                    if new_work is not None and new_work != [] and new_work != "No new tweet":
                        img = new_work[0]
                        await self.db.update_last_tweet_id(guild, artist, str(new_work[3])) # new work3 is the tweet id
                        embed = discord.Embed(title="twitter link", url=new_work[1], color=0x00ff00)
                        embed.description = "likes: " + str(new_work[2])
                        embed.set_image(url=img) # Set the image URL of the embed
                        date_posted = new_work[4]
                        embed.set_footer(text="Date posted: " + date_posted)
                        try:
                            pfp_url = last_work["profile_pic"]
                        except:
                            pfp_url = "https://em-content.zobj.net/thumbs/120/google/350/umbrella-with-rain-drops_2614.png"
                        embed.set_author(name="New art from " + artist, url=new_work[1], icon_url=pfp_url)
                        try:
                            await send_channel.send(embed=embed)
                        except Exception as e:
                            print("error sending embed(likely bot not setuped)")
                            print(e)
                except Exception as e:
                    print("error getting new art for:", artist)
                    print(e)
                    pass

def setup(bot):
    bot.add_cog(check_updates(bot))
