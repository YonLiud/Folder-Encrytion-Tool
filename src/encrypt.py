import sys
import os
from click import prompt
from cryptography.fernet import Fernet
from make_tarfile import make_tarfile as mt
import glob 

fkeypath = None

if len(sys.argv) > 2:
    fkeypath = open(sys.argv[2], 'rb').read() # read key from file

path = sys.argv[1] # path to target folder

print(os.listdir(path)) # list contents of target folder

# prompt confirmation to encrypt
if not prompt('Encrypt files in ' + path + '?', default='y', show_default=True, type=bool):
    print('Aborting...')
    exit()

print('Compresing files...')

mt = mt(path + '.tar.gz', path) # create tar.gz archive of target folder

print('Encrypting files...')


with open(path + '.tar.gz', 'rb') as f:
    data = f.read()
    
    
if not fkeypath:
    fkey = Fernet.generate_key() # create Fernet object
    # save key to file
    with open(path + '.key', 'wb') as f:
        f.write(fkey)
else:
    fkey = fkeypath

key = Fernet(fkey) # create Fernet object

encrypted = key.encrypt(data)

with open(path + '.tar.gz', 'wb') as f:
    f.write(encrypted)

# delete original folder
try:
    files = glob.glob(path + '/*')
    for file in files:
        os.remove(file)
    os.rmdir(path)
except Exception as e:
    print("Unable to delete folder: " + str(e))

f.close()

print('Done! \nEncrypted files are in ' + path + '.tar.gz')
