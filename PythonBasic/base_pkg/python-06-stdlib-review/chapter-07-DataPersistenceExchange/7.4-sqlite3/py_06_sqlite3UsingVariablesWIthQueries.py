import sys, sqlite3
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def sqlite3_argument_positional():
    db  = 'todo.db'
    pj  = 'pymotw'
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        sql_cmd = """
        select id, priority, details, status, deadline from task
        where project = ?
        """
        cursor.execute(sql_cmd, (pj,))
        for row in cursor.fetchall():
            _id, priority, details, status, deadline = row
            print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
                _id, priority, details, status, deadline
            ))
    pass

@addBreaker
def sqlite3_argument_named():
    db = 'todo.db'
    pj = 'pymotw'
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        query  = """
        select id, priority, details, status, deadline from task
        where project = :pj
        order by deadline, priority
        """
        cursor.execute(query, {'pj': pj})
        for row in cursor.fetchall():
            _id, priority, details, status, deadline = row
            print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
                _id, priority, details, status, deadline
            ))
    cursor.close()
    pass

@addBreaker
def sqlite3_argument_update():

    db   = 'todo.db'
    _id  = 2
    stat = 'done'
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        query  = """
        update task set status = :status where id = :id
        """
        cursor.execute(query, {'status': stat, 'id': _id})
    cursor.close()
    pass


if __name__ == "__main__":
    sqlite3_argument_positional()
    # name referencing is also available in sqlite3 .. nice 69
    sqlite3_argument_named()
    # name referencing can be used everywhere :^)
    sqlite3_argument_update()
    sqlite3_argument_named()