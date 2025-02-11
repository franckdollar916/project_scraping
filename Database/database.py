import psycopg2

def connect_db():
    """ Connexion à la base PostgreSQL """
    try:
        conn = psycopg2.connect(
            dbname="books_db",
            user="postgres",
            password="franckdollar91",
            host="database",  # Utiliser "database" pour Docker
            port="5432"
        )
        return conn
    except Exception as e:
        print("❌ Erreur de connexion :", e)
        return None

def execute_schema():
    """ Exécute le fichier schema.sql pour créer la base de données et les tables """
    try:
        # Connexion à PostgreSQL sans spécifier de base (nécessaire pour créer la DB)
        conn = psycopg2.connect(
            dbname="postgres",
            user="postgres",
            password="franckdollar91",
            host="database",  # Nom du service Docker (remplacer par "localhost" si hors Docker)
            port="5432"
        )
        conn.autocommit = True
        cur = conn.cursor()

        # Lire et exécuter le fichier schema.sql
        with open("/app/schema.sql", "r") as file:  # Docker monte le fichier ici
            sql_script = file.read()
        cur.execute(sql_script)

        cur.close()
        conn.close()
        print("✅ Base de données et table créées avec succès !")

    except Exception as e:
        print("❌ Erreur lors de l'exécution du schéma SQL :", e)

def insert_books(books):
    """ Insère les livres scrappés dans PostgreSQL """
    conn = connect_db()
    if not conn:
        return
    
    try:
        cur = conn.cursor()
        insert_query = """
        INSERT INTO books (title, price, availability) VALUES (%s, %s, %s)
        """

        # Vérification : `books` doit être une liste de dictionnaires
        if isinstance(books, dict):
            books = [books]  

        if not isinstance(books, list):  
            print("❌ Format invalide : `books` doit être une liste de dictionnaires")
            return

        # 📌 Vérifier que chaque livre a bien les trois champs nécessaires (remplacer les champs manquants par "")
        values = []
        for book in books:
            title = book.get("title", "").strip()  # Mettre une chaîne vide si absent
            price = book.get("price", "").strip()
            availability = book.get("availability", "").strip()

            values.append((title, price, availability))

        cur.executemany(insert_query, values)  # Exécuter l'insertion
        conn.commit()

        print(f"✅ {len(books)} livres insérés dans la base de données !")
    
    except Exception as e:
        print("❌ Erreur d'insertion :", e)
        conn.rollback()
    
    finally:
        cur.close()
        conn.close()

def afficher_books():
    """ Affiche les 10 premiers livres de la base de données """
    conn = connect_db()
    if not conn:
        return
    
    try:
        cur = conn.cursor()
        cur.execute("SELECT * FROM books LIMIT 10;")
        rows = cur.fetchall()

        print("\n📚 Liste des 10 premiers livres :")
        for row in rows:
            print(row)

    except Exception as e:
        print("❌ Erreur d'affichage :", e)
    
    finally:
        cur.close()
        conn.close()

def afficher_structure_books():
    """ Affiche la structure de la table books """
    conn = connect_db()
    if not conn:
        return
    
    try:
        cur = conn.cursor()
        cur.execute("SELECT column_name, data_type FROM information_schema.columns WHERE table_name = 'books';")
        rows = cur.fetchall()

        print("\n📌 Structure de la table 'books' :")
        for row in rows:
            print(f"- {row[0]} ({row[1]})")

    except Exception as e:
        print("❌ Erreur d'affichage de la structure :", e)
    
    finally:
        cur.close()
        conn.close()

# Exécuter la création de la base et de la table automatiquement
if __name__ == "__main__":
    execute_schema()  # Exécute le fichier schema.sql
    afficher_structure_books()  # Vérifie la structure de la table
    afficher_books()  # Vérifie les données stockées
