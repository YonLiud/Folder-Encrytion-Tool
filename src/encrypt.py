import sys
import os
from click import prompt
from cryptography.fernet import Fernet
from make_tarfile import make_tarfile as mt

fkey = None

if len(sys.argv) > 2:
    fkey = open(sys.argv[2], 'rb').read() # read key from file

path = sys.argv[1] # path to target folder

print(os.listdir(path)) # list contents of target folder

# prompt confirmation to encrypt
if not prompt('Encrypt files in ' + path + '?', default='y', show_default=True, type=bool):
    print('Aborting...')
    exit()

print('Compresing files...')

mt = mt(path + '.tar.gz', path) # create tar.gz archive of target folder

print('Encrypting files...')

if fkey == None:
    fkey = Fernet(Fernet.generate_key())
else:
    fkey = Fernet(fkey)

with open(path + '.tar.gz', 'rb') as f:
    data = f.read()
    
encrypted = fkey.encrypt(data)

with open(path + '.tar.gz', 'wb') as f:
    f.write(encrypted)

# delete original folder
os.rmdir(path)

# save key to file
with open(path + '.key', 'wb') as f:
    f.write(str(fkey).encode())

f.close()

print('Done! \nEncrypted files are in ' + path + '.tar.gz')
