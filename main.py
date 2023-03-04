from helpers.spotifyHelper import getTracks, getPlaylists
from helpers.youtubeHelper import createPlaylist, findEquivalentVideosOnYoutube, addVideosToPlaylist

def convertSpotifyTrackToQuery(track):
  artistList = []

  for artist in track["artists"]:
    artistList.append(artist["name"])

  artistQuery = " & ".join(artistList)

  trackQuery = artistQuery + " " + track["name"]

  return trackQuery

def createYoutubePlaylistWithEquivalentVideos(playlistName, equivalentVideos):
  playListId = createPlaylist("Spotify:"+ playlistName, "This playlist created from Spotify trakcs with spotify2youtube")
  print(playlistName + ": " + playListId)
  addVideosToPlaylist(playListId, equivalentVideos)

def main():
  playlists = getPlaylists()

  print("Total playlist count: " + str(len(playlists)))

  for playlist in playlists:
    tracksQueryList = []
    tracksResponse = getTracks(playlist["tracks"]["href"])

    for trackResponse in tracksResponse:
      query = convertSpotifyTrackToQuery(trackResponse["track"])
      tracksQueryList.append(query)

    equivalentVideos = findEquivalentVideosOnYoutube(tracksQueryList)

    createYoutubePlaylistWithEquivalentVideos(playlist["name"], equivalentVideos)


main()
