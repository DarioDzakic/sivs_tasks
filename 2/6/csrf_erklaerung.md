# Cross-Site Request Forgery (CSRF)

## Was ist CSRF?

Angreifer nutzt aktive Session des Benutzers aus, um unbeabsichtigte Aktionen durchzuführen. Benutzer ist auf legitimer Seite angemeldet, besucht Angreifer-Seite, die versteckt eine Anfrage an die legitime Seite sendet.

## Schutzmaßnahmen

**CSRF-Tokens**: Server generiert eindeutiges Token für jede Session. Formular enthält Token, Server validiert es.

**SameSite Cookies**: Browser sendet Cookies nicht automatisch über Site-Grenzen (Standard in modernen Browsern).

**Referer-Header Prüfung**: Server prüft, von welcher Domain die Anfrage kommt.

**POST statt GET**: State-changing Operationen nur mit POST durchführen.

## Moderne Situation

CSRF ist heute weniger kritisch, da Browser SameSite Cookies standardmäßig nutzen. Trotzdem sollten Anwendungen CSRF-Tokens verwenden und Origin-Validierung durchführen.
