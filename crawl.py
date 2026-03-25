from bs4 import BeautifulSoup
import requests

def get_html(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

    return response.text

def get_listings(url):
    html = get_html(url)
    soup = BeautifulSoup(html, "html.parser")

    results = soup.find_all("a", {"data-testid": "listingDetailsAddress"})
    
    listing_links = []

    for result in results:
        listing_links.append(result.get("href"))

    return listing_links

