import requests

BASE_URL = "http://universities.hipolabs.com/search"

def search_universities(country):
    """Search universities by country using Hipo API"""
    try:
        url = f"{BASE_URL}?country={country}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        print(f"Error searching universities: {e}")
        return []

def search_universities_by_name(name):
    """Search universities by name"""
    try:
        url = f"{BASE_URL}?name={name}"
        response = requests.get(url, timeout=10)
        
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        print(f"Error searching universities by name: {e}")
        return []
