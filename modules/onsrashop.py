from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

def onsraShop_scrape():
    ua = UserAgent()

    headers = {
        "User-Agent": ua.random
    }
    url = 'https://www.onsrashop.com/mobile-legends-bang-bang-tr-c-278'
    
    try:
        response = requests.get(headers=headers, url=url, timeout=5) 
    except requests.exceptions.RequestException as e:
        print(f"İstek sırasında hata oluştu: {e}")
        return {}

    if not response.status_code == 200:
        print(f"Hata! HTTP Durum Kodu: {response.status_code} (200 OK bekleniyordu)")
        return {}

    try:
        soup = BeautifulSoup(response.content, "html.parser")
        
      
        product_names = [
            name.get_text(strip=True) 
            for name in soup.find_all('h3', class_='product-name d-block')
        ]
     
        product_prices = [
            price.get_text(strip=True) 
            for price in soup.find_all('div', class_='sales-price fw-600 fs-18')
        ]

        product_dict = dict(zip(product_names, product_prices))

        return product_dict

    except Exception as e:
        print(f"Scraping veya sözlük oluşturma sırasında hata oluştu: {e}")
        return {}

onsra_products = onsraShop_scrape()

# if onsra_products:
#     for name, price in onsra_products.items():
#         print(f"{name} {price}")
# else:
#     print("Ürün bilgisi çekilemedi veya bir hata oluştu.")