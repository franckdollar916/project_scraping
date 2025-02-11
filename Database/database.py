import psycopg2

def connect_db():
    """ Connexion à la base PostgreSQL """
    try:
        conn = psycopg2.connect(
            dbname="books_db",
            user="postgres",
            password="franckdollar91",  
            host="localhost",
            port="5432"
        )
        return conn
    except Exception as e:
        print("❌ Erreur de connexion :", e)
        return None

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
        cur.executemany(insert_query, books)
        conn.commit()
        cur.close()
        conn.close()
        print(f"✅ {len(books)} livres insérés dans la base de données !")
    except Exception as e:
        print("❌ Erreur d'insertion :", e)
