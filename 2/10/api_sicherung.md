# Sicherungsmethoden für APIs

## Grundprinzipien

APIs benötigen mehrschichtige Sicherung:
1. **Authentifizierung**: Identifizierung des Benutzers (Wer bist du?)
2. **Autorisierung**: Überprüfung von Berechtigungen (Was darfst du?)
3. **Input-Validierung**: Überprüfung der Anfragendaten (Ist die Anfrage gültig?)

---

## Authentifizierungsverfahren

### Token-basierte Authentifizierung (JWT)
- Server stellt nach erfolgreicher Anmeldung ein signiertes Token aus
- Client sendet Token mit jeder Anfrage
- Server validiert Token-Signatur und Ablaufzeit
- Vorteil: Stateless, skalierbar für verteilte Systeme

### API-Keys
- Eindeutige Keys für Client-Authentifizierung
- Einfacher, aber weniger flexibel als JWT
- Geeignet für Machine-to-Machine-Kommunikation

### OAuth 2.0
- Delegierte Authentifizierung für Drittanbieter-Zugriffe
- Oft verwendet für Social Logins (Google, GitHub)
- Trennung zwischen Authentifizierung und Autorisierung

---

## Autorisierungsverfahren

### Rollen-basierte Zugriffskontrolle (RBAC)
- Benutzer werden Rollen zugewiesen
- Jede Rolle hat definierte Berechtigungen
- Beispiel: Admin-Rolle (READ, CREATE, UPDATE, DELETE), User-Rolle (READ, CREATE)
- Einfach zu implementieren und zu verwalten

### Granulare Berechtigungsprüfungen
- Kombination aus Rollen und Ressourceneigenschaften
- Beispiel: Ein Moderator darf Kommentare anderer löschen, ein normaler User nicht

---

## Praktische Beispiele: Schutz von Kommentaren und Beiträgen

### Problem 1: Benutzer ändert Kommentare anderer
**Angreifer-Versuch**: Direkter API-Call zum Ändern eines Kommentars, den er nicht geschrieben hat

**Schutzmaßnahme**:
1. Beim Anlegen: Server speichert automatisch, wer den Kommentar verfasst hat (aus dem Token)
2. Bei Änderungsanfrage: Server prüft, ob Anfrage-Benutzer == Kommentar-Besitzer
3. Falls nicht: Server lehnt Anfrage ab (HTTP 403 Forbidden)

### Problem 2: Benutzer postet unter fremdem Namen
**Angreifer-Versuch**: Schickt API-Request mit manipuliertem author_id Feld

**Schutzmaßnahme**:
1. Client sendet nur den Kommentar-Inhalt
2. Server nimmt author_id NICHT von der Client-Anfrage
3. Server extrahiert Benutzer-ID aus dem validiertem Authentication-Token
4. Server nutzt diese ID zum Speichern, nicht die Client-Daten
5. Die author_id wird vom Server zugewiesen, nicht vom Client

---

## Input-Validierung

### Whitelist-Validierung
- Server akzeptiert nur explizit erlaubte Felder
- Unerwartete Felder werden ignoriert oder führen zu Fehler
- Verhindert, dass Angreifer neue Felder hinzufügen (z.B. admin-Flag)

### Schema-Validierung
- Überprüfung von Datentypen (String, Number, Boolean)
- Längenbeschränkungen durchsetzen
- Format-Validierung (E-Mail, URL, etc.)

### Eingabe-Sanitization
- HTML-Tags entfernen oder escapen
- Spezielle Zeichen neutralisieren
- Verhindert XSS und Injection-Angriffe

### Rate Limiting
- Maximale Anzahl von Anfragen pro Benutzer/IP pro Zeitfenster
- Verhindert Brute-Force-Angriffe und DoS-Attacken

---

## Sicherheits-Best-Practices

- **HTTPS verwenden**: Verschlüsselung aller Daten in Transit
- **Token-Ablaufzeiten**: Tokens sollten nach kurzer Zeit ablaufen
- **CORS konfigurieren**: Nur vertrauenswürdige Domains zulassen
- **Logging**: Alle Authentifizierungs- und Autorisierungsfehler protokollieren
- **Generische Fehlermeldungen**: Keine technischen Details offenlegen (z.B. „Zugriff verweigert" statt „Benutzer 42 existiert nicht")

---

## Goldene Regeln

1. **Server ist die Autorität**: Der Server trifft ALLE Sicherheitsentscheidungen, nie der Client
2. **Benutzer-ID aus Token**: Benutzer-Identifikation kommt aus dem verifizierten Token, nicht aus Anfragedaten
3. **Ownership-Validierung**: Bei jeder Änderung prüfen, ob der Benutzer die Ressource besitzt
4. **Fail Secure**: Im Zweifelsfall Zugriff verweigern, nicht gewähren
