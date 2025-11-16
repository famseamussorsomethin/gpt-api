\* there are usage limits (you can read more below), but this is super duper flippin niche so they wont be hit. (also from vercel)  
  
  
  This API contains 4 models currently.
  1. gpt-oss-120b
  2. gpt-oss-20b
  3. glm-4.5-air
  4. qwen2.5-vl-32b
  
  Currently 120b has less requests to be made in a short amount of time (per minute), however all other models have less requests able to be made per day.

  Both 120b and 20b are smarter than gpt-4o which was the go-to quick model from OpenAI for a while.
  
  I recommend using the open ai models in tools like Kilo Code, or any other IDE that allows for any open ai compatible endpoints.

## Changelog

- 2025-11-15: Removed Polaris Alpha (because of the release of OpenAI's GPT-5.1). Added Qwen2.5-VL-32b as a fast, non reasoning model.
- 2025-11-11: Added support for Anthropic /v1/messages api. You can now specify "ANTHROPIC_BASE_URL" as "https://gpt.membean.lol" in claude code.