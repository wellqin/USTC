import sys, zipfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def zipfile_append():
    print('creating archive')
    with zipfile.ZipFile('append.zip', mode='w') as zf:
        zf.write('README.txt')
    print()
    print('appending to the archive')
    with zipfile.ZipFile('append.zip', mode='a') as zf:
        zf.write('README.txt', arcname='README2.txt')
    print()
    pass


if __name__ == "__main__":
    zipfile_append()