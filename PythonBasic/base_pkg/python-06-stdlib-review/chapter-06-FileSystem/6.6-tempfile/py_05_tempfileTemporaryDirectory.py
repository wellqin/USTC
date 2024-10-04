import sys, tempfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def tempfile_TemporaryDirectory():
    import pathlib
    with tempfile.TemporaryDirectory() as directory_name:
        the_dir = pathlib.Path(directory_name)
        print(the_dir)
        a_file  = the_dir / 'a_file.txt' 
        a_file.write_text('This file is deleted')
    print('Directory exists after?', the_dir.exists())
    print('Contents after:', list(the_dir.glob('*')))
    pass

if __name__ == "__main__":
    tempfile_TemporaryDirectory()