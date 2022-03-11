import re

text    = 'abbaaabbbbaaaaa'
pattern = 'ab'

def addBreaker(func):
    def inner(*args, **kwargs):
        Breaker = '\n{:-^50}'
        print(Breaker.format(''))
        func(*args, **kwargs)
    return inner

@addBreaker
def test_patterns(patterns, text):
    for pattern, desc in patterns:
        print("'{}' ({})\n".format(pattern, desc))
        print("  '{}'".format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            substr = text[s:e]
            n_backslashes = text[s:e].count('\\')
            prefix = '.' * (s + n_backslashes)
            print("  {}'{}'".format(prefix, substr))
        print()
    return

@addBreaker
def test_patterns_updated_ver(patterns, text):
    """Given source text and a list of patterns, look for
    matches for each pattern within the text and print them to stdout
    """
    # look for each pattern in the text and print the results
    for pattern, desc in patterns:
        print('{!r} ({})\n'.format(pattern, desc))
        print('  {!r}'.format(text))
        for match in re.finditer(pattern, text):
            s = match.start()
            e = match.end()
            prefix = ' ' * (s)
            print('  {}{!r}{} '.format(prefix, text[s:e], ' '*(len(text) - e)), end=' ')
            print(match.groups())
            if match.groupdict():
                print('{}{}'.format(' '*(len(text) - s), match.groupdict()))
        print()
    return
    
if __name__ == "__main__":
    test_patterns(patterns=[('ab', "'a' followed by 'b'")], text=text)
    test_patterns_updated_ver(patterns=[(r'a((a*)(b*))', "'a' followed by 0-n 'a' and 0-n 'b'")], text='abbaabbba')