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



    # say something when loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Update loop cog loaded!")
        self.update_loop.start()
        # self.test_loop.start()
    
    @tasks.loop(seconds=60)
    async def test_loop(self):
        guilds = await self.db.get_guilds()
        for guild in guilds:
            channel = await self.db.get_channel(guild)
            send_channel = self.bot.get_channel(channel)
            artists = await self.db.get_twitter_list(guild)
            print("Checking for new art")
            embed = discord.Embed(title="twitter link", color=0x00ff00)
            embed.description = "likes: "
            await send_channel.send(embed=embed)


    # prob have to get channel id from db? idk AHHHs

    # during execution of this loop, commands will not be processed.
    @tasks.loop(minutes=10)
    async def update_loop(self):
        guilds = await self.db.get_guilds()
        for guild in guilds:
            channel = await self.db.get_channel(guild)
            send_channel = self.bot.get_channel(channel)
            artists = await self.db.get_twitter_list(guild)
            print("Checking for new art")
            # todo: remove print statements and update last tweet id in db
            for artist in artists:
                last_work = await self.db.get_last_work(guild, artist)
                last_work_id = last_work["last_tweet_id"]
                new_work = await self.twitter_main.get_art(artist, last_work_id) #
                #return_image, return_url, return_favourite_count, str(tweet.id), date_posted
                # print("artist: " + artist)
                # print("new work: " + str(new_work))
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

def setup(bot):
    bot.add_cog(check_updates(bot))
