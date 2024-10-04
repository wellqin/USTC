import sys, tarfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def tarfile_add():
    print('creating archive')
    with tarfile.open('tarfile_add.tar', 'w') as out:
        print('adding README.txt')
        out.add('README.txt')
    print()
    print('Contents:')
    with tarfile.open('tarfile_add.tar', 'r') as t:
        for member_info in t.getmembers():
            print(member_info.name)
    
    pass

if __name__ == "__main__":
    tarfile_add()