import requests
from typing import Optional, Dict, Tuple, List

BASE_URL = "https://nominatim.openstreetmap.org"
HEADERS = {"User-Agent": "UniversityFinderProject/1.0"}
TIMEOUT = 10


def get_coordinates(place_name: str) -> Optional[Dict]:
    """
    Get coordinates for a place using Nominatim search API.
    
    Args:
        place_name: Name of the place to search for
        
    Returns:
        Dictionary with latitude, longitude, and address, or None if not found
    """
    url = f"{BASE_URL}/search"
    
    params = {
        "q": place_name,
        "format": "json",
        "limit": 1
    }
    
    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()
        
        if len(data) > 0:
            return {
                "latitude": float(data[0]["lat"]),
                "longitude": float(data[0]["lon"]),
                "address": data[0]["display_name"]
            }
        return None
        
    except Exception as e:
        print(f"Error fetching coordinates for '{place_name}': {e}")
        return None


def get_reverse_coordinates(latitude: float, longitude: float) -> Optional[Dict]:
    """
    Get address information for given coordinates using Nominatim reverse API.
    
    Args:
        latitude: Latitude coordinate
        longitude: Longitude coordinate
        
    Returns:
        Dictionary with address information or None if not found
    """
    url = f"{BASE_URL}/reverse"
    
    params = {
        "lat": latitude,
        "lon": longitude,
        "format": "json"
    }
    
    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()
        
        return {
            "address": data.get("address", {}),
            "display_name": data.get("display_name", ""),
            "lat": float(data["lat"]),
            "lon": float(data["lon"])
        }
        
    except Exception as e:
        print(f"Error fetching address for coordinates ({latitude}, {longitude}): {e}")
        return None


def search_universities_by_location(latitude: float, longitude: float, radius_km: int = 50) -> Optional[Dict]:
    """
    Search for places (universities) around a given location.
    
    Args:
        latitude: Latitude coordinate
        longitude: Longitude coordinate
        radius_km: Search radius in kilometers (default: 50)
        
    Returns:
        Dictionary with location information or None if not found
    """
    url = f"{BASE_URL}/reverse"
    
    params = {
        "lat": latitude,
        "lon": longitude,
        "format": "json",
        "zoom": 15
    }
    
    try:
        response = requests.get(url, params=params, headers=HEADERS, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()
        
        return {
            "name": data.get("display_name", "Unknown"),
            "latitude": float(data["lat"]),
            "longitude": float(data["lon"]),
            "address_details": data.get("address", {})
        }
        
    except Exception as e:
        print(f"Error searching location ({latitude}, {longitude}): {e}")
        return None


def get_multiple_coordinates(place_names: List[str]) -> List[Optional[Dict]]:
    """
    Get coordinates for multiple places.
    
    Args:
        place_names: List of place names to search for
        
    Returns:
        List of coordinate dictionaries or None values
    """
    results = []
    for place_name in place_names:
        result = get_coordinates(place_name)
        results.append(result)
    return results

