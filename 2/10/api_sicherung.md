# API-Sicherung (vereinfacht)

## Wichtige Punkte
- Authentifizierung: Wer bist du?
- Autorisierung: Was darfst du?
- Eingabe prüfen: Stimmen Felder, Typen und Länge?

## Authentifizierung
- JWT: Server gibt signiertes Token, Client sendet es bei Anfragen. Vorteil: stateless.
- API-Keys: Einfach, gut für Maschinen, weniger flexibel.
- OAuth2: Für Drittzugriffe (z. B. Social Login).

## Autorisierung
- RBAC: Benutzer bekommen Rollen mit Rechten (z. B. Admin, User).
- Feingranulare Prüfungen: Prüfen, ob der Benutzer auf genau diese Ressource zugreifen darf.

## Beispiele (kompakt)
- Kommentar ändern: Server speichert Autor beim Erstellen. Bei Änderungsanfrage prüft Server, ob der Anfragende der Autor ist — sonst 403.
- Fremder Name beim Posten: Client sendet nur Inhalt. Server weist author_id aus dem Token zu, nicht aus der Anfrage.

## Eingabe prüfen
- Whitelist: Nur erwartete Felder akzeptieren.
- Schema: Typen, Längen und Formate prüfen (E-Mail, URL).
- Sanitization: HTML entfernen/escapen, um XSS zu verhindern.
- Rate Limiting: Anfragen pro Zeit begrenzen.

## Best Practices
- HTTPS nutzen.
- Tokens kurzlebig machen.
- CORS auf vertrauenswürdige Domains beschränken.
- Zugriffsfehler protokollieren.
- Keine technischen Fehlermeldungen an Nutzer.

## Goldene Regeln
1. Server entscheidet immer.
2. Benutzer-ID aus dem verifizierten Token verwenden.
3. Bei Änderungen Ownership prüfen.
4. Im Zweifel Zugriff verweigern.