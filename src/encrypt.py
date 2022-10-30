import sys
import os
from cryptography.fernet import Fernet
from make_tarfile import make_tarfile as mt
import glob 

def encrypt(folderpath, keypath=None):

    fkeypath = None

    if keypath:
        fkeypath = keypath

    path = folderpath

    mt(path + '.tar.gz', path) # create tar.gz archive of target folder

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

    os.rename(path + '.tar.gz', path + '.secured.tar.gz')
    try:
        files = glob.glob(path + '/*')
        for file in files:
            os.remove(file)
        os.rmdir(path)
    except Exception as e:
        print("Unable to delete folder: " + str(e))

    f.close()

    print('Done! \nEncrypted files are in ' + path + '.tar.gz')
