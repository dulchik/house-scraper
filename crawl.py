from bs4 import BeautifulSoup
import requests
from dotenv import load_dotenv
import os


load_dotenv()

URL = os.getenv("URL")

def get_soup(url):
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    soup = BeautifulSoup(response.text, "html.parser")

    return soup

soup = get_soup(URL)


def get_listings():
    results = soup.find_all("a", {"data-testid": "listingDetailsAddress"})
    
    listing_links = []

    for result in results:
        listing_links.append(result.get("href"))

    return listing_links

def get_addresses():
    results = soup.find_all("div", {"class": "@container"})
    addresses = []

    for result in results:
        street = result.find_all("span", {"class": "truncate"})
        place = result.find_all("div", {"class": "truncate"})

        address = " ".join(street[0].text.split()) + " " + place[0].text.strip()
        addresses.append(address)

    return addresses

def get_prices_and_details():
    results = soup.find_all("div", {"class": "@container"})
    prices = []
    uls = []

    for result in results:
        details = result.find_all("div", {"class": "mt-2"})
        price = details[0].find_all("div", {"class": "truncate"})

        ul = details[0].find_all("ul")
        uls.append(ul)

        prices.append(price[0].text)

    details = []
    for ul in uls:
        for li in ul:
            li_spans = li.find_all("span")
            if len(li_spans) > 3:
                li_spans.pop(1)

            spans = []
            for li_span in li_spans:
                spans.append(li_span.text)

            details.append(spans)

    return prices, details
