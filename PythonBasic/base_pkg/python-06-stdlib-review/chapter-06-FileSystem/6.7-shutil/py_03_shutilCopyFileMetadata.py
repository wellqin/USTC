import sys, shutil
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def shutil_copymode():
    import os
    with open('file_to_change.txt', 'wt') as f:
        f.write('content')
    os.chmod('file_to_change.txt', 0o444)
    print('BEFORE   :', oct(os.stat('file_to_change.txt').st_mode))
    shutil.copymode('readme.md', 'file_to_change.txt')
    print('AFTER    :', oct(os.stat('file_to_change.txt').st_mode))
    pass

@addBreaker
def shutil_copystat():
    import os, time
    def show_file_info(filename):
        stat = os.stat(filename)
        print(' Mode        :', oct(stat.st_mode))
        print(' Created     :', time.ctime(stat.st_ctime))
        print(' Accessed    :', time.ctime(stat.st_atime))
        print(' Modified    :', time.ctime(stat.st_mtime))

    with open('file_to_change.txt', 'wt') as f:
        f.write('content')
    os.chmod('file_to_change.txt', 0o444)
    print('BEFORE   :')
    show_file_info('file_to_change.txt')
    shutil.copystat('readme.md', 'file_to_change.txt')
    print('\nAFTER    :')
    show_file_info('file_to_change.txt')

if __name__ == "__main__":
    # copy src_file access mode to dst_file
    shutil_copymode()
    # copy src_file stat to dst_file
    shutil_copystat()