\* there are usage limits (you can read more below), but this is super duper flippin niche so they wont be hit. (also from vercel)  
  
  
  This API contains 3 models currently.
  1. gpt-oss-120b
  2. gpt-oss-20b
  3. gpt-5.1 (Polaris Alpha)
  
  Currently 120b has less requests able to be made per day, however 20b has less requests to be made in a short amount of time (per minute).

  Both 120b and 20b are smarter than gpt-4o which was the go-to quick model from OpenAI for a while. 

  Polaris Alpha is a stealth model currently on Open Router that is highly speculated to be gpt-5.1 (because of its responses and naming). Right now it is free on Open Router so it is part of this api.
  
  I recommend using this in tools like Kilo Code, or any other IDE that allows for any open ai compatible endpoints. Both models are very good at tool calls.

## Changelog

- 2025-11-11: Added support for Anthropic /v1/messages api. You can now specify "ANTHROPIC_BASE_URL" as "https://gpt.membean.lol" in claude code.