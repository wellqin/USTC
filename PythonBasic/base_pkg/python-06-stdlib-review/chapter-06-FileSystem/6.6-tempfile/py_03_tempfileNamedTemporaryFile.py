import sys, tempfile, os, pathlib
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def tempfile_NamedTemporaryFile():
    with tempfile.NamedTemporaryFile() as f:
        print('temp:')
        print(' {!r}'.format(f))
        print('temp.name:')
        print(' {!r}'.format(f.name))
        f = pathlib.Path(f.name)
    print('Exists after close:', f.exists())
    pass

if __name__ == "__main__":
    # sometimes, having a named temporary file is import
    # for applications spanning multiple processes, or even hosts
    # naming the file is the simplest way to pass it between parts of the application
    # ! NamedTemporaryFile() creates a file w/o unlinking it.
    # ! so it retains its name (accessed with the `name` attribute)
    # ? BUT wtf is the authentic differnce in essence?
    # TemporaryFile() vs NamedTemporaryFile().
    # no different on winos
    """python
    # tempfile source code, line 558
    if _os.name != 'posix' or _os.sys.platform == 'cygwin':
        # On non-POSIX and Cygwin systems, assume that we cannot unlink a file
        # while it is open.
        TemporaryFile = NamedTemporaryFile
    """
    tempfile_NamedTemporaryFile()