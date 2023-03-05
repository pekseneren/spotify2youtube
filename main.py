import time
from helpers.spotifyHelper import get_spotify_tracks, get_spotify_playlists
from helpers.youtubeHelper import create_youtube_playlist, add_videos_to_youtube_playlist, find_youtube_song

def get_track_query(track):
    artist_query = " & ".join([artist["name"] for artist in track["artists"]])
    return f"{artist_query} {track['name']}"

def get_youtube_songs(spotify_playlist_tracks):
  youtube_songs = []

  for spotify_track in spotify_playlist_tracks:
    track_query = get_track_query(spotify_track["track"])
    song_id = find_youtube_song(track_query)

    if song_id is not None:
      youtube_songs.append(song_id)
  
  return youtube_songs

def sync_spotify_to_youtube_music():
  spotify_playlists = get_spotify_playlists()

  if not spotify_playlists:
    return

  print(f"Total Spotify playlist count: {len(spotify_playlists)}")

  for playlist in spotify_playlists:
    tracks = get_spotify_tracks(playlist['tracks']['href'])

    if not tracks:
      continue

    print(f"Total track count for {playlist['name']}: {len(tracks)}")

    youtube_songs = get_youtube_songs(tracks)
    print(f"Total song count found from YouTube: {len(youtube_songs)}")

    if youtube_songs:
      playlist_title = f"Spotify:{playlist['name']}"
      playlist_description = "This playlist was created from Spotify tracks with spotify2youtube."
      youtube_playlist_id = create_youtube_playlist(playlist_title, playlist_description)

      if youtube_playlist_id:
        print(f"{playlist['name']} playlist id: {youtube_playlist_id}")
        add_videos_to_youtube_playlist(youtube_playlist_id, youtube_songs)

    time.sleep(5)

def main():
  sync_spotify_to_youtube_music()

if __name__ == "__main__":
  main()
