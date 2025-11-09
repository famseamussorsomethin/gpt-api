import requests

req = requests.get("https://gpt.membean.lol/v1/models")

print(req.json())

# this code prints the (currently 3) models able to be used on this api.
# 1. gpt-oss-120b
# 2. gpt-oss-20b
# 3. gpt-5.1 (polaris alpha)

# currently, there are much less ratelimits on 20b
# because of the api provider I am using for that, 
# but 120b still has very few ratelimits.

# also, 20b and 120b are still much smarter then 4o, 
# so thats why that was my choice for this api. 
# (gpt 5 costs wayyy too pricy)