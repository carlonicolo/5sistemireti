# import required module
from cryptography.fernet import Fernet
import os

from EncryptDecryptFile import filekey


def encrypt(fernet, file_path):
    with open(file_path, 'rb') as file:
        original = file.read()
        encrypted = fernet.encrypt(original)
    with open(file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)

    print("File criptato: ")
    print(encrypted)


def decrypt(fernet, file_path):
    with open(file_path, 'rb') as enc_file:
        encrypted = enc_file.read()
        decrypted = fernet.decrypt(encrypted)
    with open(file_path, 'wb') as dec_file:
        dec_file.write(decrypted)
    print("File decriptato: ")
    print(decrypted)
    (filekey.key)
    
    if os.path.exists("filekey.key"):
      os.remove("filekey.key")
      print("chiave cancellata")
    else:
      print("Il file non esiste")


def createKey(file_path):
    print("Creazione chiave...")
    key = Fernet.generate_key()
    with open(file_path, 'wb') as filekey:
        filekey.write(key)


def main():
    control = input("Inserisci E per criptare, D per decriptare ---> ")
    file_path = input("Inserisci il path del file criptare/decriptare ---> ")

    controllo_key = input("Hai già una chiave salvata? SI/NO ---> ")
    if controllo_key == "SI" and control == "E":
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
            fernet = Fernet(key)
            try:
                encrypt(fernet, file_path)
                print("\n############ File criptato ############\n")
            except:
                print("\n################ Encryption doesn't work ######################\n")

    if controllo_key == "SI" and control == "D":
        with open('filekey.key', 'rb') as filekey:
            key = filekey.read()
            fernet = Fernet(key)
            decrypt(fernet, file_path)

    elif controllo_key == "NO":
        createKey(file_path)
        # print("Creazione chiave...")
        # key = Fernet.generate_key()
        # with open('filekey.key', 'wb') as filekey:
        #      filekey.write(key)
        with open(file_path, 'rb') as filekey:
            key = filekey.read()
            fernet = Fernet(key)

        if control == "E":
            encrypt(fernet, file_path)
        else:
            decrypt(fernet, file_path)


if __name__ == "__main__":
    main()

# TASK 1
# Una volta decriptato un file, la chiave utilizzata deve essere cancellata
# in modo tale da sapere che il file è nella forma originale

# TASK 2
# Gestire le eccezioni delle funzioni principali try, except

# TASK 3
# Crea una versione ad oggetti di questo semplice programmino
