# Wähle ein Basis-Image aus, z. B. Python
FROM python:3.9-slim

# Setze den Arbeitsverzeichnis-Pfad im Container
WORKDIR /main.py

# Kopiere deine Anwendung in das Image
COPY . /main.py

# Installiere Abhängigkeiten (hier z.B. über eine requirements.txt)
RUN pip install -r requirements.txt

# Definiere den Startbefehl für den Container
CMD ["python", "main.py"]
