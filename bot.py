# This example requires the 'members' privileged intent to use the Member converter.

import os
import discord
import config
from utils.firestoreDB import FirestoreDB


intents = discord.Intents.default()
intents.members = True

bot = discord.Bot(intents=intents)
db = FirestoreDB()


bot.load_extension("cogs.info")  # Load info cog
bot.load_extension("cogs.twitter_main")  # Load twitter cog
bot.load_extension("cogs.art_main")  # Load art cog
bot.load_extension("cogs.check_updates")  # Load test cog
art_main = bot.get_cog("art_main")
art_main.db = db
check_updates = bot.get_cog("check_updates")
check_updates.db = db

# adds all cogs in cogs folder (uncomment when ready)
# for file in os.listdir("./cogs"):
#     if file.endswith(".py"):
#         name = file[:-3]
#         bot.load_extension(f"cogs.{name}")




@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    print(f"Bot ID: {bot.user.id}")

@bot.slash_command()
async def joined(ctx: discord.ApplicationContext, member: discord.Member = None):
    # Setting a default value for the member parameter makes it optional ^
    user = member or ctx.author
    await ctx.respond(
        f"{user.name} joined at {discord.utils.format_dt(user.joined_at)}"
    )

@bot.slash_command()
async def bot_joined(ctx: discord.ApplicationContext):
    await ctx.respond(
        f"I joined at {discord.utils.format_dt(bot.user.joined_at)}"
    )







# To learn how to add descriptions and choices to options, check slash_options.py
bot.run(config.client_discord_token)