import requests


url = "https://nominatim.openstreetmap.org/search"

params = {
    "q": "University of Stuttgart",
    "format": "json",
    "limit": 1
}

headers = {
    "User-Agent": "GlobalUniversityExplorer"
}


response = requests.get(
    url,
    params=params,
    headers=headers
)

data = response.json()

print(data)
