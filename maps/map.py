import folium
from API.Geocoding_services import get_location
import os
import json
import random

def create_university_map(universities, country_name):
    """Create map data for D3 visualization"""
    os.makedirs('static/maps', exist_ok=True)
    
    try:
        # Get country center coordinates for clustering
        country_coords = get_location(country_name)
        if not country_coords:
            country_coords = (51.5, 10.0)  # Default to Europe center
        
        # Map of countries to approximate coordinates (for better distribution)
        country_centers = {
            'Germany': (51.165126, 10.451526),
            'United States': (37.0902, -95.7129),
            'United Kingdom': (55.3781, -3.4360),
            'France': (46.2276, 2.2137),
            'Spain': (40.4637, -3.7492),
            'Italy': (41.8719, 12.5674),
            'Netherlands': (52.1326, 5.2913),
            'Belgium': (50.5039, 4.4699),
            'Austria': (47.5162, 14.5501),
            'Switzerland': (46.8182, 8.2275),
            'Japan': (36.2048, 138.2529),
            'China': (35.8617, 104.1954),
            'India': (20.5937, 78.9629),
            'Brazil': (-14.2350, -51.9253),
            'Canada': (56.1304, -106.3468),
        }
        
        center = country_centers.get(country_name, country_coords)
        
        map_data = []
        # Add slight randomization to coordinates for better visualization
        for i, uni in enumerate(universities):
            # Generate approximate coordinates around country center
            # This creates a spread pattern for visualization
            lat_offset = random.uniform(-3, 3)
            lon_offset = random.uniform(-3, 3)
            
            lat = center[0] + lat_offset
            lon = center[1] + lon_offset
            
            map_data.append({
                'name': uni.get('name', 'N/A'),
                'country': uni.get('country', ''),
                'lat': lat,
                'lon': lon,
                'website': uni.get('web_pages', [''])[0] if uni.get('web_pages') else ''
            })
        
        # Save as JSON for D3
        map_file = 'static/maps/university_map.json'
        with open(map_file, 'w') as f:
            json.dump(map_data, f)
        
        # Also create Folium backup map
        m = folium.Map(location=center, zoom_start=6)
        
        for uni_data in map_data:
            folium.Marker(
                location=(uni_data['lat'], uni_data['lon']),
                popup=f"<b>{uni_data['name']}</b><br>{uni_data['country']}",
                tooltip=uni_data['name'],
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(m)
        
        folium_file = 'static/maps/university_map.html'
        m.save(folium_file)
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
        
        map_file = 'static/maps/country_map.html'
        m.save(map_file)
        return True
    except:
        return False
