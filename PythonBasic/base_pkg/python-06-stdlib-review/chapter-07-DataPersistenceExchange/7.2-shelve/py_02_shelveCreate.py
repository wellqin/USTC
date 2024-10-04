import sys, shelve, dbm
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def shelve_create():
    with shelve.open('test_shelf.db') as s:
        s['key1'] = {
            'int':10,
            'float':9.5,
            'string': 'Sample Data',
        }

@addBreaker
def shelve_existing():
    with shelve.open('test_shelf.db') as s:
        existing = s['key1']    
    print(existing)


@addBreaker
def shelve_readonly():
    with shelve.open('test_shelf.db', flag='r') as s:
        print('Existing:', s['key1'])
        try:
            s['key1'] = 'new value'
        except dbm.error as err:
            print('ERROR: {}'.format(err))


if __name__ == "__main__":
    shelve_create()
    # shelf existing?
    shelve_existing()
    # modifying the database while it is opened as read-only source,
    # an access error exception is generated
    shelve_readonly()