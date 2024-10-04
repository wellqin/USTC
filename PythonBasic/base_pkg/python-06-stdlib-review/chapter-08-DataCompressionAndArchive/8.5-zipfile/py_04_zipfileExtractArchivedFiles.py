import sys, zipfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def zipfile_read():
    with zipfile.ZipFile('example.zip') as zf:
        for filename in ['README.txt', 'notthere.txt']:
            try:
                data = zf.read(filename)
            except KeyError:
                print('ERROR: Did not find {} in zip file'.format(filename))
            else:
                print(filename, ':')
                print(data)
            print()

    pass

if __name__ == "__main__":
    zipfile_read()