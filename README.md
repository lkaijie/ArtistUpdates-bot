
</br>
    <div align="center">
        <img src="https://cdn.discordapp.com/avatars/1094845575368806432/3d1eb05f18c16cf6fb7370b27eea47ab.webp?size=128">
        <h2>ArtistUpdates-bot</h3>
        <span>A Discord bot for keeping track of your favourite artists</span>
    </div>
    <div align="center"style="margin-top:30px">
            <a href="https://www.python.org/">
                <img src="https://img.shields.io/badge/Python-3.11.1-blue?logo=python&logoColor=white" alt="Python 3.11.1">
            </a>
            <!-- pycord -->
            <a href="https://github.com/Pycord-Development/pycord">
                <img src="https://img.shields.io/badge/Pycord-2.4.1-blue?logo=discord&logoColor=white" alt="Pycord 2.4.1">
            </a>
            <!-- twitter api -->
            <img src="https://img.shields.io/badge/Tweepy-4.1.0-blue?logo=twitter&logoColor=white" alt="Tweepy 4.1.0">
            <!-- firebase -->
            <img src="https://img.shields.io/badge/Firebase-8.6.0-blue?logo=firebase&logoColor=white" alt="Firebase 8.6.0">
        </div>
</br>

# About
ArtistUpdates is a simple bot created to keep track and notify users when a tracked artist posts new media, ignoring all retweets.

Created using Python and Firebase, mainly utilizing the tweepy and pycord libraries

### The bot can be invited [here (OLD version)](https://discord.com/api/oauth2/authorize?client_id=1094845575368806432&permissions=139586750528&scope=bot%20applications.commands)

## Example output
![image](https://github.com/lkaijie/ArtistUpdates-bot/assets/94023052/301eac9c-212f-4b77-bcd9-463c30b7df0d)
<!-- ![image](https://github.com/lkaijie/ArtistUpdates-bot/assets/94023052/5cd1be34-e83c-4a8d-996e-7551bf4b8155) -->
<!-- ![image](https://github.com/lkaijie/ArtistUpdates-bot/assets/94023052/09babbc3-a468-4574-b2e2-1505223579e4) -->


## Supported Commands
### This bot supports slash commands
- `/add <twitter username>` - Adds a twitter user to the tracking list
- `/delete <twitter username>` - Removes a twitter user from the tracking list
- `/art_list` - Lists all the twitter users being tracked
- `/help` - Lists all the commands
- `/set_channel` - Sets the channel to send updates to

# Why?
Most twitter artist retweet and reply to a bunch of unrelated content and also art from different artists. This bot makes it possible to keep track of only media posts from tracked artists


# Upcoming Features
- Seperate update checking and bot logic
- Adding pixiv and possibly weibo tracking 
- Port following list into tracking list
- Add tracking for users via DMs instead of only servers


# Installing
## Few things needed before you can run the bot
```
pip install -r requirements.txt
```

1. Twitter API key, Firestore config and Discord Bot client key is needed
```
# Twitter
API_Key = ""
API_Key_Secret = ""
Bearer = ""
Access_Token = ""
Access_Token_Secret = ""

# Discord
Client_ID = ""
Client_Secret = ""
client_discord_token = ""

# Firebase firestore
firebase_config = {
}

```
2. Create a config.py file and place it in the root directory
3. Run bot.py

