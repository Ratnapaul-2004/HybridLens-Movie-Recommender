import requests

API_KEY = "bcfa936bb4d7ff44b5d3aacfc44c7abb"
movie_id = 550   # Example (Fight Club)

url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}"

data = requests.get(url).json()
print(data)