import time
from helpers.spotifyHelper import getSpotifyTracks, getSpotifyPlaylists
from helpers.youtubeHelper import createYoutubePlaylist, findYoutubeSong, addVideosToYoutubePlaylist

def getTrackQuery(track):
  artistList = []

  for artist in track["artists"]:
    artistList.append(artist["name"])

  artistQuery = " & ".join(artistList)

  trackQuery = artistQuery + " " + track["name"]

  return trackQuery

def getYoutubeSongs(spotifyPlaylistTracks):
  youtubeSongs = []

  for spotifyTrack in spotifyPlaylistTracks:
    trackQuery = getTrackQuery(spotifyTrack["track"])
    songId = findYoutubeSong(trackQuery)

    if songId is not None:
      youtubeSongs.append(songId)
  
  return youtubeSongs

def syncSpotifyToYoutubeMusic():
  spotifyPlaylists = getSpotifyPlaylists()

  if spotifyPlaylists is None:
    return

  print("Total Spotify playlist count: " + str(len(spotifyPlaylists)))

  for spotifyPlaylist in spotifyPlaylists:
    spotifyPlaylistTracks = getSpotifyTracks(spotifyPlaylist["tracks"]["href"])

    if spotifyPlaylistTracks is None:
      continue

    print("Total track count for " + spotifyPlaylist["name"] + ": " + str(len(spotifyPlaylistTracks)))
    
    youtubeSongs = getYoutubeSongs(spotifyPlaylistTracks)
    print("Total song count found from Youtube: " + str(len(youtubeSongs)))
    
    if len(youtubeSongs) > 0:
      youtubePlayListId = createYoutubePlaylist("Spotify:"+ spotifyPlaylist["name"], "This playlist created from Spotify trakcs with spotify2youtube")

      if youtubePlayListId is not None:
        print(spotifyPlaylist["name"] + " Playlist id: " + youtubePlayListId)
        addVideosToYoutubePlaylist(youtubePlayListId, youtubeSongs)
    
    time.sleep(5)

def main():
  syncSpotifyToYoutubeMusic()

main()
