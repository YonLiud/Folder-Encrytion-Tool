import sys
import os
from cryptography.fernet import Fernet
from numpy import extract
from extract_tarfile import extract_tarfile as et

print('Decrypting files...')

cmdargs = sys.argv # cmd arguments ( path to target folder, path to key file )

fkey = open(cmdargs[2], 'rb').read() # read key from file
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