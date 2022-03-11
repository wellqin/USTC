import cProfile as profile
import pstats
from py_01_profileRuntheProfiler import fib, fib_seq

# creates 5 sets of stats
for i in range(5):
    filename = 'profile_stats_{}.stats'.format(i)
    profile.run('print({}, fib_seq(20))'.format(i), filename)

# reads all 5 stats files into a single obj
stats = pstats.Stats('profile_stats_0.stats')
for i in range(1, 5):
    stats.add('profile_stats_{}.stats'.format(i))

# cleans up filename for the report
stats.strip_dirs()

# sorts the statistics by the cumulative time spent in the function
stats.sort_stats('cumulative')
stats.print_stats()