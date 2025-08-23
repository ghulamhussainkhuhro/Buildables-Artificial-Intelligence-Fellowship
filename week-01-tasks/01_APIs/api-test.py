import requests

# Send a GET request to the API
response = requests.get("https://official-joke-api.appspot.com/random_joke")

# Print raw response (text)
print(response.text)
