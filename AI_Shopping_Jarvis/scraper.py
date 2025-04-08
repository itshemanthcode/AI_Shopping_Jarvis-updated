from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time


def create_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    return webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


def parse_price(price_str):
    return float(price_str.replace("₹", "").replace(",", "").strip())


def get_amazon_products(query):
    driver = create_driver()
    driver.get(f"https://www.amazon.in/s?k={query.replace(' ', '+')}")
    time.sleep(3)

    products = []
    results = driver.find_elements(By.XPATH, '//div[@data-component-type="s-search-result"]')
    for item in results[:20]:
        try:
            title = item.find_element(By.TAG_NAME, 'h2').text
            link = item.find_element(By.TAG_NAME, 'a').get_attribute('href')
            price = item.find_element(By.CLASS_NAME, 'a-price-whole').text
            rating = item.find_element(By.CLASS_NAME, 'a-icon-alt').get_attribute('innerHTML')
            rating_value = float(rating.split()[0])
            if rating_value >= 4.0:
                products.append({
                    'title': title,
                    'price': f"₹{price}",
                    'rating': str(rating_value),
                    'link': link,
                    'platform': 'Amazon'
                })
        except:
            continue
    driver.quit()
    return products


def get_flipkart_products(query):
    driver = create_driver()
    driver.get(f"https://www.flipkart.com/search?q={query.replace(' ', '%20')}")
    time.sleep(3)

    products = []
    cards = driver.find_elements(By.CLASS_NAME, '_1AtVbE')
    for card in cards:
        try:
            title = card.find_element(By.CLASS_NAME, '_4rR01T').text
            price = card.find_element(By.CLASS_NAME, '_30jeq3').text
            rating = card.find_element(By.CLASS_NAME, '_3LWZlK').text
            rating_value = float(rating)
            link = card.find_element(By.TAG_NAME, 'a').get_attribute('href')
            if rating_value >= 4.0:
                products.append({
                    'title': title,
                    'price': price,
                    'rating': rating,
                    'link': f"https://www.flipkart.com{link}",
                    'platform': 'Flipkart'
                })
        except:
            continue
        if len(products) >= 20:
            break
    driver.quit()
    return products


def get_brand_store_product(query):
    brand_links = {
        "iphone": "https://www.apple.com/in/shop/buy-iphone",
        "macbook": "https://www.apple.com/in/shop/buy-mac",
        "ipad": "https://www.apple.com/in/ipad/",
        "airpods": "https://www.apple.com/in/airpods/",
        "samsung": "https://www.samsung.com/in/search/?searchvalue=",
        "oneplus": "https://www.oneplus.in/search?keyword=",
        "boat": "https://www.boat-lifestyle.com/search?q=",
        "asus": "https://www.asus.com/in/searchresult?searchKey=",
    }

    driver = create_driver()
    products = []
    for keyword, base_url in brand_links.items():
        if keyword in query.lower():
            try:
                brand_url = base_url + query.replace(" ", "+") if base_url.endswith("=") else base_url
                driver.get(brand_url)
                time.sleep(3)
                products.append({
                    "title": f"{query.title()} (Official Store)",
                    "price": "-",
                    "rating": "4.5",
                    "link": brand_url,
                    "platform": keyword.title() + " Store"
                })
                break
            except:
                continue
    driver.quit()
    return products


def get_all_products(query):
    amazon = get_amazon_products(query)
    flipkart = get_flipkart_products(query)
    brand_store = get_brand_store_product(query)

    all_products = amazon + flipkart + brand_store
    return sorted(all_products, key=lambda x: (parse_price(x['price']) if x['price'] != '-' else float('inf'), -float(x['rating'])))
