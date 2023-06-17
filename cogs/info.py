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


    @commands.Cog.listener()
    async def on_ready(self):
        print("Info cog loaded!")

    @commands.slash_command(name="help",description="Displays all avaliable commands")  
    async def help(self, ctx: discord.ApplicationContext):# 0x3083e3 is the color of the embed
        '''Displays all avaliable commands'''
        embed = discord.Embed(title="AR commands", color=0xf1c232, 
            description="""
                `/info`: Displays basic information about this bot.
                `/help`: Shows this message.
                `/ping`: Pong! Displays the ping.
                `/art_list`: Displays all the artists you are tracking.
                `/add`: Adds an artist to the list of artists you are tracking.
                `/delete`: Deletes an artist from the list of artists you are tracking.
                `/set`: Sets the default channel to send updates to.
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
        '''Displays basic information about artistupdates'''
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


def setup(bot):
    bot.add_cog(Info(bot))
