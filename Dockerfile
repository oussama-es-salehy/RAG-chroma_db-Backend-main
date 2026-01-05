# Image Python légère
FROM python:3.10-slim

# Empêche Python d’écrire des .pyc
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Dossier de travail
WORKDIR /app

# Copier les dépendances
COPY requirements.txt .

# Installer les dépendances sans cache (important pour la taille)
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet
COPY . .

# Port (Flask = 5000, FastAPI = 8000)
EXPOSE 5000

# Commande de lancement (Flask)
CMD ["python", "server.py"]
