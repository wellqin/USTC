import sys, tarfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def tarfile_is_tarfile():
    for filename in ['README.txt', 'example.tar', 'bad_example.tar', 'notthere.tar']:
        try:
            print('{:>15}   {}'.format(filename, tarfile.is_tarfile(filename)))
        except IOError as err:
            print('{:>15}   {}'.format(filename, err))
    pass

if __name__ == "__main__":
    tarfile_is_tarfile()