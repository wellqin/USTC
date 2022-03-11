import sys, shutil
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def shutil_get_archive_format():
    # working with `tarfile`, and `zipfile`
    for fmt, desc in shutil.get_archive_formats():
        print('{:<5}: {}'.format(fmt, desc))    
    pass

@addBreaker
def shutil_make_archive():
    import logging, tarfile
    logging.basicConfig(
        format='%(message)s',
        stream=sys.stdout,
        level=logging.DEBUG,
    )
    logger = logging.getLogger('pymotw')
    print('Creating archive:')
    shutil.make_archive(
        'example',
        'gztar',
        root_dir='.',
        base_dir='example',
        logger=logger,
    )

    print('\nArchive contents:')
    with tarfile.open('example.tar.gz', 'r') as t:
        for n in t.getnames():
            print(n)

@addBreaker
def shutil_get_unpack_formats():
    for fmt, exts, desc in shutil.get_unpack_formats():
        print('{:<5}: {}, names ending in {}'.format(fmt, desc, exts))

@addBreaker
def shutil_unpack_archive():
    import tempfile, pathlib
    with tempfile.TemporaryDirectory() as d:
        print('Unpacking archive:')
        shutil.unpack_archive(
            'example.tar.gz',
            extract_dir=d,
        )
        print(d)
        print('\nCreated:')
        prefix_len = len(d) + 1
        for extracted in pathlib.Path(d).rglob('*'):
            print(str(extracted)[prefix_len:])

if __name__ == "__main__":
    # get archive formats
    shutil_get_archive_format()
    # make archive
    shutil_make_archive()
    # get unpack formats
    shutil_get_unpack_formats()
    # unpack archive
    shutil_unpack_archive()