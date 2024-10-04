import sys, statistics
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def statistics_variance():
    import subprocess
    def get_Line_lengths():
        # ! works ONLY on unix-like system tho  ..
        cmd = 'wc -l ../[a-z]*/*.py'
        out = subprocess.check_output(cmd, shell=True).decode('utf8')
        for line in out.splitlines():
            parts = line.split()
            if parts[1].strip().lower() == 'total':
                break
            nlines = int(parts[0].strip())
            if not nlines:
                continue
            yield (nlines, parts[1].strip())
    
    data    = list(get_Line_lengths())
    lengths = [d[0] for d in data]
    sample  = lengths[::2]

    print('Basic statistics:')
    print(' count       : {:3d}'.format(len(lengths)))
    print(' min         : {:6.2f}'.format(min(lengths)))
    print(' max         : {:6.2f}'.format(max(lengths)))
    print(' mean        : {:6.2f}'.format(statistics.mean(lengths)))

    print('\nPopulation variance:')
    print(' pstdev      : {:6.2f}'.format(statistics.pstdev(lengths)))
    print(' pvariance   : {:6.2f}'.format(statistics.pvariance(lengths)))

    print('\nEstimated variance for sample:')
    print(' count       : {:3d}'.format(len(sample)))
    print(' stdev       : {:6.2f}'.format(statistics.stdev(sample)))
    print(' variance    : {:6.2f}'.format(statistics.variance(sample)))


if __name__ == "__main__":
    # std, variance. hmm
    statistics_variance()