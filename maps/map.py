import folium
from api.geocoding_services import get_location
import os

def create_university_map(universities, country_name):
    """Create an interactive map showing universities"""
    os.makedirs('static/maps', exist_ok=True)
    
    try:
        center_coords = get_location(country_name)
        if not center_coords:
            center_coords = (20, 0)
        
        m = folium.Map(location=center_coords, zoom_start=4)
        
        for uni in universities:
            coords = get_location(f"{uni.get('name', '')} {country_name}")
            if coords:
                folium.Marker(
                    location=coords,
                    popup=f"<b>{uni.get('name', 'N/A')}</b><br>{uni.get('country', '')}",
                    tooltip=uni.get('name', 'University'),
                    icon=folium.Icon(color='blue', icon='info-sign')
                ).add_to(m)
        
        map_file = 'static/maps/university_map.html'
        m.save(map_file)
        return True
    except Exception as e:
        print(f"Map error: {e}")
        return False

def create_country_map(country_name):
    """Create a simple map for a country"""
    os.makedirs('static/maps', exist_ok=True)
    
    try:
        center = get_location(country_name)
        if not center:
            center = (20, 0)
        
        m = folium.Map(location=center, zoom_start=5)
        folium.Marker(location=center, popup=country_name).add_to(m)
        
        map_file = 'static/maps/country_map.html'
        m.save(map_file)
        return True
    except:
        return False
