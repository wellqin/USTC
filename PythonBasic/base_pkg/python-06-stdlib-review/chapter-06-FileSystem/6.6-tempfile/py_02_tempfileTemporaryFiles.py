"""

compound modes, ez pz

+-------+--------+---------+---------+
|       |   r    |   w     | a       |
+-------+--------+---------+---------+
|  b    |   rb   |   wb    | ab      |
+-------+--------+---------+---------+
|  +    |   r+   |   w+    | a+      |
+-------+--------+---------+---------+
|  b+   |  rb+   |  wb+    | ab+     | 
+-------+--------+---------+---------+
|  x    |        |         |         |
+-------+--------+---------+---------+
|  t    |        |         |         |
+-------+--------+---------+---------+

"""

import sys, tempfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def tempfile_manual_vs_TemporaryFile():
    import os
    print('Building a filename with PID:')
    filename = 'C:\\Users\\5106001995\\AppData\\Local\\Temp\\guess_my_name.{}.txt'.format(os.getppid())
    with open(filename, 'w+b') as temp:
        print('temp:')
        print('     {!r}'.format(temp))
        print('temp.name:')
        print('     {!r}'.format(temp.name))
    # clean up the temporary file by yourself
    os.remove(filename)
    print()
    # ! elegant approach .. thunds up
    # ! by default the file handle is created with mode 'w+b' 
    # ! so that it hehaves consistently on all platform
    print('TemporaryFile:')
    with tempfile.TemporaryFile() as temp:
        print('temp:')
        print('     {!r}'.format(temp))
        print('temp.name:')
        print('     {!r}'.format(temp .name))
    # automatically cleans up the file
    
    pass

@addBreaker
def tempfile_TemporaryFile_binary():
    with tempfile.TemporaryFile() as f:
        f.write(b'some data')
        f.seek(0)
        print(f.read())

@addBreaker
def tempfile_TemporaryFile_text():
    # ! tempfile `with` statement is totally Different with FileIO open `with` block
    with tempfile.TemporaryFile(mode='w+t') as f:
        f.writelines([
            'first\n',
            'sencond\n'
        ])
        f.seek(0)
        for line in f:
            # print(f.name)
            print(line.rstrip())

if __name__ == "__main__":
    # TemporaryFile() function creates a file, and on platforms where  it is possbile,
    # ! unlinks the new file immediately.
    # * As a consequence, another program cannot find or open the file,
    # ? since there is no reference to it in the file system table.
    # ! The file created by TemporaryFile() is removed antomatically when it is closed,
    # ! wheather by calling `close()` or by using the context manager API and `with` statement
    tempfile_manual_vs_TemporaryFile()
    # write data into a temporary file and read, then delete. `w+b`
    tempfile_TemporaryFile_binary()
    # mode: `w+t`
    tempfile_TemporaryFile_text()