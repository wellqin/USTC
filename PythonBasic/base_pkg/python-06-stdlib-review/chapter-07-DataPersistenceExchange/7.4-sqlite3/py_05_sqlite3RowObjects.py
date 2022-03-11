import sys, sqlite3
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def sqlite3_row_factory():
    db = 'todo.db'
    with sqlite3.connect(db) as conn:
        # ! change the row factory to use row
        conn.row_factory = sqlite3.Row

        cursor  = conn.cursor()
        sql_cmd = """
        select name, description, deadline from project
        where name = 'pymotw'
        """
        cursor.execute(sql_cmd)
        name, description, deadline = cursor.fetchone()
        print('Project details for {} ({})\n due {}'.format(
            description, name, deadline
        ))
        sql_cmd  = """
        select id, priority, status, deadline, details from task
        where project = 'pymotw' order by deadline
        """
        cursor.execute(sql_cmd)
        print('\nNext 5 tasks:')
        for row in cursor.fetchmany(5):
            print('{:2d} [{:d}] {:<25} [{:<8}] ({})'.format(
                row['id'], row['priority'], row['details'], row['status'], row['deadline']
            ))
    pass

if __name__ == "__main__":
    # ! "rows" from database are tuples
    # ! it means using tuples as variables' container to CRUD a database
    # aha, it merely means a similar concept, index referencing and name referencing
    sqlite3_row_factory()