import requests

def detect_mood(text):
    headers = {"Authorization": f"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"}
    payload = {"inputs": text}
    response = requests.post(
        "https://api-inference.huggingface.co/models/distilbert-base-uncased-finetuned-sst-2-english",
        headers=headers,
        json=payload
    )
    label = response.json()[0][0]['label']
    if label == "POSITIVE":
        return "happy"
    elif label == "NEGATIVE":
        return "sad"
    return "neutral"
