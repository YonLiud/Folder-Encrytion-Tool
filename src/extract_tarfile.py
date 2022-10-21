import tarfile
import sys

path = sys.argv[1] # path to target file

file = tarfile.open(path)

file.extractall("./" + path[-1].split('.')[0])
  
file.close()