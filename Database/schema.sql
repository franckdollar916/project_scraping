-- Se connecter à la base (inutile si le script est exécuté dans le bon contexte)
\c books_db;

-- Création de la table books
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    price TEXT DEFAULT '',
    availability TEXT DEFAULT ''
);
