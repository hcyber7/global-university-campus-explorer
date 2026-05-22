from collections import Counter

def create_country_distribution_chart(universities):
    """Prepare data for country distribution chart"""
    if not universities:
        return {}
    
    countries = [u.get('country', 'Unknown') for u in universities]
    country_counts = Counter(countries)
    
    chart_data = [['Country', 'Number of Universities']]
    for country, count in sorted(country_counts.items(), key=lambda x: x[1], reverse=True):
        chart_data.append([country, count])
    
    return chart_data

def create_stats_chart(stats):
    """Prepare data for statistics charts"""
    return {
        'searches': stats.get('total_searches', 0),
        'favorites': stats.get('total_favorites', 0),
        'countries': stats.get('unique_countries', 0)
    }
