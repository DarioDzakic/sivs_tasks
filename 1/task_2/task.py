import hashlib

msg = "Hallo Welt!"
hash1 = hashlib.sha256(msg.encode()).hexdigest()
print("Original-Hash:", hash1)

# Nachricht wird verändert
msg2 = "Hallo welt!"   # kleines 'w'
hash2 = hashlib.sha256(msg2.encode()).hexdigest()
print("Veränderter Hash:", hash2)