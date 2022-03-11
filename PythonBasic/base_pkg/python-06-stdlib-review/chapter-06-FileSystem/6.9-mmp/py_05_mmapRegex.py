import sys, mmap
sys.path.append('.')
from pkg.breaker import addBreaker
import os
import re

@addBreaker
def mmap_regex():
    os.chdir(os.path.dirname(__file__))
    pattern = re.compile(
        rb'(\.\W+)?([^.]?nulla[^.]*?\.)',
        re.DOTALL | re.IGNORECASE | re.MULTILINE,
    )

    with open('lorem.txt', 'r') as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ) as m:
            for match in pattern.findall(m):
                print(match[1].replace(b'\n', b' '))


if __name__ == "__main__":
    mmap_regex()