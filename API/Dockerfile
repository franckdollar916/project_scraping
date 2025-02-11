FROM python:3.9
WORKDIR /app
COPY requirements.txt .  # ✅ Correction : Indique le bon chemin
RUN pip install --no-cache-dir -r requirements.txt
COPY . .  # ✅ Copie tous les fichiers de API/
CMD ["python", "api.py"]

