# Aufgabe: Hashing, Kollisionen, Rainbow-Tabellen, Salting & Peppering

## Begriff „Kollision“ im Kontext des Hashings
Eine Kollision tritt beim Hashing auf, wenn zwei unterschiedliche Eingabewerte denselben Hash-Wert erzeugen. Da Hashfunktionen eine große Eingabemenge auf eine kleinere Ausgabemenge abbilden, sind Kollisionen unvermeidbar. Sie stellen ein Sicherheitsrisiko dar, da ein Angreifer gezielt eine andere Eingabe finden kann, die denselben Hash-Wert wie ein Passwort besitzt.

## Rainbow-Tabellen
Rainbow-Tabellen sind vorgefertigte Tabellen, die für viele mögliche Passwörter deren Hash-Werte enthalten. Sie dienen dazu, Hash-Werte schnell auf das ursprüngliche Passwort zurückzuführen. Angreifer nutzen Rainbow-Tabellen, um Hashes effizient zu knacken, indem sie einfach nach dem Hash in der Tabelle suchen.

## Angriffe mit Kollisionen und Rainbow-Tabellen
- **Kollisionen:** Ein Angreifer kann eine alternative Eingabe finden, die denselben Hash wie ein legitimes Passwort erzeugt und sich damit Zugang verschaffen.
- **Rainbow-Tabellen:** Ein Angreifer kann mit Hilfe einer Rainbow-Tabelle schnell herausfinden, welches Passwort zu einem Hash gehört, sofern kein Salt verwendet wurde.

## Schutz durch Salting und Peppering
- **Salting:** Ein Salt ist ein zufälliger Wert, der zu jedem Passwort hinzugefügt wird, bevor es gehasht wird. Dadurch wird verhindert, dass identische Passwörter denselben Hash erzeugen und Rainbow-Tabellen nutzlos werden.
- **Peppering:** Ein Pepper ist ein geheimer Wert, der zusätzlich zum Salt verwendet wird und nicht in der Datenbank gespeichert wird. Er erhöht die Sicherheit weiter, da ein Angreifer den Pepper kennen muss, um Hashes zu berechnen.

## Beispiel: Hashing mit Salt und Pepper (Python)

```python
import hashlib
import os

# Passwort, Salt und Pepper
def hash_password(password, salt=None, pepper=None):
    if salt is None:
        salt = os.urandom(16)  # 16 Bytes zufälliges Salt
    if pepper is None:
        pepper = b'supersecretpepper'  # Beispiel-Pepper (sollte sicher gespeichert werden)
    # Kombiniere Passwort, Salt und Pepper
    pwd_bytes = password.encode('utf-8')
    hash_input = salt + pwd_bytes + pepper
    hash_value = hashlib.sha256(hash_input).hexdigest()
    return hash_value, salt

# Beispiel
password = 'meinPasswort123'
hash_value, salt = hash_password(password)
print(f"Hash: {hash_value}\nSalt: {salt.hex()}")
```

**Hinweis:**
- Das Salt wird für jeden Benutzer individuell und zufällig generiert und mit dem Hash gespeichert.
- Der Pepper sollte geheim gehalten und nicht in der Datenbank abgelegt werden.
