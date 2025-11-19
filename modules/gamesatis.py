from bs4 import BeautifulSoup
import requests
from fake_useragent import UserAgent

def gameSatis_scrape():
    ua = UserAgent()

    headers = {
        "User-Agent": ua.random
    }
    url = 'https://www.gamesatis.com/mobile-legends-elmas-tr'
    
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
        product_names = [name.get_text(strip=True) for name in soup.select('section div a h3')]

        product_prices = [price.get_text(strip=True) for price in soup.find_all('div', class_='selling-price')]
        product = dict(zip(product_names, product_prices))

        return product

    except Exception as e:
        print(f"Scraping veya sözlük oluşturma sırasında hata oluştu: {e}")
        return {} 


products_dict = gameSatis_scrape()

# if products_dict:
#     for name, price in products_dict.items():
#         print(f" {name} {price}")
# else:
#     print("Ürün bilgisi çekilemedi veya bir hata oluştu.")