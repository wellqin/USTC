import sys, shutil
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def shutil_disk_usage():
    total_b, used_b, free_b = shutil.disk_usage('.')
    gib = 2 ** 30 # GiB == gibibyte
    gb  = 10 ** 9 # GB == gigabyte

    print('Total: {:6.2f} GB {:6.2f} GiB'.format(total_b / gb, total_b / gib))
    print('Used : {:6.2f} GB {:6.2f} GiB'.format(used_b / gb, used_b / gib))
    print('Free : {:6.2f} GB {:6.2f} GiB'.format(free_b / gb, free_b / gib))
    pass


if __name__ == "__main__":
    shutil_disk_usage()