from openai import OpenAI

client = OpenAI(api_key="", base_url="https://gpt.membean.lol")

resp = client.chat.completions.create(
    model="", # model param required in open ai library, unneeded.
    messages=[
        {"role": "system", "content": "You are a helpful assistant."}, # system prompt optional
        {"role": "user", "content": "Hi!"},
    ],
)
print(resp) # full json response.
print(resp.choices[0].message.content) # # text response of gpt.