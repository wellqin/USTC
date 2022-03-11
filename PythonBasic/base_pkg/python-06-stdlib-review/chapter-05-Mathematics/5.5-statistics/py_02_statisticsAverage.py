import sys, statistics
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def statistics_mean():
    data = [1, 2, 2, 5, 10, 12]
    print('data           :', data)
    print('mean           : {:0.2f}'.format(statistics.mean(data)))
    print('mode           : {:0.2f}'.format(statistics.mode(data)))
    print('median         : {:0.2f}'.format(statistics.median(data)))
    print('median_low     : {:0.2f}'.format(statistics.median_low(data)))
    print('median_high    : {:0.2f}'.format(statistics.median_high(data)))
    data = [10, 20, 30, 40]
    print('data           :', data)
    print('median_grouped :')
    print('1: {:0.2f}'.format(statistics.median_grouped(data, interval=1)))
    print('2: {:0.2f}'.format(statistics.median_grouped(data, interval=2)))
    print('3: {:0.2f}'.format(statistics.median_grouped(data, interval=3)))


if __name__ == "__main__":
    # yeah, mean, median, mode three brothers
    statistics_mean()