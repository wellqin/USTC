import sys, dbm
sys.path.append('.')
from pkg.breaker import addBreaker
from py_02_dbmDatabaseTypes import DB

@addBreaker
def dbm_existing():
    with dbm.open(DB, 'r') as db:
        print('keys()   :', db.keys())
        for k in db.keys():
            print('iterating:', k, db[k])
        print('db["author"] =', db['author'])

    pass


if __name__ == "__main__":
    dbm_existing()