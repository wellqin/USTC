import sys, sqlite3, os
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def sqlite3_createdb():
    db    = 'todo.db'
    isnew = not os.path.exists(db)
    with sqlite3.connect(db) as conn:
        # ! BUT for cursor obj, need add contextmanager by yourself thou
        if isnew:
            print('need to create a schema')
        else:
            print('data exists: assume schema does, too.')

    try:
        conn.close()
    except:
        pass

@addBreaker
def sqlite3_create_schema():
    db        = 'todo.db'
    schema_fn = r'chapter-07-DataPersistenceExchange\7.4-sqlite3\todo_schema.sql'
    isnew     = not os.path.exists(db)

    with sqlite3.connect(db) as conn:
        if isnew:
            print('Creating schema')
            # ! Ohh, 69 nice
            with open(schema_fn, 'rt') as f:
                schema = f.read()
            conn.executescript(schema)
            print('Inserting initial data')
            conn.executescript("""
            insert into project (name, description, deadline)
            values ('pymotw', 'Python Module of the Week', '2016-11-01');

            insert into task (details, status, deadline, project)
            values ('write about select', 'done', '2016-04-25', 'pymotw');
            
            insert into task (details, status, deadline, project)
            values ('write about random', 'waiting', '2016-08-22', 'pymotw');
            
            insert into task (details, status, deadline, project)
            values ('write about sqlite3', 'active', '2017-07-31', 'pymotw');
            """)
        else:
            print('data exists: assume schema does, too.')


if __name__ == "__main__":
    # sqlite3_createdb()
    sqlite3_create_schema()
