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

