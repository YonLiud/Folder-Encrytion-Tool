from encrypt import encrypt
import os
from click import prompt


path = input("Insert Directory Path: ")
key = input("Insert Key Path: ")

if key == "":
    key = None

print(os.listdir(path)) # list contents of target folder

if not prompt('Encrypt files in ' + path + '?', default='y', show_default=True, type=bool):
    print('Aborting...')
    exit()

encrypt(path)