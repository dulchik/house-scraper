from crawl import get_listings, get_addresses 


def main():
    l = get_listings()
    a = get_addresses()
    
    print(a)

if __name__ == "__main__":
    main()
