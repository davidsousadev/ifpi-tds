import requests, json
response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + "exo")
response = json.dumps(response.json())
print(response)
