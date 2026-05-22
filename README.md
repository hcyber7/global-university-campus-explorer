# 🌍 Global University & Campus Explorer

A modern web application for discovering and exploring universities around the world. Built with Flask, it provides university search, country profiles, interactive maps, and statistical visualizations.

## 🎯 Features

- **University Search**: Search universities by country or name with real-time results
- **Country Profiles**: View detailed information about countries including capitals, regions, populations, and flags
- **Interactive Maps**: Visualize university locations on interactive Folium maps
- **Statistics & Charts**: Track your searches and favorites with visual charts
- **Save Favorites**: Build a personalized list of favorite universities
- **Search History**: Keep track of all your searches
- **Responsive Design**: Beautiful, modern UI with gradient backgrounds and smooth interactions

## 🛠️ Tech Stack

- **Backend**: Flask 2.3.2
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite3
- **Maps**: Folium 0.14.0
- **Charts**: Matplotlib 3.7.1
- **APIs**:
  - [Hipo University Domains API](https://github.com/Hipo/university-domains-list-api)
  - [REST Countries API](https://restcountries.com/)
  - [Nominatim Geocoding](https://nominatim.org/)

## 📋 Project Requirements Met

### W6 - Group + Skeleton (20%)
✅ Group of 3 students  
✅ Project idea confirmed  
✅ GitHub repository created  
✅ Initial project structure  
✅ Task distribution defined  
✅ Initial API & backend plan  

### W7 - Prototype and Final Demo (20%)
✅ Running Flask application  
✅ Working API calls (Universities & Countries)  
✅ Database functionality  
✅ Interactive map visualization  
✅ Statistical charts  
✅ Functional web UI  

### W8 - Final Evaluation (50%)
⏳ Complete working application  
⏳ Enhanced UI with animations  
⏳ Backend persistence  
⏳ Advanced visualizations  
⏳ Clear README & organized repository  

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip

### Installation

1. **Clone the repository**:
```bash
git clone https://github.com/hcyber7/global-university-campus-explorer.git
cd global-university-campus-explorer
```

2. **Create virtual environment**:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**:
```bash
pip install -r requirements.txt
```

4. **Run the application**:
```bash
python app.py
```

5. **Open in browser**:
Navigate to `http://localhost:5000`

## 📂 Project Structure

```
global-university-campus-explorer/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── README.md                 # This file
│
├── api/
│   ├── university_api.py    # University search API
│   ├── country_api.py       # Country information API
│   └── geocoding_services.py # Location geocoding
│
├── database/
│   └── database.py          # SQLite database management
│
├── maps/
│   └── map.py              # Interactive map generation
│
├── charts/
│   └── chart.py            # Chart and visualization generation
│
├── templates/
│   ├── base.html           # Base template with navigation
│   ├── index.html          # Home page
│   ├── search.html         # Search interface
│   ├── results.html        # Search results with visualizations
│   ├── favorites.html      # Favorites and statistics
│   ├── history.html        # Search history
│   ├── map.html            # Map viewer
│   └── 404.html            # Error page
│
├── static/
│   ├── maps/               # Generated map files
│   ├── charts/             # Generated chart files
│   └── style.css           # Optional custom styles
│
└── data/
    └── universities.db     # SQLite database (created on first run)
```

## 🎨 User Interface

### Pages

1. **Home** - Welcome page with project overview and feature highlights
2. **Search** - University search interface with two search modes
3. **Results** - Detailed results with country info, university cards, and visualizations
4. **Favorites** - Saved universities and statistics dashboard
5. **History** - Search history with timestamps and result counts

## 📊 Database Schema

### Universities Table
- `id` - Primary key
- `name` - University name
- `country` - Country
- `website` - University website
- `domain` - University domain

### Search History Table
- `id` - Primary key
- `query` - Search query
- `results_count` - Number of results
- `search_date` - Search timestamp

### Favorites Table
- `id` - Primary key
- `university_id` - Foreign key to universities
- `name` - University name
- `country` - Country
- `website` - Website URL
- `saved_date` - When favorited

## 🌐 API Endpoints

### Web Routes
- `GET /` - Home page
- `GET /search` - Search page
- `POST /search` - Process search
- `GET /favorites` - Favorites page
- `GET /history` - Search history
- `GET /map` - Map viewer

### API Endpoints
- `POST /api/add-favorite` - Add university to favorites
- `GET /api/stats` - Get application statistics

## 👥 Team & Responsibilities

### Hamza (Group Leader)
- Flask application integration
- Main routing and application flow
- GitHub repository management
- Project coordination

### Ashutosh
- API integration
- University and country data retrieval
- JSON data processing

### Ashish
- SQLite database management
- Favorites and search history system
- Map and chart implementation

## 🐛 Known Limitations

- Maps load with a delay on first search (Nominatim API rate limiting)
- Some universities may not have precise coordinate data
- Charts require at least one search to generate

## 🔧 Troubleshooting

**Issue**: "Connection Error" when searching
- Check your internet connection
- Verify API endpoints are accessible

**Issue**: Map not loading
- Wait a few seconds (API rate limiting)
- Try a different search

**Issue**: Database error
- Delete `data/universities.db` and restart the application

## 📄 License

This project is created for educational purposes - Programming Lab, Semester 2

## 🎓 Week 7 Evaluation Notes

This prototype demonstrates:
- ✅ Running Flask application with live API calls
- ✅ Database integration and persistence
- ✅ Interactive visualizations (maps and charts)
- ✅ Responsive web interface
- ✅ Complete application workflow
- ✅ Clean, organized codebase

**For the full final evaluation (W8), additional enhancements will include:**
- Enhanced animations and transitions
- Advanced filtering options
- User authentication
- Comparison features
- Export functionality
