# PGP: Funktionsweise und Anwendung

## Funktionsweise von PGP
PGP (Pretty Good Privacy) ist ein Verschlüsselungsprogramm, das sowohl asymmetrische als auch symmetrische Verfahren kombiniert. Es nutzt asymmetrische Verschlüsselung (z.B. RSA) für den Schlüsselaustausch und digitale Signaturen sowie symmetrische Verschlüsselung (z.B. AES) für die eigentliche Datenverschlüsselung. Dadurch werden die Vorteile beider Verfahren genutzt: Sicherheit beim Schlüsselaustausch und Effizienz bei der Datenverschlüsselung.

### Typische Einsatzgebiete
- E-Mail-Verschlüsselung
- Datei- und Festplattenverschlüsselung
- Digitale Signaturen zur Authentizität und Integrität

## Anwendung: Schlüsselpaar erzeugen, verschlüsseln, entschlüsseln, signieren

```python
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import serialization, hashes

# Schlüsselpaar erzeugen
def generate_keys():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

# Nachricht verschlüsseln
def encrypt_message(message, public_key):
    ciphertext = public_key.encrypt(
        message,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return ciphertext

# Nachricht entschlüsseln
def decrypt_message(ciphertext, private_key):
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    return plaintext

# Nachricht signieren
def sign_message(message, private_key):
    signature = private_key.sign(
        message,
        padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
        hashes.SHA256()
    )
    return signature

# Signatur prüfen
def verify_signature(message, signature, public_key):
    try:
        public_key.verify(
            signature,
            message,
            padding.PSS(mgf=padding.MGF1(hashes.SHA256()), salt_length=padding.PSS.MAX_LENGTH),
            hashes.SHA256()
        )
        return True
    except Exception:
        return False

if __name__ == "__main__":
    private_key, public_key = generate_keys()
    message = b"PGP-Demo-Nachricht!"
    ciphertext = encrypt_message(message, public_key)
    print(f"Verschlüsselt: {ciphertext.hex()}")
    decrypted = decrypt_message(ciphertext, private_key)
    print(f"Entschlüsselt: {decrypted}")
    signature = sign_message(message, private_key)
    print(f"Signatur: {signature.hex()}")
    print(f"Signatur gültig: {verify_signature(message, signature, public_key)}")
```

## Symmetrisch oder asymmetrisch?
PGP ist ein hybrides Verfahren: Es nutzt asymmetrische Verschlüsselung für den Schlüsselaustausch und symmetrische Verschlüsselung für die Daten. Das bietet hohe Sicherheit und Effizienz.

## Vorteile in der Praxis
- Sichere Kommunikation ohne vorherigen Schlüsselaustausch
- Digitale Signaturen für Authentizität und Integrität
- Effiziente Datenverschlüsselung
- Weit verbreitet und standardisiert
