import http.client
import json

spotifyApiConfigFile = open('helpers/spotify_api_config.json')
spotifyApiConfig = json.load(spotifyApiConfigFile)

token = spotifyApiConfig["token"]
user = spotifyApiConfig["user"]
payload = ""
headers = { "Authorization": "Bearer " + token }

def getTracks(endpoint):
  conn = http.client.HTTPSConnection("api.spotify.com")
  conn.request("GET", endpoint, payload, headers)
  tracksResponse = conn.getresponse()
  tracks = json.loads(tracksResponse.read().decode("utf-8"))
  conn.close()

  return tracks["items"]

def getPlaylists():
  conn = http.client.HTTPSConnection("api.spotify.com")
  conn.request("GET", "/v1/users/" + user + "/playlists", payload, headers)
  playlistsResponse = conn.getresponse()
  playlists = json.loads(playlistsResponse.read().decode("utf-8"))
  conn.close()

  return playlists["items"]