import folium
from API.Geocoding_services import get_location
import os
import json


def create_university_map(universities, country_name):
    """Create map with university locations"""
    os.makedirs('static/maps', exist_ok=True)
    
    try:
        # Get country center coordinates
        country_coords = get_location(country_name)
        
        # Hardcoded country centers (fallback)
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
        
        # Use coordinates if available, else use hardcoded center
        if country_coords:
            center = country_coords
        else:
            center = country_centers.get(country_name, (51.5, 10.0))
        
        map_data = []
        
        # Create map with universities
        m = folium.Map(location=center, zoom_start=6)
        
        for uni in universities:
            uni_name = uni.get('name', 'N/A')
            website = uni.get('web_pages', [''])[0] if uni.get('web_pages') else ''
            country = uni.get('country', '')
            state = uni.get('state-province', 'N/A')
            
            # Use center point for all universities (all in same country)
            lat, lon = center
            
            # Add marker to map
            folium.Marker(
                location=(lat, lon),
                popup=f"<b>{uni_name}</b><br>Country: {country}<br>State: {state}<br><a href='{website}' target='_blank'>Website</a>",
                tooltip=uni_name,
                icon=folium.Icon(color='blue', icon='info-sign')
            ).add_to(m)
            
            map_data.append({
                'name': uni_name,
                'country': country,
                'state': state,
                'lat': lat,
                'lon': lon,
                'website': website
            })
        
        # Save as JSON
        map_file = 'static/maps/university_map.json'
        with open(map_file, 'w') as f:
            json.dump(map_data, f, indent=2)
        
        # Save as HTML
        folium_file = 'static/maps/university_map.html'
        m.save(folium_file)
        
        print(f"✓ Map created: {folium_file}")
        return True
        
    except Exception as e:
        print(f"Map error: {e}")
        import traceback
        traceback.print_exc()
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
    except Exception as e:
        print(f"Error creating country map: {e}")
        return False
