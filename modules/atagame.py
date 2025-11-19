from bs4 import BeautifulSoup
import requests
import time
from fake_useragent import UserAgent

def atagame_scrape():
    ua = UserAgent()
    headers = {
        "User-Agent": ua.chrome
    }
    url = "https://www.atagame.net/mobile-legends-bang-bang-turkiye-c-132"
    try:
        response = requests.get(url=url,headers=headers,timeout=2)
        if response.status_code == 200:
            urunler = {}
            soup = BeautifulSoup(response.content,'html.parser')
            product_name = soup.find_all("h3" , attrs={'class' , 'product-name d-block'})
            product_price = soup.find_all("div" , attrs={'class' , 'sales-price fw-600 fs-18'})
            for urun_adi, urun_fiyati in zip(product_name, product_price):
                urunler[urun_adi.text.strip()] = urun_fiyati.text.strip()
            print(urunler)    
        else:
            print("Hata")
            pass

    except ConnectionError:
        print("Bağlantı Hatası")
        return False
    except Exception as e:
        print(f"HATA \n {e}")           

    return urunler

