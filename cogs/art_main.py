# This example demonstrates a standalone cog file with the bot instance in a separate file.

import discord
from discord.ext import commands
from discord import option
from discord.ui import View, button
from ignore.test import Test
from discord.commands import SlashCommandGroup
from utils.firestoreDB import FirestoreDB
from utils import get_tweets

# class PaginationView(discord.ui.View)


class art_main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.db = FirestoreDB()
        self.db = None


    # say something when loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("main cog loaded!")



    @commands.slash_command(name="art_list",description="Shows list of tracked users")
    async def art_list(self, ctx: discord.ApplicationContext):

        tracked_users = await self.db.get_twitter_list(str(ctx.guild.id))
        embed = discord.Embed(title="Tracked Twitter Users", color=0xf1c232, 
            description="""List of tracked twitter users.
            """)
        embed.set_author(name="Qbot", icon_url=self.bot.user.avatar.url)
        for user in tracked_users:
            embed.add_field(name=f"@{user}", value=f"https://twitter.com/{user}", inline=False)
        await ctx.respond(embed=embed)  

        # pagination setup TODO

    @commands.slash_command(name="setup",description="Setup and add Server to database")
    async def setup(self, ctx: discord.ApplicationContext):
        value = await self.db.add_guild(str(ctx.guild.id), ctx.guild.name, ctx.channel_id)
        if value == True:
            await ctx.respond("Setting up server")
            await ctx.respond("Server added to database")
        else:
            await ctx.respond("Server already exists in database")

    
    @commands.slash_command(name="set", description="Set the default channel to send updates to")
    async def set(self, ctx):
        # set the default channel to send updates to
        await self.db.set_channel(str(ctx.guild_id), str(ctx.channel_id))
        await ctx.respond(f"Set default channel to {ctx.channel.name}")
        




    # just a test command
    @commands.slash_command(name="add",description="add twitter user")
    @option("username", description="Example: @(askziye)")
    async def add(
        self,
        ctx: discord.ApplicationContext,
        username: str,
    ):
        pfp = await self.db.add_twitter_artist(str(ctx.guild.id), str(username))
        embed = discord.Embed(color=0xf1c232)
        embed.set_author(name=f"Added @{username} to database.", url=f"https://twitter.com/{username}",icon_url=pfp)
        try:
            await ctx.respond(embed=embed)
        except:
            await ctx.respond("Something went wrong. Check if the user exists.")

    @commands.slash_command(name="delete",description="remove twitter user")
    @option("username", description="Example: @(askziye)")
    async def remove(
        self,
        ctx: discord.ApplicationContext,
        username: str,
    ):
        await self.db.delete_twitter_artist(str(ctx.guild.id), str(username))
        await ctx.respond(
            f"Deleted {username} from database."
        )

def setup(bot):
    bot.add_cog(art_main(bot))
