# spotify2youtube
If you don't want to snyc your Spotify tracks/playlist to Youtube Music manually then you can use this simple python app with a 5~ min of auth setup.
Created songs for Youtube Music are relay on Youtubes search algorithm. Songs are not %100 matched.

# Usage

1. Get your Spotify Access Token from [here](https://developer.spotify.com/documentation/web-playback-sdk/quick-start/).
1. If you don't know your Spotify `username` find out from [here](https://developer.spotify.com/console/get-current-user/) with your Acces Token.
1. Put your `token` and Spotify `username` in to `spotify_api_config_example.json`
1. Change `spotify_api_config_example.json` file name to `spotify_api_config.json`
1. Folllow the steps from [this site](https://ytmusicapi.readthedocs.io/en/latest/setup.html) for setting up your Youtube auth headers 
1. Check your `headers_auth.json` properties with `headers_auth_example.json`
1. Make sure your auth .json files are under `helpers` folder and remove the '_example' suffix from file names.
1. Run with `python main.py`
1. Not found tracks will be printed to console for manual search.

# YTMusic

Check out the YTMusic api from [here](https://github.com/sigma67/ytmusicapi)