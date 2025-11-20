import rsa

# Schlüsselpaar erzeugen
def rsa_demo():
    public_key, private_key = rsa.newkeys(2048)
    message = b"Geheime Nachricht!"
    # Verschlüsseln
    ciphertext = rsa.encrypt(message, public_key)
    # Entschlüsseln
    plaintext = rsa.decrypt(ciphertext, private_key)
    print(f"Ursprünglich: {message}")
    print(f"Verschlüsselt: {ciphertext.hex()}")
    print(f"Entschlüsselt: {plaintext}")

if __name__ == "__main__":
    rsa_demo()
