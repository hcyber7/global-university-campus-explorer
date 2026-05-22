import requests


BASE_URL = "https://nominatim.openstreetmap.org/search"


def get_location(university_name):

    try:

        response = requests.get(
            BASE_URL,
            params={
                "q": university_name,
                "format": "json",
                "limit": 1
            },
            headers={
                "User-Agent": "GlobalUniversityExplorer"
            }
        )

        response.raise_for_status()

        data = response.json()

        if not data:
            return None

        location = {
            "latitude": data[0]["lat"],
            "longitude": data[0]["lon"]
        }

        return location

    except requests.exceptions.RequestException as e:

        print(f"Geocoding Error: {e}")

        return None
