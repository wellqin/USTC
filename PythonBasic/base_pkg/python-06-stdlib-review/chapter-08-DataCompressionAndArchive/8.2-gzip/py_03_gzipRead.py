import sys, gzip
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def gzip_read():
    import io
    with gzip.open('example.txt.gz', 'rb') as input_file:
        with io.TextIOWrapper(input_file, encoding='utf8') as dec:
            print(dec.read())
    pass

@addBreaker
def gzip_seek():
    with gzip.open('example.txt.gz', 'rb') as input_file:
        print('Entire file:')
        all_data = input_file.read()
        print(all_data)

        expected = all_data[5:15]
        # rewind to beiginning
        input_file.seek(0)
        # move ahead 5 bytes
        input_file.seek(5)
        print('starting at postion 5 for 10 bytes:')
        partial = input_file.read(10)
        print(partial)
        print()
        print(expected == partial)
    
    pass

if __name__ == "__main__":
    gzip_read()
    # seek().. ikr
    gzip_seek()