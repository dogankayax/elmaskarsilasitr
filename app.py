from flask import Flask, render_template, request, redirect, url_for
import sys
import os
import re

def clean_price(price_str):
    """Fiyat stringini temizler ve float değere dönüştürür."""
    if isinstance(price_str, (int, float)):
        return float(price_str)
    
    cleaned_str = re.sub(r'[^\d.,]', '', price_str)
    
    if ',' in cleaned_str and cleaned_str.count('.') <= 1:
        cleaned_str = cleaned_str.replace(',', '.')
    
    try:
        return float(cleaned_str)
    except ValueError:
        return 0.0 

sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

# İçe aktarmalar ve hata yakalama
try: from atagame import atagame_scrape
except ImportError: atagame_scrape = lambda: {}
try: from dijipin import dijipin_scrape
except ImportError: dijipin_scrape = lambda: {}
try: from gamesatis import gameSatis_scrape
except ImportError: gameSatis_scrape = lambda: {}
try: from onsrashop import onsraShop_scrape
except ImportError: onsraShop_scrape = lambda: {}
try: from vatangame import vatangame_scrape
except ImportError: vatangame_scrape = lambda: {}

SCRAPERS = {
    "Atagame": atagame_scrape,
    "Dijipin": dijipin_scrape,
    "GameSatis": gameSatis_scrape,
    "OnsraShop": onsraShop_scrape,
    "VatanGame": vatangame_scrape
}

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/index')

def index_page():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search():
    budget_str = request.args.get('budget')
    
    if not budget_str:
        return render_template('search.html', results=None, budget=None)

    try:
        budget = float(budget_str)
    except ValueError:
        error_message = "Lütfen geçerli bir sayısal bütçe giriniz."
        return render_template('search.html', results=None, budget=None, error=error_message)

    all_products = []
    
    for site_name, scraper_func in SCRAPERS.items():
        try:
            scraped_dict = scraper_func()
            
            for name, price_str in scraped_dict.items():
                price = clean_price(price_str)
                
                if price > 0 and price <= budget:
                    all_products.append({
                        "site_name": site_name,
                        "name": name,
                        "price": price
                    })
        except Exception as e:
            print(f"Hata: {site_name} verileri çekilemedi: {e}")
            
    filtered_products = all_products
    
    grouped_results = {}
    for product in filtered_products:
        site = product['site_name']
        if site not in grouped_results:
            grouped_results[site] = []
        grouped_results[site].append(product)
        
    for site in grouped_results:
        grouped_results[site].sort(key=lambda x: x['price'])
        
    # 7. Sonuçları göster
    return render_template(
        'search.html', 
        results=grouped_results, 
        budget=budget,
        error=None
    )


if __name__ == "__main__":
    app.run(debug=True)