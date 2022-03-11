import os, tempfile

lorem = '''Lorem ipsum dolor sit amet, consectetuer
adipiscing elit. Vivamus eget elit. In posuere mi non
risus. Mauris id quam posuere lectus sollicitudin
varius. Praesent at mi. Nunc eu velit. Sed augue massa,
fermentum id, nonummy a, nonummy sit amet, ligula. Curabitur
eros pede, egestas at, ultricies ac, apellentesque eu,
tellus.

Sed sed odio sed mi luctus mollis. Integer et nulla ac augue
convallis accumsan. Ut felis. Donec lectus sapien, elementum
nec, condimentum ac, interdum non, tellus. Aenean viverra,
mauris vehicula semper porttitor, ipsum odio consectetuer
lorem, ac imperdiet eros odio a sapien. Nulla mauris tellus,
aliquam non, egestas a, nonummy et, erat. Vivamus sagittis
porttitor eros.'''

def make_tempfile():
    """
    # tempfile.mkstemp(suffix=None, prefix=None, dir=None, text=False)
    # ! Creates a temporary file in the most secure manner possible.  --> aha, shorts for `make secure temp`
    # There are no race conditions in the file’s creation, assuming that the platform properly implements the os.O_EXCL flag for os.open(). 
    # ! The file is readable and writable only by the creating user ID. 
    # If the platform uses permission bits to indicate whether a file is executable, the file is executable by no one. 
    # The file descriptor is not inherited by child processes.

    ! Unlike TemporaryFile(), the user of mkstemp() is responsible for deleting the temporary file when done with it.
    """
    fd, temp_file_name = tempfile.mkstemp()
    os.close(fd)
    with open(temp_file_name, 'wt') as f:
        f.write(lorem)
    return temp_file_name

def cleanup(filename):
    os.remove(filename)

if __name__ == "__main__":
    fn = make_tempfile()
    print(fn)
    cleanup(fn)