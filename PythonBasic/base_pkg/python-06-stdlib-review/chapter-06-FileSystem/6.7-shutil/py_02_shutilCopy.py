import sys, shutil
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def shutil_copyfile():
    import glob, pathlib
    try:
        pathlib.Path('readme.md.copy').unlink()
    # ? FileNotFoundError vs FileExistsError?
    # * FileNotFoundError -- Raised when a file or directory is requested but doesn’t exist. Corresponds to errno ENOENT.
    # * FileExistsError -- Raised when trying to create a file or directory which already exists. Corresponds to errno EEXIST.

    except FileNotFoundError as err:
        print(err)
    print('BEFORE:', glob.glob('readme.*'))
    shutil.copyfile('readme.md', 'readme.md.copy')
    print('AFTER :', glob.glob('readme.*'))

@addBreaker
def shutil_copyfileobj():
    import io, os
    class VerboseStringIO(io.StringIO):
        def read(self, n=-1):
            next = io.StringIO.read(self, n)
            print('read({}) got {} bytes'.format(n, len(next)))
            return next
    
    lorem_ipsum = '''Lorem ipsum dolor sit amet, consectetuer
    adipiscing elit. Vestibulum aliquam mollis dolor. Donec
    vulputate nunc ut diam. Ut rutrum mi vel sem. Vestibulum
    ante ipsum.'''

    print('Default:')
    input  = VerboseStringIO(lorem_ipsum)
    output = io.StringIO()
    shutil.copyfileobj(input, output)

    print()
    
    print('All at once:')
    input  = VerboseStringIO(lorem_ipsum)
    output = io.StringIO()
    # ! default behavior is to read all of the input at one time
    shutil.copyfileobj(input, output, -1)
    
    print()

    print('Blocks of 256:')
    input  = VerboseStringIO(lorem_ipsum)
    output = io.StringIO()
    # ! positive integer is to read a specific block size ..
    shutil.copyfileobj(input, output, 256)

@addBreaker
def shutil_copy():
    import glob, os
    try:
        os.mkdir('example')
    except FileExistsError as err:
        print(err)
    print('BEFORE   :', glob.glob('example/*'))
    shutil.copy('readme.md', 'example')
    print('AFTER    :', glob.glob('example/*'))
    pass

@addBreaker
def shutil_copy2():
    import pathlib, time
    # ! strftime(fmt, time_struct)
    # ! strptime('', time_struct)
    def show_file_info(filename):
        state = pathlib.Path(filename).stat()
        print('     Mode     :', oct(state.st_mode))
        print('     Created  :', time.ctime(state.st_ctime))
        print('     Accessed :', time.ctime(state.st_atime))
        print('     Modified :', time.ctime(state.st_mtime))
    try:
        pathlib.Path('example').mkdir()
    except FileExistsError as err:
        print(err)
    print('SOURCE:')
    show_file_info('readme.md')
    shutil.copy2('readme.md', 'example')
    print('DEST:')
    show_file_info('example/readme.md')
    pass







if __name__ == "__main__":
    # Because the function opens the input file for reading, regardless of its type, 
    # special files (such as Unix device nodes) cannot be copied as new special files with copyfile()
    # ! The implementation of copyfile() uses the lower-level function copyfileobj(). While
    # the arguments to copyfile() are filenames, the arguments to copyfileobj() are open `file handles`
    shutil_copyfile()
    # low-level function
    shutil_copyfileobj()
    # copy()
    shutil_copy()
    # copy2() includes the getatime(), getmtime() in the meta-date copied
    # ! nice 69
    shutil_copy2()