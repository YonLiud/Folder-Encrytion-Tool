from encrypt import encrypt
from decrypt import decrypt
import os
from click import prompt

opt = prompt("Encrypt or Decrypt?", type=str)

if opt == "Encrypt":
    path = input("Insert Directory Path: ")
    key = input("Insert Key Path: ")

    if key == "":
        key = None

    print(os.listdir(path)) # list contents of target folder

    if not prompt('Encrypt files in ' + path + '?', default='y', show_default=True, type=bool):
        print('Aborting...')
        exit()

    encrypt(path)
elif opt == "Decrypt":
    path = input("Insert Directory Path: ")
    key = input("Insert Key Path: ")

    if key == "":
        print("No key provided, using default key")
        key = os.path.basename(path)
        key = key[:-15]
        key = key + ".key"
        # locate key in same directory as encrypted file
        key = os.path.join(os.path.dirname(path), key)
        if not os.path.isfile(key):
            print("No key found, aborting...")
            exit()
        print("Using key: " + key)
    decrypt(path, key)
    
else:
    print("Invalid option")

    exit()