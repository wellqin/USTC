import re

text    = 'abbaaabbbbaaaaa'
pattern = 'ab'

def addBreaker(func):
    def inner(*args, **kwargs):
        Breaker = '\n{:-^50}'
        print(Breaker.format(''))
        func(*args, **kwargs)
    return inner

# multiple matches using re.findall()
@addBreaker
def re_findall():
    for match in re.findall(pattern, text):
        print('Found {!r}'.format(match))

# using re.finditer()
@addBreaker
def re_finditer():
    for match in re.finditer(pattern, text):
        s = match.start()
        e = match.end()
        print('Found {!r} at {:d}:{:d}'.format(text[s:e], s, e))

def main():
    # re.findall()
    re_findall()
    # re.finditer()
    re_finditer()

if __name__ == "__main__":
    main()