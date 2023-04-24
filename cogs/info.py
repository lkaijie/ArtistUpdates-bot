# This example demonstrates a standalone cog file with the bot instance in a separate file.

from datetime import timedelta
import datetime
import time
import discord
from discord.ext import commands
from discord import option
from discord.ui import View, button
from ignore.test import Test

startTime = time.time()

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    # say something when loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("Info cog loaded!")
    # when there are more commands add here

    @commands.slash_command(name="help",description="Displays all avaliable commands")  
    async def help(self, ctx: discord.ApplicationContext):# 0x3083e3 is the color of the embed
        embed = discord.Embed(title="AR commands", color=0xf1c232, 
            description="""
                `/info`: Displays basic information about MangaUpdates.
                `/help`: Shows this message.
                `/ping`: Pong! Displays the ping.
                `/invite`: Displays bot invite link.
                `/alert`: Displays bot announcements.
            """)
        embed.set_author(name="Qbot", icon_url=self.bot.user.avatar.url)
        embed.add_field(name="__Manga__", 
            value="""
                **manga search `manga`**: Searches for information about a manga series.
            """, inline=False)
        embed.add_field(name="__Server__",
            value="""
                **server setup**: Sets up your server for manga updates.
            """, inline=False)
        embed.add_field(name="__User__",
            value="""
                **user setup**: Sets up your user for manga updates.
            """, inline=False)
        await ctx.respond(embed=embed)

    @commands.slash_command(name="artistupdates", description="Displays basic information about MangaUpdates")
    async def mangaupdates(self, ctx):
        print("testupdate")
        activeServers = self.bot.guilds
        botUsers = 0
        for i in activeServers:
            botUsers += i.member_count
        currentTime = time.time()
        differenceUptime = int(round(currentTime - startTime))
        uptime = str(timedelta(seconds = differenceUptime))
        botinfo = discord.Embed(
            title="ArtistUpdate-Bot",
            color=0x3083e3,
            timestamp=datetime.datetime.utcnow(),
            description=f"Thanks for using. This bot is also open-source! All code can be found on GitHub (Please leave a star ⭐ if you enjoy the bot).\n\n**Server Count:** {len(self.bot.guilds)}\n**Bot Users:** {botUsers}\n**Bot Uptime:** {uptime}"
        )
        botinfo.set_author(name="ArtistUpdate-Bot", icon_url=self.bot.user.avatar.url)
        await ctx.respond(embed=botinfo)

    @commands.slash_command(name="stats", description="Displays stats")
    async def stats(self, ctx):
        # guess get total artits tracked and also unique artist tracked
        pass

    @commands.slash_command(name="testing1", description="Pong! Displays the ping")
    async def ping(self, ctx):
        embed = discord.Embed(title="Title", description="Description", color=0x0099ff)

        # add first field with author icon
        embed.add_field(name="Field 1 Name", value="Field 1 Value", inline=False)
        embed.set_author(name="askziye", icon_url="https://pbs.twimg.com/profile_images/1232862373209231361/XqqCEzXQ_400x400.jpg")

        # add second field with author icon
        embed.add_field(name="Field 2 Name", value="https://pbs.twimg.com/profile_images/1155680462464942081/JBCvjutU_400x400.jpg", inline=False)
        embed.set_author(name="yoneyamai", icon_url="https://pbs.twimg.com/profile_images/1155680462464942081/JBCvjutU_400x400.jpg")
        await ctx.respond(embed=embed)

    # @commands.slash_command(name="set", description="Set the default channel to send updates to")
    # async def set(self, ctx):
    #     # set the default channel to send updates to
    #     str(ctx.guild_id)
    #     str(ctx.channel_id)
    #     # firebase instance and set the channel id implement when i am not sleepy g9
    #     pass
    # @commands.slash_command(name="testing",description="testing command from cog")  # Not passing in guild_ids creates a global slash command.
    # async def hiqwe(self, ctx: discord.ApplicationContext, inputs: discord.Option(str, "What do you want to say?")):
    #     await ctx.respond("Hi, this is a global slash command from a cog!"+inputs)
    #     test = Test()
    #     await ctx.respond(test.testing())



    # @commands.slash_command(name="test2",description="testing command from cog")  # Not passing in guild_ids creates a global slash command.
    # @option("name", description="Enter your name")
    # @option("gender", description="Choose your gender", choices=["Male", "Female", "Otherasd"])
    # async def hello(
    #     self,
    #     ctx: discord.ApplicationContext,
    #     name: str,
    #     gender: str,
    #     age: int,
    # ):
    #     await ctx.respond(
    #         f"Hello {name}! Your gender is {gender} and you are {age} years old."
    #     )
def setup(bot):
    bot.add_cog(Info(bot))


# The basic bot instance in a separate file should look something like this:
# bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))
# bot.load_extension("slash_cog")
# bot.run("TOKEN")