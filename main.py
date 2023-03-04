from helpers.spotifyHelper import getTracks, getPlaylists
from helpers.youtubeHelper import createPlayList, findEquivalentVideosOnYoutube, addVideosToPlayList

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

def createYoutubePlayListWithEquivalentVideos(equivalentTracks):
  playListId = createPlayList("My Spotify Tracks", "PlayList for Synced Spotify Tracks with spotify2youtube.")
  print("PlayList created:" + playListId)
  addVideosToPlayList(playListId, equivalentTracks)

def main():
  trackQueryList = getSpotifyTracksAsQueryList()

  equivalentVideos = findEquivalentVideosOnYoutube(trackQueryList)

  createYoutubePlayListWithEquivalentVideos(equivalentVideos)

main()
