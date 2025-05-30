import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
from rapidfuzz import fuzz

load_dotenv()  # Load environment variables from .env

# Ensure these environment variables are set
required_env_vars = ["SPOTIPY_CLIENT_ID", "SPOTIPY_CLIENT_SECRET", "SPOTIPY_REDIRECT_URI"]
for var in required_env_vars:
    if not os.getenv(var):
        raise ValueError(f"Missing required environment variable: {var}")

# Initialize Spotify client with cache file
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="playlist-modify-public",
    cache_path=".spotify_cache",
    open_browser=True
))


df = pd.read_csv('hindustani_vocalists_by_gharana.csv')  # Assumes one column with artist names
artist_names = df['Vocalist Name'].dropna().tolist()

def search_artist_on_spotify(artist_name):
    results = sp.search(q=f"artist:{artist_name}", type='artist', limit=5)
    items = results['artists']['items']
    
    # Use fuzzy matching to get the closest name
    best_match = None
    best_score = 0
    for item in items:
        score = fuzz.ratio(item['name'].lower(), artist_name.lower())
        if score > best_score:
            best_score = score
            best_match = item

    return best_match['id'] if best_match else None


def get_top_tracks(artist_id, country='US'):
    results = sp.artist_top_tracks(artist_id, country=country)
    return [track['uri'] for track in results['tracks'][:5]]

def create_playlist(name="My Artist Top 5s"):
    user_id = sp.current_user()['id']
    playlist = sp.user_playlist_create(user_id, name)
    return playlist['id']

def add_tracks_to_playlist(playlist_id, track_uris):
    for i in range(0, len(track_uris), 100):
        sp.playlist_add_items(playlist_id, track_uris[i:i+100])

all_track_uris = []

for artist in artist_names:
    artist_id = search_artist_on_spotify(artist)
    if artist_id:
        top_tracks = get_top_tracks(artist_id)
        all_track_uris.extend(top_tracks)

playlist_id = create_playlist("All Gharanas artists top 5 songs")
add_tracks_to_playlist(playlist_id, all_track_uris)

print(f"Created playlist with {len(all_track_uris)} songs!")