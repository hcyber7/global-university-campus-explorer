import requests


def get_coordinates(place_name):

    url = "https://nominatim.openstreetmap.org/search"

    params = {
        "q": place_name,
        "format": "json",
        "limit": 1
    }

    headers = {
        "User-Agent": "UniversityFinderProject/1.0"
    }

    try:

        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        data = response.json()

        if len(data) > 0:

            return {
                "latitude": data[0]["lat"],
                "longitude": data[0]["lon"],
                "address": data[0]["display_name"]
            }

        return None

    except Exception as e:

        print("Error:", e)
        return None

