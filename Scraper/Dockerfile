# Utilisation de Python 3.9
FROM python:3.9

# Définition du répertoire de travail
WORKDIR /app

# Copier les fichiers nécessaires
COPY requirements.txt .  
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le Scraper/
COPY . .

# Commande de démarrage
CMD ["python", "scraper.py"]
