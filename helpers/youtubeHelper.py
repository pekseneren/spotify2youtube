from ytmusicapi import YTMusic

def createYoutubePlaylist(name, description):
  try:
    yt = YTMusic('helpers/headers_auth.json')
    playlistId = yt.create_playlist(name, description)
    return playlistId
  except Exception as e:
    print("Playlist creation failed for: " + name)
    print("Error: " + str(e))
    return None

def findYoutubeSong(trackQuery):
  try:
    yt = YTMusic('helpers/headers_auth.json')

    search_results = yt.search(trackQuery)
    foundTheTrack = False

    for result in search_results:
      if hasattr(result, "videoId"):
        videoId = result["videoId"]
        return videoId
    
    print("Track not found in Youtube: " + trackQuery)

    return None
  except Exception as e:
    print("Playlist creation failed for: " + name)
    print("Error: " + str(e))
    return None

def addVideosToYoutubePlaylist(playlistId, videos):
  try:
    yt = YTMusic('helpers/headers_auth.json')
    response = yt.add_playlist_items(playlistId, videos, duplicates=True)
    
    if response["status"] == "STATUS_SUCCEEDED":
      print("Added video count: " + str(len(videos)))

    print("Status: " + response["status"])
  except Exception as e:
    print("Adding songs to Youtube playlist failed for: " + playlistId)
    print("Error: " + str(e))