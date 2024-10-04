import os
import sys

for entry in os.scandir('.'):
    if entry.is_dir():
        typ = 'dir'
    elif entry.is_file():
        typ = 'file'
    elif entry.is_symlink():
        typ = 'link'
    else:
        typ = 'unknown'
    print('{name:22} : {typ}'.format(
        name=entry.name,
        typ=typ,
    ))