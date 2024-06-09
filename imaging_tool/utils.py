import hashlib

def calculate_checksums(file_path):
    checksums = {}
    checksums['md5'] = calculate_md5(file_path)
    checksums['sha256'] = calculate_sha256(file_path)
    return checksums

def calculate_md5(file_path, block_size=65536):
    md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            md5.update(block)
    return md5.hexdigest()

def calculate_sha256(file_path, block_size=65536):
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()
