# ArtistUpdates-bot
Track your favorite twitter artist and get notified when they post.
![image](https://user-images.githubusercontent.com/94023052/233753404-8a4ddc9e-b5f6-49f1-89d2-bb69a1a26524.png)


# Why?
Most twitter artist retweet and reply to a bunch of unrelated content and also art from different artists. This bot makes it possible to keep track of only media posts from tracked artists


# Upcoming Features
- Migrating to postgresql from Firebase 
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

# Additional Context
- Code Refactor incoming
- Created using pycord, utilizing the twitter API