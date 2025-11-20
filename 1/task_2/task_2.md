# Hash-Funktionen & Datenintegrität – Kurznotizen

## Bedeutung von Hash-Funktionen
- Eine Hash-Funktion (z. B. SHA-256) erzeugt aus Daten einen **eindeutigen Fingerabdruck**.
- Schon eine Mini-Änderung an den Daten → komplett anderer Hash.
- Hashes sind **nicht umkehrbar** (man kann die ursprünglichen Daten nicht zurückrechnen).
- Einsatz in der Kryptographie:
  - Prüfen von **Datenintegrität**
  - Passwort-Hashing
  - Digitale Signaturen
  - Speicherung von Prüfsummen

## Wie tragen Hashes zur Integrität bei?
- Man berechnet den Hash einer Datei/Nachricht.
- Wenn die Datei später erneut gehasht wird:
  - **Gleicher Hash → unverändert**
  - **Anderer Hash → Datei wurde verändert**

