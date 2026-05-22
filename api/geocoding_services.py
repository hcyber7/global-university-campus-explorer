import requests

def get_location(place_name):
    """Get coordinates using Nominatim"""
    try:
        url = "https://nominatim.openstreetmap.org/search"
        response = requests.get(url, params={
            "q": place_name,
            "format": "json",
            "limit": 1
        }, headers={"User-Agent": "UniversityExplorer"}, timeout=10)
        
        if response.status_code == 200:
            data = response.json()
            if data:
                return float(data[0]['lat']), float(data[0]['lon'])
        return None
    except:
        return None

def get_country_center(country_name):
    """Get country center coordinates"""
    try:
        return get_location(country_name)
    except:
        return None
