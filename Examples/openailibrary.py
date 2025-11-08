from openai import OpenAI

client = OpenAI(api_key="", base_url="https://gpt.membean.lol/v1") # api key required but unnecessary for this api.

resp = client.chat.completions.create(
    model="", # model param required in open ai library, optional.
    # ^^^ this will automatically default to gpt-oss-120b unless manually specified to be gpt-oss-20b.
    messages=[
        {"role": "system", "content": "You are a helpful assistant."}, # system prompt optional
        {"role": "user", "content": "Hi!"},
    ],
)
print(resp) # full json response.
print(resp.choices[0].message.content) # # text response of gpt.
