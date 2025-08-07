from flask import Flask, request, jsonify
from flask_cors import CORS
from logger import log_entry

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "MoodTunes Flask Backend is Running!"

@app.route('/detectMood', methods=['POST'])
def detect_mood():
    data = request.get_json()
    text = data.get('text', '')

    # Dummy mood detection logic
    if "happy" in text.lower():
        mood = "Happy"
        playlist_url = "https://open.spotify.com/embed/playlist/37i9dQZF1DXdPec7aLTmlC"
    elif "calm" in text.lower():
        mood = "Calm"
        playlist_url = "https://open.spotify.com/embed/playlist/37i9dQZF1DWVFeEut75IAL"
    else:
        mood = "Neutral"
        playlist_url = "https://open.spotify.com/embed/playlist/37i9dQZF1DX3rxVfibe1L0"

    # Log to PostgreSQL
    log_entry(text, mood, playlist_url)

    return jsonify({"mood": mood, "playlistUrl": playlist_url})

if __name__ == '__main__':
    app.run(debug=True)
