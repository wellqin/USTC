import sys, filecmp
sys.path.append('.')
from pkg.breaker import addBreaker
import os, pprint

@addBreaker
def filecmp_dircmp_list():
    os.chdir(os.path.dirname(__file__))
    dc = filecmp.dircmp(
        'example/dir1',
        'example/dir2',
    )
    print('Left     :')
    pprint.pprint(dc.left_list)

    print('\nRight  :')
    pprint.pprint(dc.right_list)
    pass

@addBreaker
def filecmp_dircmp_list_filter():
    os.chdir(os.path.dirname(__file__))
    dc = filecmp.dircmp(
        'example/dir1',
        'example/dir2',
        ignore=['common_file']
    )
    print('Left     :')
    pprint.pprint(dc.left_list)

    print('\nRight  :')
    pprint.pprint(dc.right_list)
    pass

@addBreaker
def filecmp_dircmp_membership():
    dc = filecmp.dircmp(
        'example/dir1',
        'example/dir2',
    )
    print('Common   :')
    pprint.pprint(dc.common)
    print('\nLeft   :')
    pprint.pprint(dc.left_only)
    print('\nRight  :')
    pprint.pprint(dc.right_only)

@addBreaker
def filecmp_dircmp_common_stat():
    dc = filecmp.dircmp(
        'example/dir1',
        'example/dir2',
    )
    print('Common       :')
    pprint.pprint(dc.common)
    print('\nDirectories:')
    pprint.pprint(dc.common_dirs)
    print('\nFiles      :')
    pprint.pprint(dc.common_files)
    print('\nFunny      :')
    pprint.pprint(dc.common_funny)
    pass

@addBreaker
def filecmp_dircmp_diff():
    os.chdir(os.path.dirname(__file__))
    dc = filecmp.dircmp(
        'example/dir1',
        'example/dir2',
    )
    print('Same         :', dc.same_files)
    print('Different    :', dc.diff_files)
    print('Funny        :', dc.funny_files)

@addBreaker
def filecmp_dircmp_subdirs():
    os.chdir(os.path.dirname(__file__))
    dc = filecmp.dircmp(
        'example/dir1',
        'example/dir2',
    )
    print('Subdirs:')
    print(dc.subdirs)

if __name__ == "__main__":
    # ! besides report, useful things
    filecmp_dircmp_list()
    # passing `ignore` to filter a list of names
    # ! by default, the names `RCS`, `CVS`, `tags` are ignored
    filecmp_dircmp_list_filter()
    # ! category
    filecmp_dircmp_membership()
    # ! 'funny' items
    filecmp_dircmp_common_stat()
    # ! diff
    filecmp_dircmp_diff()
    # ! subdirs
    # attr `subdirs` is a dictionary mapping the directory name to new `dircmp` obj
    filecmp_dircmp_subdirs()