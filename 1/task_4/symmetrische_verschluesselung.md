# Symmetrische Verschlüsselung: Beispiel mit AES

## Gewählter Algorithmus: AES (Advanced Encryption Standard)
AES ist ein moderner, weit verbreiteter symmetrischer Verschlüsselungsalgorithmus. Er arbeitet mit festen Blockgrößen (128 Bit) und Schlüssellängen von 128, 192 oder 256 Bit. AES verschlüsselt Daten in Blöcken und ist sehr effizient und sicher, wenn korrekt implementiert.

## Prinzip von AES
Bei der symmetrischen Verschlüsselung wird derselbe Schlüssel zum Ver- und Entschlüsseln verwendet. Der Sender verschlüsselt die Nachricht mit dem Schlüssel, der Empfänger entschlüsselt sie mit demselben Schlüssel.

## Mögliche Angriffsszenarien
- **Brute-Force-Angriff:** Angreifer versucht alle möglichen Schlüssel durch.
- **Key-Recovery-Angriff:** Angreifer versucht, den Schlüssel durch Schwachstellen im System zu erlangen.
- **Side-Channel-Angriffe:** Ausnutzung von Informationen wie Stromverbrauch oder Zeitmessung.

## Unterschiede zur asymmetrischen Verschlüsselung
- **Symmetrisch:** Ein Schlüssel für Ver- und Entschlüsselung, schneller, aber Schlüsselverteilung ist kritisch.
- **Asymmetrisch:** Zwei Schlüssel (öffentlich/privat), langsamer, aber Schlüsselverteilung ist einfacher und sicherer.

## Python-Codebeispiel: AES-Verschlüsselung und -Entschlüsselung

```python
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# Nachricht und Schlüssel
def encrypt_decrypt_demo():
    key = os.urandom(32)  # 256 Bit Schlüssel
    iv = os.urandom(16)   # Initialisierungsvektor für CBC-Modus
    message = b"Geheime Information!"

    # Padding (AES benötigt Blockgröße 16)
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(message) + padder.finalize()

    # Verschlüsselung
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()

    # Entschlüsselung
    decryptor = cipher.decryptor()
    decrypted_padded = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    decrypted = unpadder.update(decrypted_padded) + unpadder.finalize()

    print(f"Ursprünglich: {message}")
    print(f"Verschlüsselt: {ciphertext.hex()}")
    print(f"Entschlüsselt: {decrypted}")

if __name__ == "__main__":
    encrypt_decrypt_demo()
```

**Hinweis:**
- Die Bibliothek `cryptography` muss installiert sein (`pip install cryptography`).
- Der Schlüssel und IV sollten sicher gespeichert und übertragen werden.
