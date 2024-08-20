## Aufgabenbeschreibung
Die Daten sollen in einer Datenbank gespeichert werden.

1. **DB aufsetzen**: Die Datenbank wird eingerichtet, um Daten zu speichern.
2. **Struktur der Datenbank mittels semantisches ER-Diagramm**: Das semantische ER-Diagramm wird erstellt, um die Struktur der Datenbank zu visualisieren.
3. **Datenbank aufsetzen und Daten einfügen**: Die Datenbank wird erstellt und Daten werden eingefügt.
4. **Daten mittels SQL-Querys bearbeiten (nicht über xampp-oberfläche)**:
   a) **Hinzufügen**: Neue Daten werden der Datenbank hinzugefügt.
   b) **Löschen**: Daten werden aus der Datenbank gelöscht.
   c) **Bearbeiten**: Bestehende Daten werden in der Datenbank bearbeitet.
   d) **Auslesen**: Daten werden aus der Datenbank abgerufen.

### Fragen:

- Welche Datenbanken gibt es? SQL, SQLite
   - MySQL, Microsoft SQL Server, Oracle Database 
- Wann macht welcher Typ Sinn? SQL bei gleichbleibenden Attributen.
   - SQLite macht sinn, bei eher kleineren Datenbankanwendungen und wenn diese lokal ausgeführt wird. MySQL ist Sinnvoll, wenn große Datenbanken geht z.B. Webanwendungen mit mehreren gleichzeitigen Nutzern und wenn die Sicherheit und Verfügbarkeit wichtig ist.
- Was ist ein Primary Key und was ein Foreign Key?
   - Ein Primary Key ist ein eindeutiger Bezeichner für eine Zeile in einer Tabelle und ein ein Foreign Key ist ein Attribut in einer Tabelle, das auf den Primary Key einer anderen Tabelle verweist.
- Was ist ein nativer und was ein künstlicher Primary Key?.
   - ein nativer Key ist von einem schon bestehendem Attribut und ein künstlicher meist eine Automatische erstellte ID 
- Welche Beziehungstypen zwischen Tabellen gibt es?
   - 1:1, 1:n, n:m. 
- Welche Wildcards gibt es in MySQL und was bedeuten sie?
   - (%), (_). % vertritt keinen oder mehrere Zeichen, _ ein einziges Zeichen. 
- Was ist ein Join?
   - eine SQL-Klausel um Daten aus mehreren Tabellen abzufragen.
- Was ist ein left- und was ein right-Join?
   - ein Left join bezieht sich auf die erste(linke) Tabelle, beim right join werden die daten aus der rechten Tabelle selektiert, auch wenn keine zu den Daten der linken Tabelle besteht. 
- Was ist das kartesische Produkt zweier Tabellen?
   - das kartesische Produkt, ist eine Verknüpfung von allen Zeilen einer Tabelle mit allen Zeilen einer anderen Tabelle.
- Was ist Kaskadierung?
   - es überträgt automatisch die Daten einer Übergeordneten Tabelle auch die zugehörigen Daten einer Untergeordneten Tabelle. 
- Wann werden Gruppierungen benötigt?
   - Gruppierungen werden benötigt, wenn aggregiertw Daten berechnet werden müssen.
- Was ist ein DBMS?
   - eine Software, welche zusammen mit der Datenbasis, die gesamtheit der zu verwaltenden Daten, die Datenbank ergibt.
- Was versteht man unter Datenintegrität?
   - die Korrektheit, Vollständigkeit und Konsistenz von Daten .
- Was ist Normalisierung?
   - beschreibt den Prozess der Strukturierung und Umorganisation eines relationalen Datenbankschemas. Um Datenredundanz zu beseitigen und Datenintegrietät zu Verbessern. 
- Was sind Aggregationsfunktionen und welche gibt es? (3 Beispiele)
   - SUM, MAX/MIN und COUNT. Sie werden genutzt um verschiedene Statistiken zu Daten ermitteln.