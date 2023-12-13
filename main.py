import requests

CHUNK_SIZE = 1024
url = "https://api.elevenlabs.io/v1/text-to-speech/IEvJPmVjZO9YRzqAPcwu"

headers = {
  "Accept": "audio/mpeg",
  "Content-Type": "application/json",
  "xi-api-key": "976d7f250511de030dc73b7dc291fccc"
}

data = {
  "text": "Herodotus was a Greek historian and offered referred to as the father of history. Though somewhat a controversial figure in ancient historiography, his descriptions of the pyramids are rather benign and conform to our modern understanding and sensibilities.",
  "model_id": "eleven_monolingual_v1",
  "voice_settings": {
    "stability": 0.5,
    "similarity_boost": 0.5
  }
}

response = requests.post(url, json=data, headers=headers)
with open('output.mp3', 'wb') as f:
    for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
        if chunk:
            f.write(chunk)
