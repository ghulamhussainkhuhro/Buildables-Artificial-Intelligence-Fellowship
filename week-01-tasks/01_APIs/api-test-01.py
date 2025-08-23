import requests

# Call the API
response = requests.get("https://official-joke-api.appspot.com/random_joke")

# Convert to Python dictionary
data = response.json()

# Access parts of the JSON
print("Setup:", data["setup"])
print("Punchline:", data["punchline"])