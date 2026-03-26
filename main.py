from crawl import get_listings, get_addresses, get_prices_and_details


def main():
    l = get_listings()
    a = get_addresses()
    p = get_prices_and_details()


    print(l)
    print(a)
    print(p)

if __name__ == "__main__":
    main()
