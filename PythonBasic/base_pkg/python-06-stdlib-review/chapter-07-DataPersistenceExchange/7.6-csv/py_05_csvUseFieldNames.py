import sys, csv
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def csv_dictreader():
    file = r'chapter-07-DataPersistenceExchange\7.6-csv\testdata.csv'
    with open(file, 'rt', encoding='utf8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row)
    pass

@addBreaker
def csv_dictwriter():
    fieldnames = ('Title 1', 'Title 2', 'Title 3', 'Title 4')
    csvfile = 'testout.csv'
    # headers = {
    #     n: n
    #     for n in fieldnames
    # }
    unicode_chars = '∫åç'
    with open(csvfile, 'wt', encoding='utf8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(3):
            writer.writerow({
                'Title 1': i + 1,
                'Title 2': chr(ord('a') + i),
                'Title 3': '08/{:02d}/07'.format(i + 1),
                'Title 4': unicode_chars[i],
            })
    print(open(csvfile, 'rt', encoding='utf8').read())
    pass

if __name__ == "__main__":
    # by default, csv.writer() vs csv.reader()
    # also, csv.DictWriter() vs csv.DictReader()
    csv_dictreader()
    csv_dictwriter()