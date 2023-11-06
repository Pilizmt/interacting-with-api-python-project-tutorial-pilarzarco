from dotenv import load_dotenv

load_dotenv()

import os

client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")


import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


song_data = {
    'Name': [],
    'Popularity': [],
    'Duration (min)': []
}

if 'tracks' in results:
    for track in results['tracks'][:10]:  # Get the first 10 songs
        name = track['name']
        popularity = track['popularity']
        duration_ms = track['duration_ms']
        
        # Converts duration from milliseconds to minutes and seconds
        duration_minutes = duration_ms / 60000
        duration_seconds = (duration_ms % 60000) / 1000

        song_data['Name'].append(name)
        song_data['Popularity'].append(popularity)
        song_data['Duration (min)'].append(duration_minutes)
    
        print(f"Name: {name}")
        print(f"Popularity: {popularity}")
        print(f"Duration: {int(duration_minutes)} minutes y {int(duration_seconds)} seconds")
        print()


        import pandas as pd

df = pd.DataFrame(song_data)

df = df.sort_values(by='Popularity', ascending=False)
df.head(3)


import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.scatter(df['Duration (min)'], df['Popularity'], alpha=0.7)
plt.title('Relationship between Duration and Popularity of Songs')
plt.xlabel('Duration (minutes)')
plt.ylabel('Popularity')
plt.grid(True)
plt.show()
