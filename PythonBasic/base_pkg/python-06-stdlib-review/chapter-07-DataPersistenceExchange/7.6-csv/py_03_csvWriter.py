import sys, csv
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def csv_writer():
    unicode_chars = '∫åç'
    csv_file      = 'testout.csv'
    with open(csv_file, 'wt', encoding='utf8') as f:
        # default quoting behavior
        writer = csv.writer(f)
        # other behavior: csv.QUOTE_NONNUMERIC, csv.QUOTE_ALL, csv.QUOTE_NONE, csv.QUOTE_MINIMAL
        writer = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        writer.writerow(('Title 1', 'Title 2', 'Title 3', 'Title 4'))
        for i in range(3):
            row = (
                i + 1,
                chr(ord('a') + i),
                '08/{:02d}/07'.format(i + 1),
                unicode_chars[i],
            )
            writer.writerow(row)
    print(open(csv_file, 'rt', encoding='utf8').read())

if __name__ == "__main__":
    csv_writer()