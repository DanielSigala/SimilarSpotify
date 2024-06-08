import os
from flask import Flask, request, render_template, jsonify
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initialize Flask app
app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Spotify API credentials
SPOTIFY_CLIENT_ID = 'your_spotify_client_id'
SPOTIFY_CLIENT_SECRET = 'your_spotify_client_secret'

# Initialize Spotipy client
auth_manager = SpotifyClientCredentials(client_id=SPOTIFY_CLIENT_ID, client_secret=SPOTIFY_CLIENT_SECRET)
spotify = spotipy.Spotify(auth_manager=auth_manager)


def get_similar_artists(artist_name):
    try:
        similar_artists = []

        # Get similar artists
        results = spotify.search(q='artist:' + artist_name, type='artist')
        if results['artists']['items']:
            artist = results['artists']['items'][0]
            similar = spotify.artist_related_artists(artist['id'])
            for similar_artist in similar['artists']:
                similar_artists.append({
                    'name': similar_artist['name'],
                    'id': similar_artist['id'],
                    'image': similar_artist['images'][0]['url'] if similar_artist['images'] else None
                })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return similar_artists


def get_artist_info(artist_id):
    try:
        artist_info = {}

        # Get artist information
        artist = spotify.artist(artist_id)
        artist_info['name'] = artist['name']
        artist_info['total_followers'] = artist['followers']['total']
        artist_info['popularity'] = artist['popularity']
        artist_info['image'] = artist['images'][0]['url'] if artist['images'] else None
        artist_info['external_url'] = artist['external_urls']['spotify']

        # Get artist's top tracks and their total plays
        top_tracks = spotify.artist_top_tracks(artist_id)
        artist_info['top_tracks'] = [{'name': track['name'], 'total_plays': track['popularity'], 'external_url': track['external_urls']['spotify']} for track in top_tracks['tracks']]

        # Get artist's albums and their release dates and images
        albums = spotify.artist_albums(artist_id, album_type='album')
        artist_info['albums'] = []
        for album in albums['items']:
            album_info = {
                'name': album['name'],
                'release_date': album['release_date'],
                'image': album['images'][0]['url'] if album['images'] else None,
                'external_url': album['external_urls']['spotify']
            }
            artist_info['albums'].append(album_info)

        # Get related artists
        related_artists = spotify.artist_related_artists(artist_id)
        artist_info['related_artists'] = [{'name': related_artist['name'], 'external_url': related_artist['external_urls']['spotify']} for related_artist in related_artists['artists']]
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return artist_info


# Endpoint for fetching search suggestions
@app.route('/suggest')
def suggest_artist():
    try:
        query = request.args.get('q')
        # Get search suggestions from Spotify API
        results = spotify.search(q='artist:' + query, type='artist', limit=5)
        suggestions = [{'name': artist['name']} for artist in results['artists']['items']]
        return jsonify(suggestions)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search_artist():
    try:
        artist_name = request.form['artist']
        similar_artists = get_similar_artists(artist_name)
        return render_template('results.html', artist_name=artist_name, similar_artists=similar_artists)
    except Exception as e:
        return render_template('error.html', error=str(e)), 500


@app.route('/artist/<artist_id>')
def artist_profile(artist_id):
    try:
        artist_info = get_artist_info(artist_id)
        return render_template('artist_profile.html', artist_info=artist_info)
    except Exception as e:
        return render_template('error.html', error=str(e)), 500


if __name__ == '__main__':
    app.run(debug=True)
