from flask import Flask, jsonify, request, send_file, Response
from flask_cors import CORS
import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import json

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes


# Credentials you get from registering a new application
secrets = json.load(open("secrets.json", "r"))
client_id = secrets['client_id']

client_secret = secrets['client_secret']
redirect_uri='http://localhost:9080'
scope = 'playlist-modify-public'

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri))

@app.route("/create_playlist", methods=["GET"])
def create_playlist():
    song_list = request.args.get("song_list").split(";")
    playlist_name = request.args.get("playlist_name", "New Playlist")
    print(f"{song_list=}")
    print(f"{playlist_name=}")
    create_playlist_fn(song_list, playlist_name)
    return jsonify({"success": True})

def create_playlist_fn(song_list, playlist_name="New Playlist"):
    user_id = sp.current_user()['id']

    # Create a new playlist
    playlist = sp.user_playlist_create(user_id, playlist_name)

    # Add each song to the playlist
    for song in song_list:
        results = sp.search(q=song, limit=1)
        if results["tracks"]["items"]:
            track_id = results["tracks"]["items"][0]["id"]
            sp.playlist_add_items(playlist['id'], [track_id])



@app.route("/.well-known/ai-plugin.json", methods=["GET"])
def plugin_manifest():
    host = request.headers["Host"]
    with open("ai-plugin.json") as f:
        text = f.read()
        return Response(text, mimetype="text/json")


@app.route("/openapi.yaml", methods=["GET"])
def openapi_spec():
    host = request.headers["Host"]
    with open("openapi.yaml") as f:
        text = f.read()
        # text = text.replace("PLUGIN_HOSTNAME", f"https://{host}")
        return Response(text, mimetype="text/yaml")


@app.route("/icon.png", methods=["GET"])
def get_icon():
    return send_file("icon.png", mimetype="image/png")



def run_server():
    app.run(host="0.0.0.0", port=9080)


if __name__ == "__main__":
    run_server()
