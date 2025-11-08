import requests # pip install requests

resp = requests.post("https://gpt.membean.lol/v1/chat/completions", json={
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."}, # system prompt optional
        {"role": "user", "content": "Hi!"},
    ],
    "model": "" # optional,
    # If left blank or an incorrect model this will default to gpt-oss-120b. 
    # You can manually switch to gpt-oss-20b for different ratelimits. 
})

print(resp.json()) # full json response.
print(resp.json()["choices"][0]["message"]["content"]) # text response of gpt.