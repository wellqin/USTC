import sys, zipfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def zipfile_namelist():
    with zipfile.ZipFile('example.zip', 'r') as zf:
        print(zf.namelist())
    pass

if __name__ == "__main__":
    zipfile_namelist()