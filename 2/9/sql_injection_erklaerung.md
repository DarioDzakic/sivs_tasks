# SQL Injections – Theorie

## Was ist eine SQL-Injection?

Eine SQL-Injection ist eine Sicherheitslücke, bei der Angreifer Befehle direkt in SQL-Abfragen einfügen. Dies ermöglicht unerlaubten Datenzugriff, Manipulation oder Löschung von DatenbankInhalten.

## Angriffsvektoren

- **Login-Umgehung**: Manipulation von WHERE-Bedingungen zur Authentifizierungsumgehung
- **Datenbankabfrage**: Datendiebstahl durch UNION-Anweisungen
- **Datenlöschung**: Ausführung destruktiver Befehle wie DROP TABLE
- **Injektionspunkte**: Unkontrollierte Eingabefelder (Login, Suchfelder, Filter)

## Schutzmaßnahmen

### 1. Prepared Statements
Sicherste Methode: Code und Daten werden getrennt behandelt. Der Eingabewert wird als reiner Datenwert erkannt, nicht als SQL-Code.

### 2. Eingabevalidierung
Whitelist-basierte Validierung durchführen. Nur erlaubte Muster, Datentypen und Längenbeschränkungen akzeptieren.

### 3. Datenbankberechtigungen beschränken
Anwenden des Principle of Least Privilege: Datenbankbenutzer erhalten nur notwendige Permissions (z.B. SELECT und INSERT, kein DROP oder ALTER).

### 4. Escaping von Sonderzeichen
Falls Prepared Statements nicht möglich: Spezielle Zeichen mit datenbankspezifischen Escaping-Funktionen neutralisieren.

### 5. Fehlerbehandlung
Generische Fehlermeldungen an Benutzer zeigen. Detaillierte SQL-Fehler nur intern loggen, um Information Disclosure zu verhindern.

### 6. Web Application Firewall (WAF)
Überwachen und Filtern verdächtiger SQL-Patterns als zusätzliche Schutzschicht.
