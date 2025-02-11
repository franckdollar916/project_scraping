# 📌 Projet de Scraping et Visualisation des Données

## 🚀 Introduction
Ce projet consiste à scraper des données depuis un site web, les stocker dans une base de données PostgreSQL, les exposer via une API FastAPI et les afficher dans une interface web avec Dash. L’ensemble du projet est conteneurisé avec Docker et orchestré via `docker-compose`.

---

## 🛠️ Technologies Utilisées
✅ **Scraping** : `BeautifulSoup`, `Requests`  
✅ **Base de données** : `PostgreSQL`  
✅ **API** : `FastAPI`  
✅ **Interface Web** : `Dash (Plotly)`  
✅ **Conteneurisation** : `Docker` & `Docker-Compose`

---

## 📁 Structure du Projet
```
projet_scraping_IMDB/
│── Scraper/          # Scraping des données
│── Database/         # Base de données PostgreSQL
│── API/              # API FastAPI pour l'accès aux données
│── WebApp/           # Interface Web avec Dash
│── docker-compose.yml # Orchestration Docker
│── README.md         # Ce fichier 📄
```

---

## ⚙️ Installation & Lancement
### 🔹 **1. Prérequis**
- Docker & Docker-Compose installés

### 🔹 **2. Cloner le projet**
```bash
git clone https://github.com/franckdollar916/projet_scraping.git
cd projet_scraping_IMDB
```

### 🔹 **3. Construire et démarrer les services**
```bash
docker-compose up --build
```
📌 **Attendre quelques secondes** le temps que la base de données PostgreSQL démarre.

### 🔹 **4. Tester les services**
📡 **API** (Swagger Docs) : [http://localhost:8000/docs](http://localhost:8000/docs)  
📊 **Interface Web** : [http://localhost:8050](http://localhost:8050)  

---

## 🛠️ Fonctionnalités
✔ **Scraping des données** depuis un site web.  
✔ **Stockage des données** dans PostgreSQL.  
✔ **Accès via une API** FastAPI en JSON.  
✔ **Affichage dynamique** des données dans une interface web.  
✔ **Déploiement facilité** avec Docker.

---

## 🔥 Problèmes rencontrés et solutions
### ❌ `ModuleNotFoundError: No module named 'Database'`
📌 **Solution** : Modification du `Dockerfile` du Scraper pour copier correctement les fichiers :
```dockerfile
COPY Scraper /app/
```

### ❌ `connection to server at "database" failed: Connection refused`
📌 **Solution** : Ajout d’un **délai d’attente** dans `docker-compose.yml` avant d’exécuter l’API :
```yaml
entrypoint: ["/bin/sh", "-c", "sleep 10 && python /app/database.py"]
```

### ❌ `No such file or directory: '/app/Scraper/requirements.txt'`
📌 **Solution** : Vérification du chemin dans le `Dockerfile` et correction avec :
```dockerfile
COPY . /app/
```

### ❌ `database "books_db" already exists`
📌 **Solution** : Suppression de la ligne `CREATE DATABASE books_db;` dans `schema.sql`.

---

## 🎯 Améliorations futures
🚀 **Scraping en temps réel avec Celery**  
🚀 **Ajout d’Elasticsearch pour une recherche avancée**  
🚀 **Utilisation de Redis pour la mise en cache**  


