import requests
from bs4 import BeautifulSoup
import pandas as pd

print("Starting Web Scraping...")

# 1. Send request to website
url = "http://quotes.toscrape.com/"
response = requests.get(url)

# 2. Parse HTML
soup = BeautifulSoup(response.text, 'html.parser')

# 3. Extract data
quotes = []
authors = []
tags = []

all_quotes = soup.find_all('div', class_='quote')

for quote in all_quotes:
    text = quote.find('span', class_='text').text
    author = quote.find('small', class_='author').text
    tag_list = [t.text for t in quote.find_all('a', class_='tag')]
    tag = ", ".join(tag_list)
    
    quotes.append(text)
    authors.append(author)
    tags.append(tag)

# 4. Save to DataFrame and CSV
df = pd.DataFrame({
    'Quote': quotes,
    'Author': authors,
    'Tags': tags
})

df.to_csv('scraped_quotes.csv', index=False)

print("\n=== SCRAPING COMPLETE ===")
print(df)
print(f"\nTotal {len(df)} quotes saved to 'scraped_quotes.csv'")