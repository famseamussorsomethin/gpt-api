import requests # pip install requests

resp = requests.post("https://gpt.membean.lol", json={
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."}, # system prompt optional
        {"role": "user", "content": "Hi!"},
    ],
})

print(resp.json()) # full json response.
print(resp.json()["choices"][0]["message"]["content"]) # text response of gpt.