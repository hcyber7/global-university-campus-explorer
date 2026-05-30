import requests

def get_country_info(country_name):
    """Get country information from REST Countries API"""
    try:
        url = f"https://restcountries.com/v3.1/name/{country_name}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return []
    except Exception as e:
        print(f"Error: {e}")
        return []

def get_country_flag(country_name):
    """Get country flag URL"""
    try:
        data = get_country_info(country_name)
        if data:
            return data[0].get('flags', {}).get('png', '')
        return ''
    except:
        return ''

def get_country_details(country_name):
    """Get detailed country information"""
    try:
        data = get_country_info(country_name)
        if data:
            c = data[0]
            return {
                'name': c.get('name', {}).get('common', country_name),
                'capital': (c.get('capital', ['N/A'])[0] if c.get('capital') else 'N/A'),
                'region': c.get('region', 'N/A'),
                'flag': c.get('flags', {}).get('png', ''),
                'population': c.get('population', 0),
                'area': c.get('area', 0),
            }
        return None
    except:
        return None
