import sys, csv
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def csv_list_dialects():
    print(csv.list_dialects())
    pass

@addBreaker
def csv_dialect():
    csv.register_dialect('pipes', delimiter='|')
    file = r'chapter-07-DataPersistenceExchange\7.6-csv\testdata.pipes'
    with open(file, 'r') as f:
        reader = csv.reader(f, dialect='pipes')
        for row in reader:
            print(row)
    
    pass

if __name__ == "__main__":
    # by default, csv dialects: excel, excel-tab, unix
    csv_list_dialects()
    # user defined dialects are also welcomed by using `csv.register_dialect('pipes', delimiter='|')`
    csv_dialect()
    # auto detect dialect using `sniff()`. it returns a `Dialect` instance