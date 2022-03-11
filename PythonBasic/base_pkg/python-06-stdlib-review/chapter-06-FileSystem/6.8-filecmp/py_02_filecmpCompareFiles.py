import sys, filecmp
sys.path.append('.')
from pkg.breaker import addBreaker
import os, pathlib

@addBreaker
def filecmp_cmp():
    curdir = os.path.dirname(__file__)
    os.chdir(curdir)
    print('common_file  :', end=' ')
    print(filecmp.cmp(
        'example/dir1/common_file',
        'example/dir2/common_file'), 
        end=' ',
    )
    print(filecmp.cmp(
        'example/dir1/common_file',
        'example/dir2/common_file', 
        shallow=False,)
    )

    print('\nnot_the_same :', end=' ')
    print(filecmp.cmp(
        'example/dir1/not_the_same',
        'example/dir2/not_the_same',),
        end=' '
    )
    print(filecmp.cmp(
        'example/dir1/not_the_same',
        'example/dir2/not_the_same',
        shallow=False)
    )

    print('\nidentical    :', end=' ')
    print(filecmp.cmp(
        'example/dir1/file_only_in_dir1',
        'example/dir1/file_only_in_dir1',),
        end = ' '
    )
    print(filecmp.cmp(
        'example/dir1/file_only_in_dir1',
        'example/dir1/file_only_in_dir1',
        shallow=False),
    )

    pass

@addBreaker
def filecmp_cmpfiles():
    os.chdir(pathlib.Path(__file__).parent)
    # determine the items that exist in both directories
    d1_contents  = set(os.listdir('example/dir1'))
    d2_contents  = set(os.listdir('example/dir2'))
    common       = list(d1_contents & d2_contents)
    common_files = [ f for f in common if pathlib.Path('example/dir1/' + f).is_file()]
    print('Common files :', common_files)
    # compare the directories
    # ! if files could not be compared (due to permisson problem or for any other reason)
    match, mismatch, errors = filecmp.cmpfiles(
        'example/dir1',
        'example/dir2',
        common_files,
    )
    print('Match        :', match)
    print('MisMatch     :', mismatch)
    print('Erros        :', errors)

if __name__ == "__main__":
    # ! by default, comparing two file contents, file descriptors
    # ! setting `shallow` to false, to compare file descriptors ONLY
    filecmp_cmp()
    # comparing a set of files in two directories w/o recursing
    filecmp_cmpfiles()