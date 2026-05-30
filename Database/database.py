import sqlite3
from datetime import datetime
import os

DB_PATH = 'data/universities.db'

def init_db():
    """Initialize database with required tables"""
    os.makedirs('data', exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS universities (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        country TEXT NOT NULL,
        website TEXT,
        domain TEXT,
        added_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS search_history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        query TEXT NOT NULL,
        results_count INTEGER,
        search_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        university_id INTEGER UNIQUE,
        name TEXT NOT NULL,
        country TEXT NOT NULL,
        website TEXT,
        saved_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(university_id) REFERENCES universities(id)
    )''')
    
    conn.commit()
    conn.close()

def add_university_to_search(name, country, website, domain):
    """Add a university to the database"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''INSERT INTO universities (name, country, website, domain) 
                 VALUES (?, ?, ?, ?)''',
              (name, country, website, domain))
    
    conn.commit()
    conn.close()

def record_search(query, results_count):
    """Record a search in history"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''INSERT INTO search_history (query, results_count) 
                 VALUES (?, ?)''',
              (query, results_count))
    
    conn.commit()
    conn.close()

def add_to_favorites(name, country, website):
    """Add university to favorites"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('''INSERT OR IGNORE INTO favorites (name, country, website) 
                 VALUES (?, ?, ?)''',
              (name, country, website))
    
    conn.commit()
    conn.close()

def get_favorites():
    """Get all favorite universities"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT name, country, website FROM favorites ORDER BY saved_date DESC')
    favorites = [{'name': row[0], 'country': row[1], 'website': row[2]} for row in c.fetchall()]
    
    conn.close()
    return favorites

def get_search_history():
    """Get search history"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT query, results_count, search_date FROM search_history ORDER BY search_date DESC LIMIT 10')
    history = [{'query': row[0], 'count': row[1], 'date': row[2]} for row in c.fetchall()]
    
    conn.close()
    return history

def get_stats():
    """Get application statistics"""
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    
    c.execute('SELECT COUNT(*) FROM search_history')
    total_searches = c.fetchone()[0]
    
    c.execute('SELECT COUNT(*) FROM favorites')
    total_favorites = c.fetchone()[0]
    
    c.execute('SELECT COUNT(DISTINCT country) FROM universities')
    unique_countries = c.fetchone()[0]
    
    conn.close()
    
    return {
        'total_searches': total_searches,
        'total_favorites': total_favorites,
        'unique_countries': unique_countries
    }

def remove_favorite(name):  # Remove a university from favorites by name

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute(
        "DELETE FROM favorites WHERE name = ?",
        (name,)
    )

    conn.commit()
    conn.close()


def clear_all_favorites(): # Clear all entries from the favorites table

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    c.execute("DELETE FROM favorites")

    conn.commit()
    conn.close()