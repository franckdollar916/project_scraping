FROM python:3.9

WORKDIR /app

# ✅ Copier uniquement Scraper/ pour éviter les problèmes de chemin
COPY Scraper /app/

# ✅ Vérifier si requirements.txt existe
RUN ls /app

# ✅ Installer les dépendances
RUN pip install --no-cache-dir -r /app/requirements.txt

# ✅ Exécuter le scraper
CMD ["python", "/app/scraper.py"]
