import sys, zipfile
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def zipfile_writestr_zipinfo():
    import time
    msg = b'This data did not exist in a file.'
    with zipfile.ZipFile('writestr_zipinfo.zip',
                        mode='w',
                        ) as zf:
        info = zipfile.ZipInfo('from_string.txt',
                                date_time=time.localtime(time.time()),
                                )
    info.compress_type = zipfile.ZIP_DEFLATED
    info.comment = b'Remarks go here'
    info.create_system = 0
    zf.writestr(info, msg)
    pass


if __name__ == "__main__":
    zipfile_writestr_zipinfo()