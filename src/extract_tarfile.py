import tarfile

def extract_tarfile(path):
    tar = tarfile.open(path, "r:gz")
    tar.extractall(path[:-7])
    tar.close()