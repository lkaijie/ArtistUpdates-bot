import os
import sys
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import asyncio

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from utils import get_tweets
import config





class FirestoreDB():
    def __init__(self):
        cred = credentials.Certificate(config.firebase_config)
        firebase_admin.initialize_app(cred)
        self.db = firestore.client()
        self.twitter_main = get_tweets.Twitter_main()

    
    async def add_guild(self, guild_id, guild_name, channel_id):
        '''Adds a guild to the database'''
        guild_ref = self.db.collection("Guilds").document(guild_id)
        if guild_ref.get().exists:
            return False
        else:
            artist_ref = guild_ref.collection("twitter_list")
            artist_ref2 = guild_ref.collection("pixiv_list")
            guild_ref.set({
                "guild_name": guild_name,
                "channel_id": channel_id,
                "date_first_joined": firestore.SERVER_TIMESTAMP,
                "date_last_updated": firestore.SERVER_TIMESTAMP
            })
            return True
    
    async def get_guilds(self):
        guilds = self.db.collection("Guilds")
        guild_ids = []
        for guild in guilds.stream():
            # print(f'{guild.id} => {guild.to_dict()}')
            guild_ids.append(guild.id)
        return guild_ids

    async def get_channel(self, guild_id):
        guild_ref = self.db.collection("Guilds").document(guild_id)
        guild_doc = guild_ref.get()
        if guild_doc.exists:
            return guild_doc.to_dict().get("channel_id")
        else:
            return None

    
    async def get_twitter_list(self, guild_id) -> list:
        '''Returns a list of tracked twitter artists'''
        guild_ref = self.db.collection("Guilds").document(guild_id)
        guild_doc = guild_ref.get()
        return_list = []
        if guild_doc.exists:
            sub_collection = guild_ref.collections()
            for doc in sub_collection:
                if doc.id == "twitter_list":
                    for d in doc.stream():
                        # print(f'{d.id} => {d.to_dict()}')
                        return_list.append(d.id)
        return return_list
    
    async def get_pfp(self, guild_id, artist_id) -> str:
        '''Returns the profile picture of the artist'''
        guild_ref = self.db.collection("Guilds").document(guild_id)
        artist_ref = guild_ref.collection("twitter_list").document(artist_id)
        artist_doc = artist_ref.get()
        if artist_doc.exists:
            return artist_doc.to_dict().get("profile_pic")
        else:
            return None


    async def get_last_work(self, guild_id, artist_id) -> dict:
        '''Returns the last work of the artist'''
        guild_ref = self.db.collection("Guilds").document(guild_id)
        artist_ref = guild_ref.collection("twitter_list").document(artist_id)
        artist_doc = artist_ref.get()
        if artist_doc.exists:
            return artist_doc.to_dict()
        else:
            return None
        
    async def delete_twitter_artist(self, guild_id, artist_id):
        '''Deletes the artist from the database'''
        guild_ref = self.db.collection("Guilds").document(guild_id)
        artist_ref = guild_ref.collection("twitter_list").document(artist_id)
        artist_doc = artist_ref.get()
        if artist_doc.exists:
            artist_ref.delete()
        else:
            print("Artist does not exist")


    async def add_twitter_artist(self, guild_id, artist_id):
        '''adds a twitter artist to the database with the last tweet id'''
        guild_ref = self.db.collection("Guilds").document(guild_id)
        artist_ref = guild_ref.collection("twitter_list")
        doc_ref = artist_ref.document(artist_id)
        # Guilds -> ybugqgybewiwe -> twitter_list -> askziye
        doc = doc_ref.get()
        if doc.exists:
            print("Document exists")
        else:
            print("Document does not exist")
            last_tweet_id = await self.twitter_main.get_last_id(artist_id)
            pfp_url = await self.twitter_main.get_pfp(artist_id)
            
            if last_tweet_id == None:
                doc_ref.set({"last_tweet_id": "0","profile_pic": pfp_url}) # if multiple attributes plz do one line
            else:
                doc_ref.set({"last_tweet_id": last_tweet_id,"profile_pic": pfp_url})
            return pfp_url
                
    async def set_channel(self, guild_id, channel_id):
        '''Sets the channel id for the guild'''
        guild_ref = self.db.collection("Guilds").document(guild_id)
        guild_doc = guild_ref.get()
        if guild_doc.exists:
            guild_ref.update({"channel_id": channel_id})
        else:
            print("Guild does not exist")
    
    async def update_last_tweet_id(self, guild_id, artist_id, last_tweet_id):
        '''Updates the last tweet id of the artist'''
        guild_ref = self.db.collection("Guilds").document(guild_id)
        artist_ref = guild_ref.collection("twitter_list").document(artist_id)
        artist_doc = artist_ref.get()
        if artist_doc.exists:
            artist_ref.update({"last_tweet_id": last_tweet_id})
        else:
            print("Artist does not exist")

async def main():
    testing = FirestoreDB()
    artists = await testing.get_twitter_list("WUSEqWOxrIJSmLH9zV0A")
    print("List of artists")
    for artist in artists:
        print(artist)
        print("Last Work: ")
        last_work = await testing.get_last_work("WUSEqWOxrIJSmLH9zV0A", artist)
        print(last_work)
        print("id of last work")
        print(last_work["last_tweet_id"])
    await testing.add_twitter_artist("WUSEqWOxrIJSmLH9zV0A", "genshinimpact") # alreadyt exists
    await testing.add_twitter_artist("WUSEqWOxrIJSmLH9zV0A", "KuguiEMA") # does not exist
    guilds = await testing.get_guilds()
    for x in guilds:
        print(x)    


if __name__ == "__main__":
    asyncio.run(main())