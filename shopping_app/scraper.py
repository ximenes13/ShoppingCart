from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from urllib.parse import quote_plus
import time

def get_price_continente(product_name):
    chrome_path = r"C:\Users\anaxg\Downloads\chromedriver-win64\chromedriver.exe"

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')

    service = Service(executable_path=chrome_path)
    driver = webdriver.Chrome(service=service, options=options)

    try:
        query = quote_plus(product_name)
        url = f"https://www.continente.pt/pesquisa/?q={query}"
        driver.get(url)
        time.sleep(5)

        # Vai para a página do primeiro produto encontrado
        product_links = driver.find_elements(By.CSS_SELECTOR, 'a.ct-product-card')
        if not product_links:
            return "Produto não encontrado"
        product_links[0].click()
        time.sleep(3)

        # Extrai o nome do produto
        title = driver.find_element(By.CSS_SELECTOR, 'h1.product-name').text

        # Extrai o preço do produto
        price = driver.find_element(By.CSS_SELECTOR, 'span.ct-price-formatted').text

        return f"{title}: {price}"
    except Exception as e:
        return f"Erro: {str(e)}"
    finally:
        driver.quit()
