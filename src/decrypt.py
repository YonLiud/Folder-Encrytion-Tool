import sys
import os
from cryptography.fernet import Fernet
from numpy import extract
from extract_tarfile import extract_tarfile as et

cmdargs = sys.argv # cmd arguments ( path to target folder, path to key file )

def decrypt(path, keypath):
    fkey = open(keypath, 'rb').read() # read key from file
    fkey = Fernet(fkey)

    with open(path, 'rb') as f:
        data = f.read()
    try:
        decrypted = fkey.decrypt(data)
    except Exception as e:
        raise e

    with open(path, 'wb') as f:
        f.write(decrypted)

    et(path)

    # delete archive
    os.remove(path)

    # remove .secured suffix from folder name
    fname = path.split('\\')[-1]
    new_name = fname[:-8]
    os.rename(path[:-7], path[:-7][:-8])
    
    return path[:-7][:-8]