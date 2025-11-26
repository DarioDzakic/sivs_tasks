# Cross-Site Scripting (XSS) – Theorie

## Was ist XSS?

Cross-Site Scripting (XSS) ist eine Sicherheitslücke, bei der Angreifer schädlichen JavaScript-Code in eine Website einbinden. Der Code wird im Browser des Opfers ausgeführt und kann Daten stehlen oder Benutzer manipulieren.

## Angriffsvektoren

- **Injektionspunkte**: Unzureichend validierte Eingabefelder (Kommentare, Formulare, Suchfelder, URLs)
- **Speicherung**: Code kann in Datenbanken gespeichert und später ausgeführt werden
- **Folgen**: Session-Übernahme, Passwort-Diebstahl, Phishing, Malware-Verbreitung

## Schutzmaßnahmen

### 1. Escaping von Benutzereingaben
Konvertieren Sie HTML-Sonderzeichen in sichere Entities. Ausgabe-Funktionen sollten automatisch escapen, statt rohe HTML-Ausgabe zu ermöglichen.

### 2. Content Security Policy (CSP)
HTTP-Header definiert, welche Ressourcen (Skripte, Bilder, Styles) geladen werden dürfen. Blockiert unsichere Inline-Skripte.

### 3. Sichere JavaScript-Praktiken
Vermeiden Sie unsichere DOM-Manipulationsmethoden mit Benutzereingaben. Nutzen Sie sichere Alternativen. Externe Skripte nur von vertrauenswürdigen Quellen laden.

### 4. Eingabevalidierung
Validierungen auf Whitelist-Basis durchführen. Nur erlaubte Zeichen und Längen akzeptieren.

### 5. Sicherheits-Header
Implementieren Sie HTTP-Header wie X-Content-Type-Options, X-Frame-Options und Strict-Transport-Security.
