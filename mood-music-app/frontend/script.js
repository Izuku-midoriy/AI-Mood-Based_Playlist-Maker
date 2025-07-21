function detectMood() {
  const text = document.getElementById('moodInput').value;
  fetch('https://YOUR_CLOUD_RUN_URL/detectMood', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text })
  })
  .then(res => res.json())
  .then(data => {
    document.getElementById('player').innerHTML = `
      <p>Mood: ${data.mood}</p>
      <iframe src="${data.playlistUrl}" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>
    `;
  });
}

function startVoice() {
  const recognition = new webkitSpeechRecognition();
  recognition.lang = "en-US";
  recognition.onresult = function(event) {
    document.getElementById("moodInput").value = event.results[0][0].transcript;
  };
  recognition.start();
}
