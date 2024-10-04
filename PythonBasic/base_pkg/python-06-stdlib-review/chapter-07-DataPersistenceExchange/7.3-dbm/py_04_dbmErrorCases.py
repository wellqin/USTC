import sys, dbm
sys.path.append('.')
from pkg.breaker import addBreaker

from py_02_dbmDatabaseTypes import DB

@addBreaker
def dbm_intkey():
    with dbm.open(DB, 'w') as db:
        try:
            db[1] = 'one'
        except TypeError as err:
            print(err)

@addBreaker
def dbm_intvalue():
    with dbm.open(DB, 'w') as db:
        try:
            db['one'] = 1
        except TypeError as err:
            print(err)


if __name__ == "__main__":
    # ! Why? 
    # * cuz `dbm` mapping accepts byte or string elements ONLY
    # assigns integer value as key
    dbm_intkey()
    # assigns int value as value
    dbm_intvalue()