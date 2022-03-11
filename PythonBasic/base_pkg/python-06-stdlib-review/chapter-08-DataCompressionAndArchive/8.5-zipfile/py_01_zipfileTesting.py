import sys, zipfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def zipfile_is_zipfile():
    for filename in ['README.txt', 'example.zip', 'bad_example.zip', 'notthere.zip']:
        print('{:>15} {}'.format(filename, zipfile.is_zipfile(filename)))
    pass

if __name__ == "__main__":
    # how to check if it is a zipfile? using is_zipfile() function
    zipfile_is_zipfile()