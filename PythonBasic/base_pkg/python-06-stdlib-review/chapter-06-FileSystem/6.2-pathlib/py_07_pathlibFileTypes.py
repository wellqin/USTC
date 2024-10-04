import sys, pathlib
sys.path.append('.')
from pkg.breaker import addBreaker
import os, itertools

@addBreaker
def pathlib_types():
    # ! Unix-like os only
    root = pathlib.Path('test_files')
    # clean up from previous runs
    if root.exists():
        for f in root.iterdir():
            f.unlink()
    else:
        root.mkdir()

    # create test files
    (root / 'file').write_text('this is a regular file', encoding='utf8')
    (root / 'symlink').symlink_to('file')
    os.mkfifo(str(root / 'fifo'))

    # check the file types
    to_scan = itertools.chain(root.iterdir(),
                                [pathlib.Path('/dev/disk0'),
                                pathlib.Path('/dev/console')]
    )
    hfmt = '{:18s}' + ('    {:>5}' * 6)
    print(hfmt.format('Name', 'File', 'Dir', 'Link', 'FIFO', 'Block', 'Character'))
    print()
    fmt = '{:20s}   ' + ('{!r:>5}   ' * 6)
    for f in to_scan:
        print(fmt.format(
            str(f),
            f.is_file(),
            f.is_dir(),
            f.is_symlink(),
            f.is_fifo(),
            f.is_block_device(),
            f.is_char_device(),
        ))
    return

if __name__ == "__main__":
    # file types
    pathlib_types()
    # tests
    # pathlib_types()