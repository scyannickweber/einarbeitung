# Projektname: Erstellung einer API zur Datenabfrage

## Beschreibung
In diesem Projekt wird eine API erstellt, über die Daten abgefragt werden können. Es sollen zwei Endpunkte implementiert werden: Einer, der alle Datensätze zurückgibt, und ein anderer, der einen bestimmten Datensatz anhand einer speziellen ID liefert.

## Inhaltsverzeichnis
1. [Einrichten der API](#einrichten-der-api)
2. [Implementierung der Datenabfrage](#implementierung-der-datenabfrage)
3. [Fragen und Antworten](#fragen-und-antworten)

## Einrichten der API
- Richte eine API ein, die auf einem Webframework wie Flask oder Django basiert.
- Konfiguriere die Routen und Endpunkte für die Datenabfrage.

## Implementierung der Datenabfrage
- Implementiere zwei Endpunkte: Einen für die Abfrage aller Datensätze und einen für die Abfrage eines bestimmten Datensatzes anhand einer ID.
- Stelle sicher, dass die Daten korrekt formatiert und über die API zurückgegeben werden.

## Fragen und Antworten
- Was ist eine API? Erläutere den Begriff und ihre Bedeutung in der Softwareentwicklung.
    - Eine API ist eine Schnittstelle, die es unabhängigen Programmen ermöglicht, miteinander zu kommunizieren und Daten auszutauschen ohne viel am Code ändern zu müssen.
- Woraus besteht eine API? Beschreibe die Komponenten und Funktionen einer API.
    - Eine API besteht aus Endpunkten, die bestimmte URL-Adressen definieren, Anfragen wie GET oder POST annehmen und strukturierte Antworten (z.B. JSON) zurückgeben. Sie verwendet Authentifizierung zur Absicherung und bietet Dokumentation, um das Arbeiten mit einer API zu erleichtern. APIs machen den Austausch von Daten und Funktionen zwischen verschiedenen Systemen möglich.
- Wann wird eine API verwendet? Erkläre die Einsatzgebiete und Situationen, in denen APIs eingesetzt werden.
    - APIs werden verwendet, um Anwendungen oder Systeme miteinander zu verbinden und den Datenaustausch zu ermöglichen, z. B. bei Web-Apps, mobilen Apps, IoT-Geräten oder der Integration externer Dienste wie Zahlungs- oder Kartendienste.
- Warum sind APIs wichtig? Diskutiere die Bedeutung von APIs für die Interoperabilität und Integration von Systemen.
    - Sie sind wichtig, weil sie die Interoperabilität zwischen Systemen ermöglichen und so eine nahtlose Integration von Diensten und Daten erleichtern. Sie machen die Entwicklung flexibler, fördern die Wiederverwendbarkeit von Funktionen und verbessern die Skalierbarkeit.
- Was ist ein API-Token und was ein API-Key? Unterscheide zwischen den beiden und erkläre ihre Verwendungszwecke.
    - API-Key: statischer Schlüssel zur Authentifizierung eines Clients bei einer API. API-Token: ein dynammischer, zeitlich begrenzter Schlüssel, welcher für sicherere Authentifizierung und Autorisierung genutzt wird.
- Warum nicht die Daten direkt auf der DB abfragen? Diskutiere die Vorteile der Verwendung einer API zur Datenabfrage im Vergleich zur direkten Abfrage der Datenbank.
    - APIs bieten mehr Sicherheit, abstrahieren die interne Datenstruktur und ermöglichen bessere Zugriffskontrolle sowie effizientere Skalierbarkeit im Vergleich zur direkten Datenbankabfrage.
- Nenne verschiedene Bereiche, in denen APIs verwendet werden. Beschreibe die Anwendungsbereiche und Beispiele für die Verwendung von APIs.
    - Sie werden in vielen Bereichen eingesetzt, wie in Web- und Mobile-Apps für den Abruf von Echtzeitdaten, in Social Media zur Integration von Plattformen, im E-Commerce für Zahlungsdienste und in IoT-Geräten für die Kommunikation. Sie ermöglichen nahtlosen Datenaustausch und einfache Systemintegration.
- Was ist REST? Erläutere den Begriff und die Prinzipien von RESTful APIs.
    - REST ist ein Architekturstil für Web-APIs, der auf die standard HTTP-Methoden (wie GET, POST, PUT, DELETE) basiert und es ermöglicht, Ressourcen stateless und cachebar über URLs anzusprechen.
- Was ist GraphQL und wie unterscheidet es sich von REST? Beschreibe die Unterschiede zwischen GraphQL und RESTful APIs.
    - GraphQL ist eine Abfragesprache, ein Architekturstil und eine Reihe von Tools zum Erstellen und Bearbeiten von APIs, Außerdem eignet es sich gut für große, komplexe und miteinander verbundene Datenquellen. REST Dagegen ist eher für einfache Datenquellen.
- Welche Sicherheitsaspekte sind bei der Entwicklung einer API zu beachten? Diskutiere mögliche Sicherheitsrisiken und Best Practices für die API-Sicherheit.
    - API-Sicherheit erfordert starke Authentifizierung, Verschlüsselung (TLS), Eingabevalidierung und Rate-Limiting, ergänzt durch Logging und regelmäßige Sicherheitsprüfungen.
