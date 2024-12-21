import requests
from bs4 import BeautifulSoup

def fetch_page(url):
    response = requests.get(url)
    return response.text

def parse_quotes(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    quotes = soup.find_all('span', class_='text')
    authors = soup.find_all('small', class_='author')
    return [(q.get_text(), a.get_text()) for q, a in zip(quotes, authors)]

if __name__ == "__main__":
    url = "http://quotes.toscrape.com/"
    html_content = fetch_page(url)
    for quote, author in parse_quotes(html_content):
        print(f"{quote} - {author}")
