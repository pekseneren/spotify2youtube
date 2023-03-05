import json
import requests

with open('helpers/spotify_api_config.json') as f:
    spotifyApiConfig = json.load(f)

token = spotifyApiConfig["token"]
user = spotifyApiConfig["user"]
headers = { "Authorization": f"Bearer {token}" }

def get_spotify_tracks(endpoint):
  try:
      response = requests.get(endpoint, headers=headers)
      response.raise_for_status()
      return response.json()["items"]
  except requests.exceptions.RequestException as e:
      print(f"Getting Spotify tracks failed: {e}")
      return None

def get_spotify_playlists():
    playlists = []
    next_url = f"https://api.spotify.com/v1/users/{user}/playlists"
    while next_url:
        try:
            response = requests.get(next_url, headers=headers)
            response.raise_for_status()
            data = response.json()
            playlists.extend(data["items"])
            next_url = data["next"]
        except requests.exceptions.RequestException as e:
            print(f"Getting Spotify playlists failed: {e}")
            return None
    return playlists