from ytmusicapi import YTMusic

headers_file = 'helpers/headers_auth.json'

def create_youtube_playlist(name, description):
  try:
    yt = YTMusic(headers_file)
    playlist_id = yt.create_playlist(name, description)
    return playlist_id
  except Exception as e:
    print(f"Failed to create playlist '{name}': {str(e)}")
    return None

def find_youtube_song(track_query):
  try:
    yt = YTMusic(headers_file)
    search_items = yt.search(track_query)

    for item in search_items:
      try:
        return item["videoId"]
      except KeyError:
        continue
    
    else:
        print(f"No results found for '{track_query}'")
        return None
  except Exception as e:
    print(f"Failed to search for '{track_query}': {str(e)}")
    return None

def add_videos_to_youtube_playlist(playlist_id, videos):
  try:
    yt = YTMusic(headers_file)
    response = yt.add_playlist_items(playlist_id, videos, duplicates=True)
    if response["status"] == "STATUS_SUCCEEDED":
      print(f"Added {len(videos)} videos to playlist '{playlist_id}'")
    else:
      print(f"Failed to add videos to playlist '{playlist_id}': {response}")
  except Exception as e:
    print(f"Failed to add videos to playlist '{playlist_id}': {str(e)}")