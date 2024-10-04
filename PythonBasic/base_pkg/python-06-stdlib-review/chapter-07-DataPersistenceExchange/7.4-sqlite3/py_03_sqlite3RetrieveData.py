import sys, sqlite3
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def sqlite3_select_tasks():
    db  = 'todo.db'
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        cursor.execute("""
        select id, priority, details, status, deadline from task
        where project = 'pymotw'
        """)

        for row in cursor.fetchall():
            task_id, priority, details, status, deadline = row
            print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
                task_id, priority, details, status, deadline
            ))
        cursor.close()

@addBreaker
def sqlite3_select_variabtions():
    db = 'todo.db'
    with sqlite3.connect(db) as conn:
        cursor  = conn.cursor()
        sql_cmd = """
        select name, description, deadline from project
        where name = 'pymotw'
        """
        cursor.execute(sql_cmd)
        print('\nfetchone():')
        name, description, deadline = cursor.fetchone()
        print('Project details for {} ({})\n due {}'.format(description, name, deadline))
        sql_cmd = """
        select id, priority, details, status, deadline from task
        where project = 'pymotw' order by deadline
        """
        n = 5
        print('\nNext {} tasks:'.format(n))
        cursor.execute(sql_cmd)
        for row in cursor.fetchmany(n):
            _id, priority, details, status, deadline = row
            print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(_id, priority, description, status, deadline))
        cursor.close()

if __name__ == "__main__":
    # nice 69, scyn. fetchall()
    sqlite3_select_tasks()
    # fetchmany()
    sqlite3_select_variabtions()
    # fetchone()
