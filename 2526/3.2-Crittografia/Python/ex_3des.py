from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

# Genera chiave da 24 byte (192 bit totali)
# e corregge la parità dei bit
key = DES3.adjust_key_parity(get_random_bytes(24))


# Modalità CBC: ogni blocco dipende dal precedente
# Più sicura di ECB
cipher = DES3.new(key, DES3.MODE_CBC)
plaintext = b"Messaggio segreto da proteggere bim bum bam zig zag"


# Padding automatico per blocchi da 8 byte
ciphertext = cipher.encrypt(pad(plaintext, 8))
print("Cifrato:", ciphertext.hex())
print("IV usato:", cipher.iv.hex())

# Decifratura: serve lo stesso IV
cipher_dec = DES3.new(key, DES3.MODE_CBC, cipher.iv)
decrypted = unpad(cipher_dec.decrypt(ciphertext), 8)
print("Decifrato:", decrypted.decode())