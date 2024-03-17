import requests
from bs4 import BeautifulSoup
import json
from urllib.parse import urljoin

def scrape_quotes(url):
    all_quotes = []
    all_authors = set()
    while url:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        quotes = soup.find_all('div', class_='quote')
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            all_quotes.append({'quote': text, 'author': author, 'tags': tags})
            all_authors.add(author)
        next_button = soup.find('li', class_='next')
        if next_button:
            url = urljoin(url, next_button.find('a')['href'])
        else:
            url = None
    return all_quotes, all_authors

def save_quotes_to_json(quotes, filename):
    with open(filename, 'w') as file:
        json.dump(quotes, file, indent=4)

def save_authors_to_json(authors, filename):
    with open(filename, 'w') as file:
        json.dump(list(authors), file, indent=4)

if __name__ == "__main__":
    first_page_url = 'http://quotes.toscrape.com'
    all_quotes, all_authors = scrape_quotes(first_page_url)
    save_quotes_to_json(all_quotes, 'quotes.json')
    save_authors_to_json(all_authors, 'authors.json')
