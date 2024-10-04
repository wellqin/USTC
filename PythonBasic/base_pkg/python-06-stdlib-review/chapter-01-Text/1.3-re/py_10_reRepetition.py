# import sys, os
# sys.path.append(os.path.dirname(os.path.dirname(__file__)))
# from pkg.breaker import addBreaker
from py_09_rePatterns import test_patterns, text

if __name__ == "__main__":
    # default behavior is greedy
    test_patterns(
        [('ab*', 'a followed by zero or more b'),
        ('ab+', 'a followed by one or more b'),
        ('ab?', 'a followed by zero or one b'),
        ('ab{3}', 'a followed by three b'),
        ('ab{2, 3}', 'a followed by two or three b')],
        text='abbaabbba'
    )
    # non-greedy via turning off by following the repetition instruction with ?
    test_patterns(
        [('ab*?', 'a followed by zero or more b'),
        ('ab+?', 'a followed by one or more b'),
        ('ab??', 'a followed by zero or one b'),
        ('ab{3}?', 'a followed by three b'),
        ('ab{2, 3}?', 'a followed by two or three b')],
        text='abbaabbba'
    )
