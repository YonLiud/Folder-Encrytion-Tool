# LFES- Light Folder Encryption System

## About

Encrypt folders using Symmetric Encryption (Fernet) technology without hussle.


![workflow](https://i.imgur.com/2BdiO5S.png)

## Usage:

```bash
$ python3 src\\main.py
```

and follow the instructions on the screen.

# Notes:
Encryption and Decryption are not reversible. So, make sure you have a backup of your files before you encrypt them.

You cannot recover your files if the exact file is not used for decryption.

If you don't want/have an existing key for encryption, LFES can generate one for you upon encryption.