# This example demonstrates a standalone cog file with the bot instance in a separate file.

import discord
from discord.ext import commands
from discord import option
from discord.ui import View, button
# from ignore.test import Test
from discord.commands import SlashCommandGroup
from utils.firestoreDB import FirestoreDB
from utils import get_tweets

class art_main(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.db = FirestoreDB()
        self.db = None


    # say something when loaded
    @commands.Cog.listener()
    async def on_ready(self):
        print("main cog loaded!")
    # when there are more commands add here



    @commands.slash_command(name="art_list",description="Shows list of tracked users")
    async def art_list(self, ctx: discord.ApplicationContext):

        tracked_users = await self.db.get_twitter_list(str(ctx.guild.id))






        embed = discord.Embed(title="Tracked Twitter Users", color=0xf1c232, 
            description="""
                `@askziye`
                `@askziye`
                `@askziye`
                `@askziye`
            """)
        embed.set_author(name="Qbot", icon_url=self.bot.user.avatar.url)
        await ctx.respond(embed=embed)  

    @commands.slash_command(name="setup",description="Setup and add Server to database")
    async def setup(self, ctx: discord.ApplicationContext):
        value = await self.db.add_guild(str(ctx.guild.id), ctx.guild.name, ctx.channel_id)
        if value == True:
            await ctx.respond("Setting up server")
            await ctx.respond("Server added to database")
        else:
            await ctx.respond("Server already exists in database")


    # just a test command
    @commands.slash_command(name="add",description="add twitter user")
    @option("username", description="Example: @(askziye)")
    async def add(
        self,
        ctx: discord.ApplicationContext,
        username: str,
    ):
        await self.db.add_twitter_artist(str(ctx.guild.id), str(username))
        await ctx.respond(
            f"Added {username} to database."
        )
        # change this to embed msg with user profile pic and name with clickable link to twitter

def setup(bot):
    bot.add_cog(art_main(bot))


# The basic bot instance in a separate file should look something like this:
# bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"))
# bot.load_extension("slash_cog")
# bot.run("TOKEN")