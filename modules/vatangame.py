from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def vatangame_scrape():
    options = Options()
    options.add_argument("--start-maximized")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=options)
    
    try:
        driver.get("https://vatangame.com/oyunlar/mobile-legends-bang-bang-elmas")
        
        wait = WebDriverWait(driver, 10)
        
        # Ürün adlarını çek
        urun_adlari = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "p.font-bold.form-label-black"))
        )
        
        genel_urunler = {}
        
        if len(urun_adlari) % 2 == 0:  
            for i in range(0, len(urun_adlari), 2):
                if i + 1 < len(urun_adlari):
                    genel_urunler[urun_adlari[i].text] = urun_adlari[i + 1].text
        else:
            urun_list = [elem.text for elem in urun_adlari]
            print("Ham veri:", urun_list)
            
            for i in range(0, len(urun_list), 2):
                if i + 1 < len(urun_list):
                    genel_urunler[urun_list[i]] = urun_list[i + 1]
        return genel_urunler
        
    except Exception as e:
        print(f"Hata oluştu: {e}")
        return {}
        
    finally:
        driver.quit()

urunler = vatangame_scrape()