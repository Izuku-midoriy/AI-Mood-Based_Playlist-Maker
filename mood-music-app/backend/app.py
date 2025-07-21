from flask import Flask, request, jsonify
from flask_cors import CORS
from ai import detect_mood
from spotify import get_playlist
from logger import log_entry

app = Flask(__name__)
CORS(app)

@app.route('/detectMood', methods=['POST'])
def detect():
    text = request.json.get('text', '')
    mood = detect_mood(text)
    playlist_url = get_playlist(mood)
    log_entry(text, mood, playlist_url)
    return jsonify({'mood': mood, 'playlistUrl': playlist_url})

if __name__ == '__main__':
    app.run(debug=True)
