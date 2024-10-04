import sys, sqlite3
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def sqlite3_load_csv():
    pass


if __name__ == "__main__":
    sqlite3_load_csv()