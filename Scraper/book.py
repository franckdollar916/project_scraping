import requests
from bs4 import BeautifulSoup

# URL à scraper
url = "http://books.toscrape.com/catalogue/category/books_1/index.html"

# Faire la requête
response = requests.get(url)

# Vérifier si le site répond bien
if response.status_code == 200:
    # Parser le HTML
    soup = BeautifulSoup(response.text, "html.parser")

    # Trouver tous les livres
    books = soup.find_all("article", class_="product_pod")

    # Stocker les données
    book_list = []

    for book in books:
        title = book.h3.a["title"]  # Récupérer le titre
        price = book.find("p", class_="price_color").text.strip()  # Récupérer le prix
        availability = book.find("p", class_="instock availability").text.strip()  # Disponibilité
        
        book_list.append({
            "Titre": title,
            "Prix": price,
            "Disponibilité": availability
        })

    # Afficher les 5 premiers livres
    for b in book_list[:5]:
        print(b)
else:
    print("❌ Échec de la requête")
