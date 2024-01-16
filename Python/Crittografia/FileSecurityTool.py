# import required module
from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()

# string the key in a file
# Above code will generate a file with the name filekey.key. 
# The file will contain one line, which is a string acting as a ke
with open('filekey.key', 'wb') as filekey:
    filekey.write(key)

""" Encrypt the file using the key generated
Now we have an encrypted key and file to be encrypted. Now write code to encrypt this file:

1 - Open the file that contains the key.
2 - Initialize the Fernet object and store it in the fernet variable.
3 - Read the original file.
4 - Encrypt the file and store it into an object.
5 - Then write the encrypted data into the same file nba.csv. """

# opening the key
with open('filekey.key', 'rb') as filekey:
	key = filekey.read()

# using the generated key
fernet = Fernet(key)

#---------------- Encrypt ------------------

# opening the original file to encrypt
with open('estado.sql', 'rb') as file:
	original = file.read()
	
# encrypting the file
encrypted = fernet.encrypt(original)

# opening the file in write mode and 
# writing the encrypted data
with open('estado.sql', 'wb') as encrypted_file:
	encrypted_file.write(encrypted)

#----------------------------------------------

#------------- Decrypt ------------------------

""" Decrypt the encrypted file
We have to use the same key to decrypt the file:

Initialize the Fernet object and store it in the fernet variable.
Read the encrypted file.
Decrypt the file and store it into an object.
Then write the decrypted data into the same file nba.csv. """

# using the key
fernet = Fernet(key)

# opening the encrypted file
with open('estado.sql', 'rb') as enc_file:
	encrypted = enc_file.read()

# decrypting the file
decrypted = fernet.decrypt(encrypted)

# opening the file in write mode and
# writing the decrypted data
with open('estado.sql', 'wb') as dec_file:
	dec_file.write(decrypted)

#----------------------------------------------#

# TASK create two function to encrypt and decrypt a file
# taking as parameter the key and the filename to encrypt/decrypt

def encrypt(fernet, filename):
    pass

def decrypt(fernet, filename):
    pass

def main():
    # Hai già una chiave salvata ? 
    
    # Se la chiave non è salvata non esiste un file.key allora genera
    # la chiave e usala
    
    # Crea oggetto Fernet(key)
    
    # Task vuoi criptare o decriptare un file ?
    
    
    
    
    pass


if __name__ == "__main__":
    main()