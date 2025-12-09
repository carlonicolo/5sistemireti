from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes

# Genera una chiave casuale di 8 byte
# (56 bit effettivi + 8 bit di parità)
key = get_random_bytes(8)

# Crea un oggetto cipher in modalità ECB
# (Electronic CodeBook - la più semplice)
cipher = DES.new(key, DES.MODE_ECB)

# DES lavora su blocchi da 8 byte
plaintext = b"Hello123"


# Cifratura del blocco
ciphertext = cipher.encrypt(plaintext)
print("Chiave:", key.hex())
print("Cifrato:", ciphertext.hex())


# Decifratura
cipher_dec = DES.new(key, DES.MODE_ECB)
decrypted = cipher_dec.decrypt(ciphertext)
print("Decifrato:", decrypted)
