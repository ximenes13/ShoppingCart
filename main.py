from continente_scraper import search_continente_selenium

if __name__ == "__main__":
    food = input("Enter food name: ")
    results = search_continente_selenium(food)

    if results:
        print(f"\nTop results for '{food}' on Continente:\n")
        for item in results:
            print(f"{item['name']}")
            print(f"Price: {item['price']}")
            print(f"Link: {item['link']}\n")
    else:
        print("No results found.")
