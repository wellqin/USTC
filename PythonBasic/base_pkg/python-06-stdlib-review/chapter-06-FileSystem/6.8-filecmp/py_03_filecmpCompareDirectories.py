import sys, filecmp
sys.path.append('.')
from pkg.breaker import addBreaker
import os

@addBreaker
def filecmp_dircmp_report():
    os.chdir(os.path.dirname(__file__))
    dc = filecmp.dircmp(
        'example/dir1',
        'example/dir2'
    )
    dc.report()
    pass

@addBreaker
def filecmp_dircmp_report_full_closure():
    dc = filecmp.dircmp(
        'example/dir1',
        'example/dir2',
    )
    dc.report_full_closure()
    pass

if __name__ == "__main__":
    # report() vs report_partial_closure() vs vs report_full_closure()
    # details: simple, more, most
    filecmp_dircmp_report()
    filecmp_dircmp_report_full_closure()