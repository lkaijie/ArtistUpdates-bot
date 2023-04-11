import discord
from ..cogs import test_cog
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
client = commands.Bot(command_prefix='!', intents=intents)

client.add_cog(test_cog.MyCog(client))

@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)}ms')


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    # if message.content == 'hello':
    #     print('hello was said')
    #     await message.channel.send('Hello!')


    # await client.process_commands(message)
    try:
        guild_name = message.guild.name
        await message.channel.send(message.author.name+" said "+message.content+" in "+guild_name)
    except:
        await message.channel.send(message.author.name+" said "+message.content+" in DMs")
    # if message.content.startswith('$hello'):
    #     await message.channel.send('Hello!')
    #     # print('hello was said')
    await client.process_commands(message)

client.run('MTA5NDg0NTU3NTM2ODgwNjQzMg.GdqvOy.gNHlgHk8ZuCLlij_VRFvcg3_KWjMiDFp0fR9JA')