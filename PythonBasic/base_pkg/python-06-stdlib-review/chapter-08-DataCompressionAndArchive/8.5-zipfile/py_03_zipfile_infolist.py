import sys, zipfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def zipfile_infolist():
    import datetime
    def print_info(archive_name):
        with zipfile.ZipFile(archive_name) as zf:
            for info in zf.infolist():
                print(info.filename)
                print(' Comment :', info.comment)
                mod_date = datetime.datetime(*info.date_time)
                print(' Modified :', mod_date)
                # ic ..
                if info.create_system == 0:
                    system = 'Windows'
                elif info.create_system == 3:
                    system = 'Unix'
                else:
                    system = 'UNKNOWN'
                print(' System :', system)
                print(' ZIP version :', info.create_version)
                print(' Compressed :', info.compress_size, 'bytes')
                print(' Uncompressed:', info.file_size, 'bytes')
                print()
    print_info('example.zip')
    pass

@addBreaker
def zipfile_getinfo():
    with zipfile.ZipFile('example.zip') as zf:
        for filename in ['README.txt', 'notthere.txt']:
            try:
                info = zf.getinfo(filename)
            except KeyError:
                print('ERROR: Did not find {} in zip file'.format(filename))    
            else:
                print('{} is {} bytes'.format(info.filename, info.file_size))
    pass


if __name__ == "__main__":
    zipfile_infolist()