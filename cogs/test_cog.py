import datetime
from discord.ext import commands, tasks
import pytz

utc = datetime.timezone.utc
# timezone = pytz.timezone('GMT-6')


# If no tzinfo is given then UTC is assumed.
time = datetime.time(hour=19, minute=24, tzinfo=utc) # 7:24 PM = 1:24 AM GMT-6

class MyCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.my_task2.start()
        self.my_task.start()
        print("My cog has been loaded!")

    def cog_unload(self):
        self.my_task.cancel()

    @tasks.loop(time=time)
    async def my_task(self):
        print("My task is running!")

    @tasks.loop(seconds=5)  # have to call start() to start the loop in init
    async def my_task2(self):
        print("My task 2 is running!")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        
        try:
            guild_name = message.guild.name
            await message.channel.send(message.author.name+" said(cog) "+message.content+" in "+guild_name)
        except:
            await message.channel.send(message.author.name+" said "+message.content+" in DMs")