import requests

BASE_URL = "http://universities.hipolabs.com/search"


def search_universities(country):

    url = f"{BASE_URL}?country={country}"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return []


results = get_country_info("Germany")

country = results[0]

print("Country:", country["name"]["common"])
print("Capital:", country["capital"][0])
print("Region:", country["region"])

results = search_universities("Germany")
print(results)
