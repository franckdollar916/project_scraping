from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        dbname="books_db",
        user="postgres",
        password="franckdollar91",
        host="localhost",
        port="5432",
        client_encoding="UTF8"  # 🔥 Force l'encodage UTF-8
    )

@app.route('/')
def home():
    return jsonify({"message": "Bienvenue sur l'API Books !", "endpoints": ["/books"]})

@app.route('/books', methods=['GET'])
def get_books():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT title, price, availability FROM books;")
    books = cur.fetchall()
    cur.close()
    conn.close()

    # ✅ Correction des problèmes d'encodage avec UTF-8
    clean_books = []
    for title, price, availability in books:
        try:
            title = title.encode("latin1").decode("utf-8") if isinstance(title, str) else title
            price = price.encode("latin1").decode("utf-8") if isinstance(price, str) else price
            availability = availability.encode("latin1").decode("utf-8") if isinstance(availability, str) else availability
        except UnicodeDecodeError:
            title, price, availability = title, price, availability  # Évite l'erreur si déjà bien encodé
            
        clean_books.append({"Titre": title, "Prix": price, "Disponibilité": availability})

    return jsonify(clean_books)


if __name__ == '__main__':
    print("\n✅ API démarrée ! Accède à l'URL suivante :")
    print("📌 http://127.0.0.1:5000/")
    print("📌 http://127.0.0.1:5000/books\n")
    
    app.run(debug=True)
