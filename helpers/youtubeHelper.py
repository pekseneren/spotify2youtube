from ytmusicapi import YTMusic

def createPlayList(name, description):
  yt = YTMusic('helpers/headers_auth.json')
  playlistId = yt.create_playlist(name, description)

  return playlistId

def findEquivalentVideosOnYoutube(trackQueryList):
  yt = YTMusic('helpers/headers_auth.json')
  equivalentVideos = []

  for trackQuery in trackQueryList:
    search_results = yt.search(trackQuery)

    for result in search_results:
      try:
        videoId = search_results[0]["videoId"]
        equivalentVideos.append(videoId)
        break
      except Exception as songException:
        continue

  return equivalentVideos

def addVideosToPlayList(playlistId, videos):
  yt = YTMusic('helpers/headers_auth.json')
  response = yt.add_playlist_items(playlistId, videos, duplicates=True)
  
  if response["status"] == "STATUS_SUCCEEDED":
    print("Added video count:" + str(len(equivalentTracks)))

  print("Status:" + response["status"])