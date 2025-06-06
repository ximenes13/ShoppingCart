from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time


def search_continente_selenium(product_name):
    options = Options()
    options.headless = True  # Run browser in background

    driver = webdriver.Chrome(options=options)
    driver.get(f"https://www.continente.pt/pesquisa/?q={product_name.replace(' ', '+')}")

    time.sleep(5)  # wait for JS to load content

    results = []

    products = driver.find_elements(By.CLASS_NAME, "product-card")[:5]
    for product in products:
        try:
            name = product.find_element(By.CLASS_NAME, "product-card__title").text
            price = product.find_element(By.CLASS_NAME, "sales-price__amount").text
            link = product.find_element(By.CLASS_NAME, "product-card__image-link").get_attribute("href")
            results.append({
                "name": name,
                "price": price,
                "link": link
            })
        except:
            continue

    driver.quit()
    return results

if __name__ == "__main__":
    items = search_continente_selenium("azeite")
    for item in items:
        print(item)
