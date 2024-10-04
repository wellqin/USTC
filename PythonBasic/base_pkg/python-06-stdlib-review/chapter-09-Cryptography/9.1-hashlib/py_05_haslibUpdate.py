import sys, hashlib
sys.path.append('.')
from pkg.breaker import addBreaker
from hashlib_data import lorem

@addBreaker
def hashlib_update():
    def chunksize(size, text):
        start = 0
        while start < len(text):
            chunk = text[start:start+size]
            yield chunk
            start += size
        return
    # reads all at once
    h = hashlib.md5()
    h.update(lorem.encode('utf8'))
    all_at_once = h.hexdigest()
    # reads line by line
    h = hashlib.md5()
    for chunk in chunksize(64, lorem.encode('utf8')):
        h.update(chunk)
    line_by_line = h.hexdigest()
    print('all at once  :', all_at_once)
    print('line by line :', line_by_line)
    print('same         :', (all_at_once == line_by_line))
    
    pass

if __name__ == "__main__":
    hashlib_update()