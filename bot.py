import discord
from cogs import test_cog
from discord.ext import commands
from bot_test import get_tweets
import config
from cogs import info

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
    last_tweet_id = "1646033217944965121"
    get_tweets1 = get_tweets.Twitter_main()
    try:
        url = await (get_tweets1.get_art(arg, last_tweet_id))
        send_art = True
    except Exception as e:
        print(e)
        await ctx.send(arg+" 's latest 30 tweets/retweets were not art pieces.")
    if send_art:
        if url == None:
            await ctx.send("no new art from "+arg)
            return
        await ctx.send(arg+"'s latest work:")
        print(url[3])
        embed = discord.Embed(title="twitter link",url=url[1], color=0x00ff00)
        embed.description = "likes: "+ str(url[2])
        await ctx.send(embed=embed)
        await ctx.send(url[0])

@client.command()
async def test(ctx):
    
    embed = discord.Embed()
    embed.description = "[link](https://stackoverflow.com/questions/64527464/clickable-link-inside-message-discord-py)."
    await ctx.send(embed=embed)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print("Bot is ready")
    client.load_extension(f"cogs.info")

@client.event
async def on_message(message):
    await client.process_commands(message)
    pass

client.run(config.client_discord_token)