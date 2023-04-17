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
                print("artist: " + artist)
                print("new work: " + str(new_work))
                if new_work is not None and new_work != [] and new_work != "No new tweet":
                    img = new_work[0]
                    await self.db.update_last_tweet_id(guild, artist, str(new_work[3])) # new work3 is the tweet id
                    embed = discord.Embed(title="twitter link", url=new_work[1], color=0x00ff00)
                    embed.description = "likes: " + str(new_work[2])
                    embed.set_image(url=img) # Set the image URL of the embed
                    embed.set_footer(text="Art by: " + artist)
                    try:
                        pfp_url = last_work["profile_pic"]
                    except:
                        pfp_url = "https://em-content.zobj.net/thumbs/120/google/350/umbrella-with-rain-drops_2614.png"
                    embed.set_author(name="New art from " + artist, url=new_work[1], icon_url=pfp_url)
                    # embed.set_thumbnail(url="https://pbs.twimg.com/profile_images/1410000")
                    # embed.set_thumbnail(url=f"https://twitter.com/{artist}/photo")
                    try:
                        await send_channel.send(embed=embed)
                    except Exception as e:
                        print("error sending embed(likely bot not setuped)")
                        print(e)





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