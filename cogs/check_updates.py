# This example demonstrates a standalone cog file with the bot instance in a separate file.

import discord
from discord.ext import commands, tasks
from discord import option
from discord.ui import View, button
from utils.test import Test
from discord.commands import SlashCommandGroup
from utils.firestoreDB import FirestoreDB
from bot_test import get_tweets

class check_updates(commands.Cog):
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
    @tasks.loop(seconds=60)
    async def update_loop(self):
        guilds = await self.db.get_guilds()
        for guild in guilds:
            channel = await self.db.get_channel(guild)
            send_channel = self.bot.get_channel(channel)
            artists = await self.db.get_twitter_list(guild)
            print("Checking for new art")
            for artist in artists:
                last_work = await self.db.get_last_work(guild, artist)
                last_work_id = last_work["last_tweet_id"]
                new_work = await self.twitter_main.get_art(artist, last_work_id)
                if new_work is not None:
                    img = new_work[0]
                    embed = discord.Embed(title="twitter link", url=new_work[1], color=0x00ff00)
                    embed.description = "likes: " + str(new_work[2])
                    embed.set_image(url=img) # Set the image URL of the embed
                    try:
                        await send_channel.send(embed=embed)
                    except:
                        print("error sending embed(likely bot not setuped)")
    # async def update_loop(self):
    #     guilds = await self.db.get_guilds()
    #     for guild in guilds:
    #         channel = self.db.get_channel(guild)
    #         artists = await self.db.get_twitter_list(guild)
    #         await channel.send("Checking for new art")
    #         for artist in artists:
    #             last_work = await self.db.get_last_work(guild, artist)
    #             last_work_id = last_work["last_tweet_id"]
    #             new_work = await self.twitter_main.get_art(artist, last_work_id)
    #             if new_work != None:
    #                 # send_channel = self.bot.get_channel(channel)
    #                 img = new_work[0]
    #                 embed = discord.Embed(title="twitter link",url=new_work[1], color=0x00ff00)
    #                 embed.description = "likes: "+ str(new_work[2])
    #                 await channel.send(embed=embed)
    #                 await channel.send(new_work[0])


                
    # send a msg to the channel every 60 seconds


def setup(bot):
    bot.add_cog(check_updates(bot))


# The basic bot instance in a separate file should look something like this:
# bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))
# bot.load_extension("slash_cog")
# bot.run("TOKEN")