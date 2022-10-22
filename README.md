# LFES- Light Folder Encryption System

## About

Encrypt folders using Python technology without hussle.


![workflow](https://i.imgur.com/2BdiO5S.png)

## Example:

### Encryption

```shell
$ python3 src\encrypt.py test\private\
```
_Encryption is possible for multiple files using the same key by:_

**_$ python3 src\encrypt.py test\private\ test\private.key_**

_the key must be compatible with Fernet's encryption_
### Decryption

```shell
$ python3 src\decrypt.py test\private.secured.tar.gz test\private.key
```