import folium
from API.Geocoding_services import get_location
import os
import json
import random


def create_university_map(universities, country_name):
    """Create interactive map for universities"""
    os.makedirs('static/maps', exist_ok=True)
    
    try:
        # Get country center
        center = get_location(country_name)
        if not center:
            center = (51.5, 10.0)
        
        map_data = []
        m = folium.Map(location=center, zoom_start=6)
        
        # Add universities with slight random spread
        for uni in universities:
            uni_name = uni.get('name', 'N/A')
            website = uni.get('web_pages', [''])[0] if uni.get('web_pages') else ''
            country = uni.get('country', '')
            
            # Add slight randomization for visual spread
            lat = center[0] + random.uniform(-1, 1)
            lon = center[1] + random.uniform(-1, 1)
            
            # Add marker
            folium.Marker(
                location=(lat, lon),
                popup=f"<b>{uni_name}</b><br>{country}<br><a href='{website}' target='_blank'>Website</a>",
                tooltip=uni_name,
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(m)
            
            map_data.append({
                'name': uni_name,
                'country': country,
                'lat': lat,
                'lon': lon,
                'website': website
            })
        
        # Save files
        with open('static/maps/university_map.json', 'w') as f:
            json.dump(map_data, f, indent=2)
        
        m.save('static/maps/university_map.html')
        print("✓ Map created successfully!")
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
        
        m = folium.Map(location=center, zoom_start=9)
        folium.Marker(location=center, popup=country_name).add_to(m)
        m.save('static/maps/country_map.html')
        return True
    except:
        return False
