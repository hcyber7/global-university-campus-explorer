import requests

BASE_URL = "http://universities.hipolabs.com/search"


def search_universities(country):

    url = f"{BASE_URL}?country={country}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return []


results = search_universities("Germany")
print(results)
assss