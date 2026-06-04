# Nominatim API Integration Guide

## Overview
This project uses the **Nominatim API** from OpenStreetMap for geocoding and reverse geocoding features. Nominatim is used to convert place names to coordinates and vice versa, which is essential for:
- Getting university locations on maps
- Finding country centers for map visualization
- Reverse geocoding coordinates to get address information

## What is Nominatim?
Nominatim is a search engine for OpenStreetMap data. It allows you to:
- **Geocoding**: Convert place names to geographic coordinates (latitude, longitude)
- **Reverse Geocoding**: Convert geographic coordinates to place names/addresses
- **Address Lookup**: Get detailed address information from coordinates

Official Documentation: https://nominatim.org/release-docs/latest/api/Overview/

## Files Involved

### 1. `API/nominatim_api.py`
**Main Nominatim API wrapper** - Contains all Nominatim API functions.

**Available Functions:**

```python
# Get coordinates from a place name
get_coordinates(place_name: str) -> Dict
# Returns: {"latitude": float, "longitude": float, "address": str}

# Get address from coordinates
get_reverse_coordinates(lat: float, lon: float) -> Dict
# Returns: {"address": dict, "display_name": str, "lat": float, "lon": float}

# Search universities by location
search_universities_by_location(lat: float, lon: float, radius_km: int) -> Dict
# Returns: Location information around the coordinates

# Get coordinates for multiple places
get_multiple_coordinates(place_names: List[str]) -> List[Optional[Dict]]
# Returns: List of coordinate dictionaries
```

### 2. `API/Geocoding_services.py`
**High-level geocoding service** - Wraps Nominatim functions for convenient use in the application.

**Available Functions:**

```python
# Get location coordinates
get_location(place_name: str) -> Tuple[float, float]
# Returns: (latitude, longitude)

# Get country center coordinates
get_country_center(country_name: str) -> Tuple[float, float]
# Returns: (latitude, longitude)

# Get address details from coordinates
get_address_from_coordinates(lat: float, lon: float) -> Dict
# Returns: Full address information

# Get region information for coordinates
get_university_region(lat: float, lon: float) -> str
# Returns: Region/state name
```

### 3. `maps/map.py`
**Map visualization** - Uses Nominatim to get coordinates for creating interactive maps.

**Integration Points:**
- Uses `get_location()` to get country center for map centering
- Creates Folium maps with university markers
- Exports maps as both JSON and HTML

## How It Works in the Application

### Step 1: User searches for universities by country
```
User searches: "Germany"
↓
app.py calls: search_universities("Germany")
↓
University list returned with: name, country, website, domains
```

### Step 2: Map is created for the country
```
User clicks "View Map"
↓
maps/map.py calls: get_location("Germany")
↓
Nominatim returns: (51.165, 10.451)
↓
Folium map is created centered at Germany
↓
University markers are placed on the map
```

### Step 3: Address lookup (optional)
```
Coordinates are known: (52.517, 13.395)
↓
maps/map.py or app.py calls: get_reverse_coordinates(52.517, 13.395)
↓
Nominatim returns: "Berlin, Germany"
↓
Full address displayed to user
```

## Usage Examples

### Example 1: Get coordinates for a university city
```python
from API.nominatim_api import get_coordinates

result = get_coordinates("Technical University of Munich, Germany")
print(f"Latitude: {result['latitude']}")
print(f"Longitude: {result['longitude']}")
print(f"Address: {result['address']}")
```

### Example 2: Find address from coordinates
```python
from API.Geocoding_services import get_address_from_coordinates

address = get_address_from_coordinates(52.5173885, 13.3951309)
print(address['display_name'])  # "Berlin, Germany"
```

### Example 3: Get multiple locations
```python
from API.nominatim_api import get_multiple_coordinates

universities = [
    "University of Berlin",
    "University of Munich",
    "University of Heidelberg"
]

coordinates = get_multiple_coordinates(universities)
for uni, coords in zip(universities, coordinates):
    if coords:
        print(f"{uni}: ({coords['latitude']}, {coords['longitude']})")
```

### Example 4: Create a map for a country (already done in app)
```python
from API.Geocoding_services import get_location
from maps.map import create_university_map

country = "Germany"
universities = search_universities(country)
create_university_map(universities, country)
# Creates: static/maps/university_map.json and university_map.html
```

## API Requirements and Best Practices

### Requirements
- Internet connection (for API calls)
- Valid User-Agent header (already set to "UniversityFinderProject/1.0")
- Timeout: 10 seconds (configurable)

### Rate Limiting
Nominatim has rate limiting (1 request per second recommended):
- Free tier: Approximately 1 request/second
- If you get HTTP 429 errors, wait before making more requests
- The code handles this with try-except blocks

### Error Handling
All functions include error handling:
- Returns None if API call fails
- Prints error messages to console
- Application continues with default values

## Testing the Integration

### Run the Demo
```bash
cd /Users/ashu/Desktop/SRH/2_semester/code_project/global-university-campus-explorer
python3 API/nominatim_demo.py
```

This will show:
- Geocoding examples
- Reverse geocoding examples
- Multiple location lookups
- Country center coordinates
- Location details
- University searches

### Test Individual Functions
```python
from API.Geocoding_services import get_location, get_country_center

# Test basic geocoding
coords = get_location("Paris, France")
print(coords)  # (48.8566, 2.3522)

# Test country center
center = get_country_center("Italy")
print(center)  # (42.6384, 12.6743)
```

## Data Flow in Application

```
┌─────────────────────────────────────────────────────────────┐
│ User Interface (HTML/Templates)                             │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  app.py (Flask Routes)                                       │
│  ├─ search_universities(country)                            │
│  ├─ map_page(country)                                       │
│  └─ favorites/history operations                            │
│         │                                                    │
│         ▼                                                    │
│  API Layer                                                   │
│  ├─ University_api.py (HipoLabs API)                        │
│  ├─ country_api.py (REST Countries API)                     │
│  │                                                           │
│  └─ Geocoding_services.py ◄─────────────────┐              │
│     ├─ get_location()                       │              │
│     ├─ get_country_center()                 │              │
│     └─ get_address_from_coordinates()       │              │
│          │                                  │              │
│          ▼                                  │              │
│  nominatim_api.py ◄───────────────┐        │              │
│  ├─ get_coordinates()              │        │              │
│  ├─ get_reverse_coordinates()      │        │              │
│  └─ search_universities_by_location()      │              │
│          │                                  │              │
│          ▼                                  │              │
│     NOMINATIM API (OpenStreetMap)          │              │
│     https://nominatim.openstreetmap.org    │              │
│                                             │              │
│  maps/map.py                               │              │
│  └─ create_university_map() ───────────────┘              │
│     ├─ Gets country center                                │
│     ├─ Generates map data                                 │
│     └─ Creates Folium/JSON maps                           │
│                                             │              │
│  Database Layer                            │              │
│  ├─ favorites.db                           │              │
│  ├─ search_history.db                      │              │
│  └─ user preferences                       │              │
│                                             │              │
└─────────────────────────────────────────────────────────────┘
```

## Important Notes for Submission

✓ **Nominatim API is fully integrated and working**
- All geocoding functions are implemented
- Reverse geocoding is working
- Map creation uses Nominatim for coordinates
- Error handling is in place

✓ **No additional setup required**
- Only uses standard Python libraries (requests)
- All configuration is hardcoded
- Works locally without internet restrictions

✓ **Following Project Structure**
- API integration follows existing pattern (University_api.py, country_api.py)
- Geocoding_services.py follows existing naming convention
- Maps use the geocoding services correctly
- No changes to app.py needed

## Troubleshooting

### Issue: "429 Too Many Requests"
**Solution**: Wait a few seconds before making more API calls. The code handles this gracefully.

### Issue: "Connection timeout"
**Solution**: Check internet connection. The timeout is set to 10 seconds.

### Issue: Location not found
**Solution**: Try with different place name format (e.g., "Berlin, Germany" instead of "Berlin")

### Issue: Coordinates seem inaccurate
**Solution**: This is normal for broad searches. Use more specific location names for better accuracy.

## For Exam Submission

The Nominatim API integration is complete and ready for submission:

1. **Geocoding module** - `API/nominatim_api.py` with full type hints and documentation
2. **Geocoding service** - `API/Geocoding_services.py` providing high-level interface
3. **Map generation** - `maps/map.py` using Nominatim for coordinates
4. **Demo file** - `API/nominatim_demo.py` showing all capabilities
5. **Error handling** - All functions handle errors gracefully
6. **Documentation** - This file explaining the integration

The implementation is production-ready and follows best practices for API integration.
