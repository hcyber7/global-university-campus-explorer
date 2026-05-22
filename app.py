from flask import Flask, render_template, request, jsonify
from api.university_api import search_universities, search_universities_by_name
from api.country_api import get_country_details
from database.database import init_db, record_search, add_to_favorites, get_favorites, get_search_history, get_stats
from maps.map import create_university_map, create_country_map
from charts.chart import create_country_distribution_chart, create_stats_chart
import os
import json

app = Flask(__name__)
init_db()

@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    """Search page and handler"""
    if request.method == 'POST':
        search_query = request.form.get('query', '').strip()
        search_type = request.form.get('type', 'country')
        
        if not search_query:
            return render_template('results.html', error="Please enter a search query", results=[], chart_data='[]')
        
        try:
            if search_type == 'country':
                results = search_universities(search_query)
            else:
                results = search_universities_by_name(search_query)
            
            record_search(search_query, len(results))
            
            # Get country info
            country_info = get_country_details(search_query) if search_type == 'country' else None
            
            # Create visualizations
            chart_data = []
            if results:
                chart_data = create_country_distribution_chart(results)
                create_university_map(results, search_query)
            
            return render_template('results.html', 
                                 results=results, 
                                 query=search_query, 
                                 country_info=country_info,
                                 search_type=search_type,
                                 chart_data=json.dumps(chart_data))
        except Exception as e:
            return render_template('results.html', error=f"Search error: {str(e)}", results=[], chart_data='[]')
    
    return render_template('search.html')

@app.route('/favorites')
def favorites():
    """View and manage favorites"""
    favorites_list = get_favorites()
    stats = get_stats()
    return render_template('favorites.html', favorites=favorites_list, stats=stats)

@app.route('/history')
def history():
    """View search history"""
    search_history = get_search_history()
    return render_template('history.html', history=search_history)

@app.route('/api/add-favorite', methods=['POST'])
def add_favorite():
    """API endpoint to add to favorites"""
    try:
        data = request.json
        add_to_favorites(data.get('name'), data.get('country'), data.get('website'))
        return jsonify({'success': True}), 200
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 400

@app.route('/map')
def view_map():
    """View the generated map"""
    return render_template('map.html')

@app.route('/api/stats')
def api_stats():
    """Get application statistics"""
    return jsonify(get_stats())

@app.errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(e):
    return render_template('500.html'), 500

if __name__ == '__main__':
    os.makedirs('static/maps', exist_ok=True)
    os.makedirs('data', exist_ok=True)
    app.run(debug=True, host='0.0.0.0', port=5000)
