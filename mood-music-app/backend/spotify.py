import requests

SPOTIFY_TOKEN = "6922ed1f01fc45b9936f304f240a92c5"

def get_playlist(mood):
    headers = {"Authorization": f"Bearer {SPOTIFY_TOKEN}"}
    params = {"q": mood, "type": "playlist", "limit": 1}
    res = requests.get("https://api.spotify.com/v1/search", headers=headers, params=params)
    playlists = res.json().get('playlists', {}).get('items', [])
    if playlists:
        return playlists[0]['external_urls']['spotify']
    return "https://open.spotify.com"
