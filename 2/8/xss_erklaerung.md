# Cross-Site Scripting (XSS) – Theorie

## Was ist XSS?

Cross-Site Scripting (XSS) ist eine Sicherheitslücke, bei der Angreifer schädlichen JavaScript-Code in eine Website einbinden. Der Code wird im Browser des Opfers ausgeführt und kann Daten stehlen oder Benutzer manipulieren.

## Angriffsvektoren

- Reflected XSS Attacks
- Stored XSS Attacks
- Blind Cross-site Scripting

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

1) Kontext‑sensitives Output‑Encoding (immer beim Output)
- Escapen je nach Einfüge‑Kontext:
  - HTML-Text: escape <, >, &.
  - HTML‑Attribute: zusätzlich Quotes (", ').
  - JavaScript‑Kontext: escape Quotes, Backslashes, neue Zeilen; besser: JSON.stringify(value) zur sicheren Einbettung in Skriptvariablen.
  - CSS / URL: jeweils passendes Encoding (CSS escape / encodeURIComponent).
- Praxis: benutze Template‑Engines mit Auto‑Escaping (z. B. Thymeleaf, Django, Handlebars) oder Server‑Side-Encoder.

2) Vermeide unsichere DOM‑APIs; nutze sichere Alternativen
- Nicht verwenden mit rohen Benutzerdaten: innerHTML, outerHTML, insertAdjacentHTML, document.write, eval(), new Function().
- Sicher: element.textContent = userInput; element.setAttribute(name, value); node.appendChild(document.createTextNode(...)).

3) HTML nur nach Whitelist‑Sanitization
- Wenn HTML erlaubt sein muss (z. B. Rich Text), sanitize auf Serverseite und Client mit bewährten Bibliotheken (z. B. DOMPurify).
- Verwende eine Whitelist für erlaubte Tags/Attribute und entferne Event-Handler (on*), Scripts, style-Urls.

   Beispiel DOMPurify (Client):
    var clean = DOMPurify.sanitize(dirtyHtml);
    container.innerHTML = clean;

4) Content‑Security‑Policy (CSP) konsequent einsetzen
- CSP limitiert Quellen und blockiert Inline‑Skripte/Styles ohne Nonce/Hashes.
- Vermeide 'unsafe-inline' und 'unsafe-eval'; nutze Nonces oder Script‑Hashes für erlaubte Inline‑Skripte.
- Testen zuerst mit Report‑Only, dann enforce.

   Beispiel-Header (vereinfacht):
    Content-Security-Policy: default-src 'self'; script-src 'self' 'nonce-ABC123'; object-src 'none'; base-uri 'self'

7) Defense‑in‑Depth & Testing
- Kombiniere Maßnahmen: Encoding + Sanitizer + CSP + sichere APIs.
- Automatisierte Scanner, statische Analyse und gezielte manuelle Tests / Pentests nutzen.
- Security‑Header ergänzen: X-Content-Type-Options, X-Frame-Options, Referrer-Policy.
