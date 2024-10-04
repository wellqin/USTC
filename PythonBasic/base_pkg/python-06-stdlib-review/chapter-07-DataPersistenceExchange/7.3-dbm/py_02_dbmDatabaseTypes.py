import sys, dbm
sys.path.append('.')
from pkg.breaker import addBreaker

DB = './example.db'

@addBreaker
def dbm_new():
    with dbm.open(DB, 'n') as db:
        db['key']    = 'value'
        db['today']  = 'Sunday'
        db['author'] = 'Doug'
    pass


@addBreaker
def dbm_whichdb():
    # whichdb() reports the type of database that was created
    print(dbm.whichdb(DB))

    
    
    pass


if __name__ == "__main__":
    # open() functions takes flags to control how the database file is managed
    # flags
    # 'c': create a new database when necessary
    # 'n': always creates a new database, overwriting an existing file
    # 'r': read-only 
    # 'w': write-only
    dbm_new()
    dbm_whichdb()