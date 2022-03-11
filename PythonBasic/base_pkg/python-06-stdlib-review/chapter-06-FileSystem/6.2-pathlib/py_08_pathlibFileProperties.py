import pathlib, sys
sys.path.append('.')
from pkg.breaker import addBreaker
import time

@addBreaker
def pathlib_stat():
    if len(sys.argv) == 1:
        filename = __file__
    else:
        filename = sys.argv[1]
    p         = pathlib.Path(filename)
    stat_info = p.stat()
    print('{}:'.format(filename))
    print('    Size         :', stat_info.st_size)
    print('    Permissions  :', stat_info.st_mode)
    print('    Owner        :', stat_info.st_uid)
    print('    Device       :', stat_info.st_dev)
    print('    Created      :', time.ctime(stat_info.st_ctime))
    print('    Last modified:', time.ctime(stat_info.st_mtime))
    print('    Last accessed:', time.ctime(stat_info.st_atime))
    # ! p.owner() NOT work on winos
    # print('    {} is owned by {}/{}'.format(p, p.owner(), p.group()))
    
    return

if __name__ == "__main__":
    pathlib_stat()