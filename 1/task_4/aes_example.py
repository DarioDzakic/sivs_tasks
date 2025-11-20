from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
import os

# AES-Verschlüsselung und -Entschlüsselung

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
