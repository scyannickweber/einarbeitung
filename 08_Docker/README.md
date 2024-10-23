# Projektname: Webanwendung mit Docker Container

## Beschreibung
In diesem Projekt soll eine Webanwendung in einem Docker-Container gestartet werden. Dabei sollen die Webanwendung und die Datenbank in unterschiedlichen Containern laufen.

## Inhaltsverzeichnis
1. [Einrichten der Docker Container](#einrichten-der-docker-container)
2. [Starten der Webanwendung](#starten-der-webanwendung)
3. [Fragen und Antworten](#fragen-und-antworten)

## Einrichten der Docker Container
- Erstelle Docker-Container für die Webanwendung und die Datenbank.
- Definiere die Dockerfile(s) und docker-compose-Datei(en) für die Container.

## Starten der Webanwendung
- Starte die Webanwendung in einem Docker-Container.
- Stelle sicher, dass die Webanwendung korrekt funktioniert und auf die Datenbank zugreifen kann.

## Fragen und Antworten
- Was sind die Unterschiede zwischen einer Virtual Machine (VM) und Docker? Erläutere die Konzepte und ihre Vor- und Nachteile.
    - VMs virtualisieren ganze Betriebssysteme, bieten starke Isolation, sind aber ressourcenintensiv und langsamer. Docker-Container sind leichtgewichtiger, starten schneller, teilen den   Kernel des Hosts, bieten jedoch weniger Isolation.- Was ist Docker und was ist docker-compose? Beschreibe die Funktionen und Verwendungszwecke von Docker und docker-compose.
- Was sind die Vorteile von Docker? Diskutiere die Vorteile von Docker im Vergleich zu traditionellen Bereitstellungsmethoden.
    - Docker ist leichtgewichtig, startet schnell, und bietet hohe Portabilität über verschiedene Umgebungen hinweg. Es sorgt für konsistente Deployments, eliminiert Umgebungsprobleme und ermöglicht einfache Updates und Rollbacks, was es agiler und effizienter als traditionelle Bereitstellungsmethoden macht.
- Was ist ein Docker-Image? Beschreibe die Bedeutung und Funktionsweise von Docker-Images.
    - Ein Docker-Image ist eine unveränderliche Vorlage, die alle notwendigen Komponenten enthält, um eine Anwendung auszuführen. Es bildet die Grundlage für Container und ermöglicht konsistente, wiederholbare Deployments in verschiedenen Umgebungen.
- Was ist Containerisierung? Erläutere den Begriff und seine Vorteile für die Softwareentwicklung und -bereitstellung.
    - Containerisierung verpackt Anwendungen und ihre Abhängigkeiten in isolierte, leichtgewichtige Container, die portabel und ressourcenschonend sind. Sie bieten Konsistenz, schnellere Bereitstellung und vereinfachte Skalierbarkeit in der Softwareentwicklung.
- Was kann man alles in einem Docker-Container starten? Nenne Beispiele für Anwendungen und Services, die in Docker-Containern ausgeführt werden können.
    - In Docker-Containern können Webserver (NGINX), Datenbanken (MySQL), Programmiersprachenumgebungen (Python), Microservices, CI/CD Tools (Jenkins), Caching-Dienste (Redis) und Messaging-Queues (RabbitMQ) ausgeführt werden
- Was ist Docker-Hub und was ist eine Docker-Registry? Unterscheide zwischen den beiden und beschreibe ihre Rolle in der Docker-Ökosystem.
    - Docker Hub ist eine öffentliche Registry für das Speichern und Teilen von Docker-Images. Eine Docker-Registry kann sowohl öffentlich als auch privat sein und dient allgemein zum Verwalten von Images. Docker Hub ist ein Beispiel einer Registry, während eine Docker-Registry jeder Speicherort für Images sein kann.
- Können Daten verloren gehen, wenn ein Docker-Container beendet wird? Diskutiere mögliche Szenarien für Datenverlust und wie man sie vermeiden kann.
    - Ja, Daten können verloren gehen, wenn ein Docker-Container beendet wird, da Container temporär sind. Um Datenverlust zu vermeiden, können Volumes oder Bind Mounts genutzt werden, die Daten außerhalb des Containers speichern und über Neustarts hinweg erhalten bleiben. 
- Wie kann man den Datenverlust eines Containers verhindern? Beschreibe Strategien für die Datenpersistenz in Docker-Containern.
    - Datenverlust in Containern lässt sich durch Docker Volumes verhinder, die Daten extern speichern Bind Mounts, die Host-Verzeichnisse nutzen, oder durch externe Datenbanken, die unabhänging vom Container laufen
- Was bedeutet Mounten? Erläutere den Begriff und seine Bedeutung in Bezug auf Docker-Container.
    - Mounten bedeutet, Host-Verzeichnisse oder Datein in einem Docker-Container einzubinden, um den zugriff auf Daten zu ermöglichen. Bind Mounts verknüpfen direkt mit Host-Verzeichnissen, während Volumes von Docker verwltete Speicherorte sind, die Daten unabhängig vom Container speichern 
- Was ist ein Docker Image und was ist ein Dockerfile? Erkläre die Unterschiede zwischen den beiden und ihre Verwendungszwecke.
    - Ein Docker-Image ist eine ausführbere Vorlage, die alle Komponenten einer Anwenung enthält und zur Erstellung von Containern dient. Ein Dockerfile ist eine Textdatei mit Anweisungen, wie ein Image gebaut wird. Das Docekrfile erstellt das Image, und das Image wird genutzt, um Container zu starten
- Was ist ein Docker-Network? Beschreibe die Netzwerkfunktionalitäten von Docker und wie Container miteinander kommunizieren können.
    - Ein Docker-Network ermöglicht Containern, miteinander zu kommunizieren. Es gibt verschiedene Modi, wie Bridge (Kommunikation auf demselben Host), Host (Container nutzt das Host-Netzwerk) und Overlay (für verteilte Container auf mehreren Hosts). Container im selben Netzwerk können sich über ihre Namen ansprechen.
- Was legen Docker-ENTRYPOINT und -WORKDIR fest? Erläutere die Bedeutung dieser Anweisungen in einem Dockerfile.
    - ENTRYPOINT legt das Hauptkommando fest, das beim Start eines Containers ausgeführt wird. WORKDIR bestimmt das Arbeitsverzeichnis innerhalb des Containers, in dem Befehle ausgeführt oder Dateien abgelegt werden. Beide Anweisungen helfen, das Verhalten und den Kontext des Containers zu steuern.
- Was sagen folgende Fehlermeldungen aus und wie könnte man diese beheben? Diskutiere gängige Fehlermeldungen beim Arbeiten mit Docker-Containern und mögliche Lösungsansätze.
    - "No such file or directory" bedeutet, dass ein Pfad fehlt, Lösung: Pfade prüfen. "Port already in use" weist auf einen belegten Port hin, Lösung: Port ändern oder Prozess beenden. "Image not found" tritt bei einem fehlenden image auf, Lösung: Image abrufen. "Cannot connect to the Docker daemon" deutet auf einen nicht laufenden Daemon oder Berechtigungsprobleme hin, Lösung: Daemon starten oder auch die Rechte prüfen.
