import sys, shelve
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def shelve_withoutWriteback():
    with shelve.open('test_shelf.db') as s:
        print(s['key1'])
        s['key1']['new_value'] = 'this was not here before'
    
    with shelve.open('test_shelf.db', writeback=True) as s:
        print(s['key1'])
    
    pass

if __name__ == "__main__":
    # ! writeback flag causes the shelf to remember all of the objects
    # ! retrieved from the database using an in-memory cache.
    shelve_withoutWriteback()