import http.client
import json

token = "<TOKEN_HERE>"
user = "<SPOTIFY_USER_HERE>"
payload = ''
headers = { 'Authorization': 'Bearer ' + token }
conn = http.client.HTTPSConnection("api.spotify.com")

def getTracks(endpoint):
  conn.request("GET", endpoint, payload, headers)
  tracksResponse = conn.getresponse()
  tracks = json.loads(tracksResponse.read().decode('utf-8'))

  return tracks["items"]

def getPlaylists():
  conn.request("GET", "/v1/users/" + user + "/playlists", payload, headers)
  playlistsResponse = conn.getresponse()
  playlists = json.loads(playlistsResponse.read().decode('utf-8'))

  return playlists["items"]

def convertSpotifyTrackToQuery(track):
  artistList = []

  for artist in track["artists"]:
    artistList.append(artist["name"])

  artistQuery = ' & '.join(artistList)

  return artistQuery + " " + track["name"]

def getSpotifyTracksBySearchableQuery():
  playlists = getPlaylists()

  print("Total playlist count: " + str(len(playlists)))

  trackSearchQuery = []

  for playlist in playlists:
    print("Getting tracks of playlist: " + playlist["name"])
    tracksResponse = getTracks(playlist["tracks"]["href"])

    for trackResponse in tracksResponse:
      query = convertSpotifyTrackToQuery(trackResponse["track"])
      trackSearchQuery.append(query)

  print("Total found tracks: " + str(len(trackSearchQuery)))

  return trackSearchQuery

def main():
  print("start")

  spotifyTracks = getSpotifyTracksBySearchableQuery()

  print(spotifyTracks)

  conn.close()

  print("end")

main()
