import sys
import os
from cryptography.fernet import Fernet
from numpy import extract
from extract_tarfile import extract_tarfile as et

print('Decrypting files...')

cmdargs = sys.argv # cmd arguments ( path to target folder, path to key file )

try:
    fkey = open(cmdargs[2], 'rb').read() # read key from file
except IndexError:
    print('No key file specified. Aborting...')
    exit()
except Exception as e:
    print('Unable to read key file: ' + str(e))
    exit()
fkey = Fernet(fkey) # create Fernet object
path = cmdargs[1] # path to target file

with open(path, 'rb') as f:
    data = f.read()

decrypted = fkey.decrypt(data)

with open(path, 'wb') as f:
    f.write(decrypted)

print('Decompressing files...')

et(path)

print('Done! \nDecrypted files are in ' + path[:-7])

# delete archive
os.remove(path)

# remove .secured suffix from folder name
fname = path.split('\\')[-1]
new_name = fname[:-8]
os.rename(path[:-7], path[:-7][:-8])
