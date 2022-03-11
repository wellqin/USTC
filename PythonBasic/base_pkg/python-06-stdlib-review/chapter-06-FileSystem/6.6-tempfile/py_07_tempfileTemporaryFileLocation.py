import sys, tempfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def tempfile_settings():
    print('default tempdir  :', tempfile.tempdir)
    print('gettempdir()     :', tempfile.gettempdir())
    print('gettempprefix()  :', tempfile.gettempprefix())

@addBreaker
def tempfile_tempdir():
    tempfile.tempdir = '.'
    print('gettempdir() :', tempfile.gettempdir())

if __name__ == "__main__":
    # gettempdir() is using a straightforward algorithm to look throu
    # a list of locations for the first place where the current process can create a file
    # * orders:
    # environment variable `TMPDIR`
    # environment variable  `TEMP`
    # environment variable  `TMP`
    # a fallback, based on the platform (winos uses the first available of `C:\temp, c:\tmp, \temp, or \tmp`. other platforms use `/tmp, /var/tmp, /usr/tmp`)
    # if no other directry can be found, using the current working directory
    tempfile_settings()
    # ! user defined tempdir
    tempfile_tempdir()