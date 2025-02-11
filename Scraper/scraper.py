import sys
import os

# ✅ Correction de la parenthèse fermante
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from Database.database import insert_books  # ✅ Import corrigé
import requests
from bs4 import BeautifulSoup

# ✅ URL à scraper
URL = "http://books.toscrape.com/catalogue/page-1.html"

def scrape_books():
    """Scrape les livres à partir du site web."""
    try:
        response = requests.get(URL)
        response.raise_for_status()  # ✅ Vérifie les erreurs HTTP

        soup = BeautifulSoup(response.text, "html.parser")

        books = []
        for book_item in soup.select("article.product_pod"):
            title = book_item.select_one("h3 a")["title"].strip()
            price = book_item.select_one(".price_color").text.strip()
            stock = "In stock" if "In stock" in book_item.select_one(".instock.availability").text else "Out of stock"

            books.append({"title": title, "price": price, "stock": stock})

        return books

    except requests.RequestException as e:
        print(f"❌ Erreur lors du scraping : {e}")
        return []

if __name__ == "__main__":
    print("🚀 Scraping en cours...")
    books_data = scrape_books()

    if books_data:
        print(f"✅ {len(books_data)} livres trouvés. Insertion en base...")
        insert_books(books_data)
        print("📌 Données insérées avec succès !")
    else:
        print("❌ Aucun livre trouvé.")
