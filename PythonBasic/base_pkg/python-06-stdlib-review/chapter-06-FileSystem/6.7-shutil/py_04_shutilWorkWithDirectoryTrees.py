import sys, shutil
sys.path.append('.')
from pkg.breaker import addBreaker
import glob, pprint, tempfile

def cleanup(d: str):
    import os, pathlib
    try:
        # winos does NOT allow to do this ..
        # manual deletion
        for file in pathlib.Path(d).glob('*.*'):
            os.unlink(file)
        os.rmdir(d)
    except FileNotFoundError:
        pass

@addBreaker
def shutil_copytree():
    print('BEFORE   :')
    tmpdir      = tempfile.gettempdir()
    example_dir = tmpdir + '\\example'
    cleanup(example_dir)
    pprint.pprint(glob.glob(example_dir))
    # * oh, no need to prefabricate `example` directory when using copytree()
    shutil.copytree('.\\chapter-06-FileSystem\\6.7-shutil', example_dir)
    print('\nAFTER  :')
    pprint.pprint(glob.glob(example_dir))

@addBreaker
def shutil_copytree_verbose():
    def verbose_copy(src, dst):
        print('copying\n {!r}\n to {!r}'.format(src, dst))
        return shutil.copy2(src, dst)

    tmpdir = tempfile.gettempdir()
    example_dir = tmpdir + '\\example'
    cleanup(example_dir)
    print('BEFORE   :')
    pprint.pprint(glob.glob(example_dir))
    print()
    shutil.copytree(
        '.\\chapter-06-FileSystem\\6.7-shutil',
        example_dir,
        copy_function=verbose_copy,
        ignore=shutil.ignore_patterns('*.py')
    )
    print('\nAFTER  :')
    pprint.pprint(glob.glob(example_dir))

@addBreaker
def shutil_rmtree():
    print('BEFORE   :')
    tmpdir = tempfile.gettempdir()
    example_dir = tmpdir + '\\example'
    pprint.pprint(glob.glob(example_dir))
    shutil.rmtree(example_dir)
    print('\nAFTER  :')
    pprint.pprint(glob.glob(example_dir))

@addBreaker
def shutil_move():
    with open('example.txt', 'wt') as f:
        f.write('juice')
    print('BEFORE   :', glob.glob('example*'))
    shutil.move('example.txt', 'example')
    print('AFTER    :', glob.glob('example*'))










if __name__ == "__main__":
    # default setting
    shutil_copytree()
    # user defined behavior by passing `copy_function` and `ignore`
    shutil_copytree_verbose()
    # built-in rmtree
    shutil_rmtree()
    # move file/folder to dst
    shutil_move()