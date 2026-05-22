# 🎓 W7 Evaluation Demo Guide

## Quick Start (< 2 minutes)

### 1. Setup
```bash
# Clone repo (if not already done)
git clone https://github.com/hcyber7/global-university-campus-explorer.git
cd global-university-campus-explorer

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Run Application
```bash
python app.py
```

Then open: **http://localhost:5000**

## Demo Workflow (5-10 minutes)

### Slide 1: Home Page
- Show the hero section with project overview
- Highlight the 6 feature cards
- Demonstrate responsive design

### Slide 2: University Search
Navigate to `/search` page:
1. **Search by Country**: Search "Germany"
   - Show country profile with flag, capital, region, population
   - Display university results in cards
   - Show website and domain information

2. **Search by University Name**: Search "Harvard"
   - Show specific university results

### Slide 3: Data Visualizations
On results page, show:
1. **Interactive Map** 
   - Folium map with university locations
   - Zoom and pan functionality
   - Markers for each university

2. **Google Charts Distribution Chart**
   - Bar chart showing universities by country
   - Dynamic data based on search results

### Slide 4: Favorites Management
Navigate to `/favorites`:
1. Add universities from search results (⭐ button)
2. View saved favorites
3. Show statistics:
   - Total searches
   - Total favorites
   - Unique countries explored

4. Show Google Charts statistics visualization:
   - Bar chart with metrics

### Slide 5: Search History
Navigate to `/history`:
- Show all previous searches with timestamps
- Display result counts
- Demonstrate persistence across sessions

## Technical Highlights

✅ **Working APIs**:
   - Hipo University API (search functionality)
   - REST Countries API (country info & flags)
   - Nominatim Geocoding (map coordinates)

✅ **Database**:
   - SQLite3 with 3 tables
   - Persistent storage of searches, favorites, universities
   - Statistics tracking

✅ **Visualizations**:
   - Folium interactive maps
   - Google Charts (bar charts, statistics)

✅ **UI/UX**:
   - Responsive design
   - Gradient backgrounds
   - Smooth transitions
   - Accessibility features

## Key Features to Demonstrate

1. **Search Functionality**
   - Type in search query
   - Instant API results
   - Multiple universities display

2. **Country Profile**
   - Flag display
   - Capital, region, population
   - Area in km²

3. **Data Persistence**
   - Search history saved
   - Favorites saved
   - Statistics tracked

4. **Interactive Elements**
   - Add to favorites buttons
   - Visit website links
   - Clickable map markers

5. **Charts & Graphs**
   - Real-time data visualization
   - Google Charts rendering
   - Statistics dashboard

## Troubleshooting

**Issue**: "Connection Error" when searching
- Check internet connection
- APIs may have rate limiting

**Issue**: Map not loading
- Wait a few seconds (Nominatim can be slow)
- Try a different search

**Issue**: Database error
```bash
rm -rf data/universities.db
python app.py  # Restart
```

## Project Status

### W6 Completed ✅
- Group formed (3 students)
- Project scope defined
- GitHub repository created
- Initial structure established

### W7 Completed ✅
- Full Flask application running
- All APIs integrated and working
- Database with 3 tables
- Interactive maps with Folium
- Google Charts visualizations
- Responsive web UI
- Search history & favorites system

### W8 Goals
- Enhanced UI animations
- Advanced filtering
- User authentication
- Comparison features
- Export functionality

## Presentation Notes

- **Duration**: 5-10 minutes demo
- **Focus**: Working application with real data
- **Highlight**: Database persistence and visualizations
- **Strengths**: 
  - Clean, modern UI
  - Real-time API integration
  - Full data flow (search → database → visualization)
  - Responsive design

## Files to Know

```
Key Files:
- app.py                    - Main Flask application (200 lines)
- api/university_api.py    - University search API
- api/country_api.py       - Country information API
- database/database.py     - SQLite management (150 lines)
- maps/map.py             - Folium map generation
- charts/chart.py         - Google Charts data preparation
- templates/              - 8 beautiful HTML templates
```

## Success Criteria Met

✅ Running sample code with API calls  
✅ Working database flow  
✅ Map/chart generation (Google Charts + Folium)  
✅ First end-to-end demo  
✅ Clean repository and README  
✅ Organized project structure  
✅ Responsive web interface  
✅ Full CRUD operations for favorites  

