# ArtistUpdates-bot
Track your favorite artist and get notified when they post.


# Upcoming Features
Migrating to postgresql from Firebase
Adding pixiv and possibly weibo tracking


# Installing
## Few things needed before you can run the bot
1. Twitter API key, Firestore config and Discord Bot client key is needed
2. make a config.py file with the following fields ```(
    (twitter)
    API_Key = ""
    API_Key_Secret = ""
    Bearer = ""
    Access_Token = ""
    Access_Token_Secret = ""
    (discord)
    Client_ID = ""
    Client_Secret = ""
    client_discord_token = ""
    (firebase)
    firebase_config = {
    })```
3. Run bot.py

# Additional Context
- Code Refactor incoming
- Created using pycord, utilizing the twitter API