#!/usr/bin/env python3
"""
BBC News Scraper for RoboHormiga
Scrapes BBC News headlines and saves them to news.json
"""

import json
from datetime import datetime
import sys

try:
    import requests
    from bs4 import BeautifulSoup
    DEPENDENCIES_AVAILABLE = True
except ImportError:
    DEPENDENCIES_AVAILABLE = False


def scrape_bbc_news():
    """
    Scrape BBC News headlines and return structured data
    """
    if not DEPENDENCIES_AVAILABLE:
        print("⚠️ Dependencies not installed. Install with: pip install -r requirements.txt")
        print("📝 Creating sample data for demonstration...")
        return create_sample_data()
    
    url = "https://www.bbc.com/news"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        print("🔍 Scraping BBC News...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find headline elements (BBC News uses various selectors)
        headlines = []
        
        # Look for common headline selectors on BBC
        selectors = [
            'h3[data-testid="card-headline"]',
            '.gs-c-promo-heading__title',
            'h3.gs-c-promo-heading__title',
            'h2[data-testid="card-headline"]',
            'a[data-testid="internal-link"] h3',
        ]
        
        for selector in selectors:
            elements = soup.select(selector)
            for element in elements:
                headline_text = element.get_text(strip=True)
                if headline_text and len(headline_text) > 10:  # Filter out short/empty headlines
                    
                    # Try to find the associated link
                    link_element = element.find_parent('a') or element.find('a')
                    headline_url = ""
                    
                    if link_element and link_element.get('href'):
                        href = link_element.get('href')
                        if href.startswith('/'):
                            headline_url = f"https://www.bbc.com{href}"
                        elif href.startswith('http'):
                            headline_url = href
                    
                    headlines.append({
                        'title': headline_text,
                        'url': headline_url,
                        'source': 'BBC News',
                        'scraped_at': datetime.now().isoformat()
                    })
        
        # Remove duplicates based on title
        seen_titles = set()
        unique_headlines = []
        for headline in headlines:
            if headline['title'] not in seen_titles:
                seen_titles.add(headline['title'])
                unique_headlines.append(headline)
        
        if unique_headlines:
            print(f"✅ Found {len(unique_headlines)} unique headlines")
            return unique_headlines[:20]  # Limit to top 20 headlines
        else:
            print("⚠️ No headlines found. Creating sample data...")
            return create_sample_data()
        
    except Exception as e:
        print(f"❌ Error scraping BBC News: {e}")
        print("📝 Creating sample data for demonstration...")
        return create_sample_data()


def create_sample_data():
    """
    Create sample news data for demonstration
    """
    sample_headlines = [
        {
            'title': 'Global Climate Summit Reaches Historic Agreement on Carbon Emissions',
            'url': 'https://www.bbc.com/news/sample-1',
            'source': 'BBC News (Sample)',
            'scraped_at': datetime.now().isoformat()
        },
        {
            'title': 'Tech Giants Announce Major Investment in Renewable Energy',
            'url': 'https://www.bbc.com/news/sample-2',
            'source': 'BBC News (Sample)',
            'scraped_at': datetime.now().isoformat()
        },
        {
            'title': 'Scientists Discover Breakthrough in Cancer Treatment Research',
            'url': 'https://www.bbc.com/news/sample-3',
            'source': 'BBC News (Sample)',
            'scraped_at': datetime.now().isoformat()
        },
        {
            'title': 'New Archaeological Discovery Sheds Light on Ancient Civilizations',
            'url': 'https://www.bbc.com/news/sample-4',
            'source': 'BBC News (Sample)',
            'scraped_at': datetime.now().isoformat()
        },
        {
            'title': 'International Space Station Welcomes New Research Mission',
            'url': 'https://www.bbc.com/news/sample-5',
            'source': 'BBC News (Sample)',
            'scraped_at': datetime.now().isoformat()
        }
    ]
    return sample_headlines


def save_news_data(headlines):
    """
    Save headlines to news.json file
    """
    news_data = {
        'last_updated': datetime.now().isoformat(),
        'total_articles': len(headlines),
        'source': 'BBC News',
        'articles': headlines
    }
    
    try:
        with open('news.json', 'w', encoding='utf-8') as f:
            json.dump(news_data, f, indent=2, ensure_ascii=False)
        print(f"💾 Saved {len(headlines)} headlines to news.json")
    except Exception as e:
        print(f"❌ Error saving news data: {e}")


def main():
    """
    Main function to run the scraper
    """
    print("🤖🐜 RoboHormiga BBC News Scraper")
    print("=" * 40)
    
    headlines = scrape_bbc_news()
    
    if headlines:
        save_news_data(headlines)
        print("\n📰 Latest Headlines:")
        print("-" * 40)
        for i, headline in enumerate(headlines[:5], 1):
            print(f"{i}. {headline['title']}")
    else:
        print("⚠️ No headlines found. Creating empty news.json...")
        save_news_data([])
    
    print("\n✨ Scraping completed!")


if __name__ == "__main__":
    main()