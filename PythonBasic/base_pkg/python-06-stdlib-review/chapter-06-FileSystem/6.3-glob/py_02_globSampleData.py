import pathlib

def makeSampleData():
    """
    dir
    dir/file.txt
    dir/file1.txt
    dir/file2.txt
    dir/filea.txt
    dir/fileb.txt
    dir/file?.txt
    dir/file*.txt
    dir/file[.txt
    dir/subdir
    dir/subdir/subfile.txt
    """
    dirs = [
        './dir',
        './dir/subdir'
    ]
    dir_files = [
        'dir/file.txt',
        'dir/file1.txt',
        'dir/file2.txt',
        'dir/filea.txt',
        'dir/fileb.txt',
        'dir/file+.txt',
        'dir/file-.txt',
        'dir/file[.txt',
        'dir/subdir/subfile.txt'
    ]

    for dr in dirs:
        try:
            pathlib.Path(dr).mkdir()
        except FileExistsError as err:
            print(err)
    for file in dir_files:
        try:
            pathlib.Path(file).touch()
        except FileExistsError as err:
            print(err)

if __name__ == "__main__":
    makeSampleData()
    