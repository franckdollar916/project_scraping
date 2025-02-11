FROM python:3.9

WORKDIR /app

# Copier uniquement les fichiers nécessaires
COPY ./Scraper/requirements.txt /app/requirements.txt
COPY ./Scraper/scraper.py /app/scraper.py
COPY ./Database /app/Database  # Copier le dossier Database pour les imports

# Installer les dépendances
RUN pip install --no-cache-dir -r /app/requirements.txt

# Exécuter le scraper
CMD ["python", "/app/scraper.py"]