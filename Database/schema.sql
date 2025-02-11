CREATE DATABASE books_db;

\c books_db;

CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title TEXT,
    price TEXT,
    availability TEXT
);
