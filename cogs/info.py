# This example demonstrates a standalone cog file with the bot instance in a separate file.

import discord
from discord.ext import commands
from discord import option
from discord.ui import View, button

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