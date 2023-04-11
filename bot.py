import discord
from cogs import test_cog
from discord.ext import commands
from bot_test import get_tweets
import config

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)

# client.add_cog(test_cog.MyCog(client))
# client.load_extension('cogs.test_cog')

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')

@client.command()
async def get(ctx, arg):
    send_art = False
    try:
        url = (get_tweets.get_art(arg))
        send_art = True
    except:
        await ctx.send(arg+" 's latest 30 tweets/retweets were not art pieces.")
    if send_art:
        await ctx.send(arg+"'s latest work:")
        await ctx.send(url)




@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print("Bot is ready")
    await client.change_presence(activity=discord.Game(name="with your mom"))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="you sleep"))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="your mom scream"))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="with your mom"))
    # await client.add_cog(test_cog.MyCog(client))

@client.event
async def on_message(message):
    # if message.author == client.user:
    #     return
    
    # # if message.content == 'hello':
    # #     print('hello was said')
    # #     await message.channel.send('Hello!')


    # # await client.process_commands(message)
    # try:
    #     guild_name = message.guild.name
    #     await message.channel.send(message.author.name+" said "+message.content+" in "+guild_name)
    # except:
    #     await message.channel.send(message.author.name+" said "+message.content+" in DMs")
    # # if message.content.startswith('$hello'):
    # #     await message.channel.send('Hello!')
    # #     # print('hello was said')
    await client.process_commands(message)
    pass

client.run(config.client_discord_token)