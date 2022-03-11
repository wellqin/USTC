import sys, sqlite3
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def sqlite3_cursor_description():
    db = 'todo.db'
    with sqlite3.connect(db) as conn:
        cursor  = conn.cursor()
        sql_cmd = """
        select * from task where project = 'pymotw'
        """
        cursor.execute(sql_cmd)
        print('cursor.description:')
        for colinfo in cursor.description:
            print(colinfo)
    pass

if __name__ == "__main__":
    # DB-API 2.0 spec. says that after execute() has been called,
    # the Cursor should set its description attribute to hold informatino
    # about the data that will be returned by the fetch methods.
    sqlite3_cursor_description()