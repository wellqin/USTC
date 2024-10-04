import sys, tarfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def tarfile_getname():
    with tarfile.open('example.tar', 'r') as t:
        print(t.getnames())
    
    pass


if __name__ == "__main__":
    tarfile_getname()