import isort
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from settings import SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET

birdy_uri = 'spotify:artist:2ye2Wgw4gimLv2eAKyk1NB'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())
results = spotify.artist_albums(birdy_uri, album_type='album')
albums = results['items']
print(albums)
while results['next']:
    results = spotify.next(results)
    albums.extend(results['items'])
for album in albums:
    print(album['name'])
