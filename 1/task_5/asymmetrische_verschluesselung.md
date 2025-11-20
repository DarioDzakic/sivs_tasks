# Asymmetrische Verschlüsselung: Beispiel mit RSA

## Gewählter Algorithmus: RSA (Rivest-Shamir-Adleman)
RSA ist ein weit verbreiteter asymmetrischer Verschlüsselungsalgorithmus. Er verwendet ein Schlüsselpaar: einen öffentlichen Schlüssel zum Verschlüsseln und einen privaten Schlüssel zum Entschlüsseln. Die Sicherheit basiert auf der Schwierigkeit, große Zahlen in ihre Primfaktoren zu zerlegen.

## Funktionsweise von RSA
- **Schlüsselerzeugung:** Es werden zwei große Primzahlen gewählt und daraus der öffentliche und private Schlüssel berechnet.
- **Verschlüsselung:** Die Nachricht wird mit dem öffentlichen Schlüssel verschlüsselt.
- **Entschlüsselung:** Nur der Besitzer des privaten Schlüssels kann die Nachricht entschlüsseln.

## Potenzielle Angriffsmethoden
- **Faktorisierungsangriff:** Angreifer versuchen, den privaten Schlüssel durch Faktorisierung des öffentlichen Modulus zu berechnen.
- **Timing-Angriffe:** Analyse der Zeit, die für die Entschlüsselung benötigt wird.
- **Man-in-the-Middle:** Angreifer tauscht öffentliche Schlüssel aus, um Nachrichten abzufangen.

## Vergleich mit symmetrischer Verschlüsselung
- **Asymmetrisch:** Zwei Schlüssel, langsamer, aber Schlüsselverteilung ist sicherer und flexibler.
- **Symmetrisch:** Ein Schlüssel, schneller, aber Schlüsselverteilung ist ein Problem.
- **Anwendung:** Asymmetrische Verfahren werden oft für den Schlüsselaustausch und digitale Signaturen verwendet, symmetrische für die eigentliche Datenverschlüsselung.

## Python-Codebeispiel: RSA-Verschlüsselung und -Entschlüsselung

```python
import rsa

# Schlüsselpaar erzeugen
(public_key, private_key) = rsa.newkeys(2048)

message = b"Geheime Nachricht!"

# Verschlüsseln
ciphertext = rsa.encrypt(message, public_key)

# Entschlüsseln
plaintext = rsa.decrypt(ciphertext, private_key)

print(f"Ursprünglich: {message}")
print(f"Verschlüsselt: {ciphertext.hex()}")
print(f"Entschlüsselt: {plaintext}")
```

**Hinweis:**
- Die Bibliothek `rsa` muss installiert sein (`pip install rsa`).
- In der Praxis werden oft hybride Verfahren verwendet: RSA für den Schlüsselaustausch, AES für die Datenverschlüsselung.
