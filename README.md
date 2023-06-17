# Spotify Playlist Generator for ChatGPT

This plugin allows ChatGPT to create Spotify playlists. This plugin is not available on the store, so you will need to have Plugin Developer access to use this; however, there are multiple similar options available on the Plugin Store.

# Config
1. Clone repository
2. Install packages: `pip install flask spotipy`
3. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/) and create a new project.
4. Store the `client_id` and `client_secret` in `./src/secrets.json` (there is an example file)
5. Go to the `src` directory and run `python serve.py`
6. Go to the ChatGPT Plugin Store -> Develop your own plugin -> Type `localhost:9080` (make sure script is running)
7. You can now create a new chat and create playlists via the chat.
