"""
re.match() vs re.search()

? what is difference between re.match() and re.search()?
:: re.match()  -- re.match is anchored at the beginning of the string. That has nothing to do with newlines, so it is not the same as using ^ in the pattern.
:: re.search() -- re.search searches the entire string

? when to use re.mathc(), and re.search()
:: So if you need to match at the beginning of the string, or to match the entire string use match. It is faster. Otherwise use search.


"""
import re, sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

text    = 'This is some text -- with punctuation.'
pattern = 'is'

@addBreaker
def re_Match_vs_Search():
    print('Text   :', text)
    print('Pattern:', pattern)

    m = re.match(pattern, text)
    s = re.search(pattern, text)
    print('Match  :', m)
    print('Search :', s)

@addBreaker
def re_Fullmatch():
    print('Text      :', text)
    print('Pattern   :', pattern)

    m = re.fullmatch(pattern, text)
    s = re.search(pattern, text)
    print('Full match:', m)
    print('Search    :', s)

@addBreaker
def re_Search_substring():
    pattern = re.compile(r'\b\w*is\w*\b')
    print('Text:', text)
    print()

    pos = 0
    while True:
        match = pattern.search(text, pos)
        if not match:
            break
        s = match.start()
        e = match.end()
        print('  {:>2d} : {:>2d} = "{}"'.format(s, e - 1, text[s:e]))
        # Move forward in text for the next search.
        pos = e

if __name__ == "__main__":
    re_Match_vs_Search()
    re_Fullmatch()
    re_Search_substring()