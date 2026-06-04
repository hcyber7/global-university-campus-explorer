from API.nominatim_api import get_coordinates, get_reverse_coordinates, search_universities_by_location


def get_location(place_name):
    """
    Get coordinates using Nominatim.
    
    Args:
        place_name: Name of the place to search for
        
    Returns:
        Tuple of (latitude, longitude) or None if not found
    """
    try:
        result = get_coordinates(place_name)
        if result:
            return float(result['latitude']), float(result['longitude'])
        return None
    except Exception as e:
        print(f"Error getting location for '{place_name}': {e}")
        return None


def get_country_center(country_name):
    """
    Get country center coordinates using Nominatim.
    
    Args:
        country_name: Name of the country
        
    Returns:
        Tuple of (latitude, longitude) or None if not found
    """
    try:
        return get_location(country_name)
    except Exception as e:
        print(f"Error getting country center for '{country_name}': {e}")
        return None


def get_address_from_coordinates(latitude, longitude):
    """
    Get address information from coordinates using Nominatim reverse geocoding.
    
    Args:
        latitude: Latitude coordinate
        longitude: Longitude coordinate
        
    Returns:
        Dictionary with address information or None
    """
    try:
        result = get_reverse_coordinates(latitude, longitude)
        if result and 'address' in result:
            return result
        return None
    except Exception as e:
        print(f"Error getting address from coordinates: {e}")
        return None


def get_university_region(latitude, longitude):
    """
    Get region/area information for a university location.
    
    Args:
        latitude: Latitude coordinate
        longitude: Longitude coordinate
        
    Returns:
        String with region information or None
    """
    try:
        address_info = get_reverse_coordinates(latitude, longitude)
        if address_info and 'address' in address_info:
            address_details = address_info.get('address', {})
            region = address_details.get('state') or address_details.get('province') or address_details.get('county')
            return region
        return None
    except Exception as e:
        print(f"Error getting university region: {e}")
        return None
