def download_file(file, filename):
    with open(filename, 'wb') as f:
        f.write(file)
