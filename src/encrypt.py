import sys
import os
from click import prompt
from cryptography.fernet import Fernet
from make_tarfile import make_tarfile as mt

path = sys.argv[1] # path to target folder

print(os.listdir(path)) # list contents of target folder

# prompt confirmation to encrypt
if not prompt('Encrypt files in ' + path + '?', default='y', show_default=True, type=bool):
    print('Aborting...')
    exit()

print('Compresing files...')

mt = mt(path + '.tar.gz', path) # create tar.gz archive of target folder