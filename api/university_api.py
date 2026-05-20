import requests

BASE_URL = "https://restcountries.com/v3.1/all?fields=name,flags"


def get_country_info(country):

    url = BASE_URL + country

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    return []


results = get_country_info("Germany")

country = results[0]

print("Country:", country["name"]["common"])
print("Capital:", country["capital"][0])
print("Region:", country["region"])
noohgfc helpp