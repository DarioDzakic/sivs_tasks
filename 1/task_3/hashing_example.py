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
if __name__ == "__main__":
    password = 'meinPasswort123'
    hash_value, salt = hash_password(password)
    print(f"Hash: {hash_value}\nSalt: {salt.hex()}")
