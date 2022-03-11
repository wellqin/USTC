import sys, csv
sys.path.append('.')
from pkg.breaker import addBreaker

csv_data = r'chapter-07-DataPersistenceExchange\7.6-csv\testdata.csv'

@addBreaker
def csv_reading():
    with open(csv_data, 'rt', encoding='utf8') as f:
        # The parser handles line breaks embedded within strings in a row
        reader = csv.reader(f)
        for row in reader:
            print(row)
    pass

if __name__ == "__main__":
    csv_reading()