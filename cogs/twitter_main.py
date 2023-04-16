# This example demonstrates a standalone cog file with the bot instance in a separate file.

import discord
from discord.ext import commands
from discord import option
from discord.ui import View, button
import config
# from ignore.test import Test
# import slash command group
from discord.commands import SlashCommandGroup

class Twitter(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.Cog.listener()
    async def on_ready(self):
        print("Twitter cog loaded!")



    @commands.slash_command(name="twitter_list",description="Show list of tracked twitter users")
    async def twitter_list(self, ctx: discord.ApplicationContext):
        embed = discord.Embed(title="Tracked Twitter Users", color=0xf1c232, 
            description="""
                `@askziye`
                `@askziye`
                `@askziye`
                `@askziye`
            """)
        embed.set_author(name="Qbot", icon_url=self.bot.user.avatar.url)
        await ctx.respond(embed=embed) 

    @commands.slash_command(name="twitter",description="Add twitter users to track")  # Not passing in guild_ids creates a global slash command.
    @option("option", description="Add or Delete", choices=["Add", "Delete" ])
    @option("username", description="Example: @(askziye)")
    async def twitter(
        self,
        ctx: discord.ApplicationContext,
        option: str,
        username: str,
    ):
        
        if option == "Add":
            await ctx.respond(
                f"Selected{option} for username {username}."
            )


        elif option == "Delete":
            await ctx.respond(
                f"Selected{option} for username {username}."
            )
        await ctx.respond(
            f"Selected{option} for username {username}."
        )
def setup(bot):
    bot.add_cog(Twitter(bot))
