from helpers.spotifyHelper import getTracks, getPlaylists
from helpers.youtubeHelper import createPlaylist, findEquivalentVideosOnYoutube, addVideosToPlaylist

def convertSpotifyTrackToQuery(track):
  artistList = []

  for artist in track["artists"]:
    artistList.append(artist["name"])

  artistQuery = " & ".join(artistList)

  trackQuery = artistQuery + " " + track["name"]

  return trackQuery

def getSpotifyTracksAsQueryList():
  playlists = getPlaylists()

  print("Total playlist count: " + str(len(playlists)))

  trackQueryList = []

  for playlist in playlists:
    tracksResponse = getTracks(playlist["tracks"]["href"])

    for trackResponse in tracksResponse:
      query = convertSpotifyTrackToQuery(trackResponse["track"])
      trackQueryList.append(query)

  print("Total found tracks: " + str(len(trackQueryList)))

  return trackQueryList

def createYoutubePlaylistWithEquivalentVideos(equivalentTracks):
  playListId = createPlaylist("My Spotify Tracks", "This playlist created for my Spotify Tracks with spotify2youtube.")
  print("Playlist created: " + playListId)
  addVideosToPlaylist(playListId, equivalentTracks)

def main():
  trackQueryList = getSpotifyTracksAsQueryList()

  equivalentVideos = findEquivalentVideosOnYoutube(trackQueryList)

  createYoutubePlaylistWithEquivalentVideos(equivalentVideos)

main()
