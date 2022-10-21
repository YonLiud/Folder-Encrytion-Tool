import sys
import os
from cryptography.fernet import Fernet


cmdargs = sys.argv # cmd arguments ( path to target folder, path to key file )

fkey = open(cmdargs[2], 'rb').read() # read key from file
fkey = Fernet(fkey) # create Fernet object
path = cmdargs[1] # path to target file

with open(path, 'rb') as f:
    data = f.read()

decrypted = fkey.decrypt(data)

with open(path, 'wb') as f:
    f.write(decrypted)

