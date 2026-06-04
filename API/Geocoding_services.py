import requests

def get_location(place_name):
    """Get coordinates using Open-Meteo Geocoding API"""
    try:
        url = "https://geocoding-api.open-meteo.com/v1/search"
        response = requests.get(url, params={
            "name": place_name,
            "count": 1,
            "language": "en",
            "format": "json"
        }, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data.get('results'):
                result = data['results'][0]
                return float(result['latitude']), float(result['longitude'])
        return None
    except Exception as e:
        print(f"Error getting location: {e}")
        return None


def get_country_center(country_name):
    """Get country center coordinates"""
    try:
        return get_location(country_name)
    except Exception as e:
        print(f"Error getting country center: {e}")
        return None
