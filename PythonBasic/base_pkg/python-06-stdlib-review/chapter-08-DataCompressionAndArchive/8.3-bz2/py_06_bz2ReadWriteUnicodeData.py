import sys, bz2
sys.path.append('.')
from pkg.breaker import addBreaker

@addBreaker
def bz2_unicode():
    import os
    data = 'Character with an åccent.'

    with bz2.open('example.bz2', 'wt', encoding='utf8') as output:
        output.write(data)
    with bz2.open('example.bz2', 'rt', encoding='utf8') as _input:
        print('Full file: {}'.format(_input.read()))

    # move to the beginning of the accented character
    with bz2.open('example.bz2', 'rt', encoding='utf8') as _input:
        _input.seek(18)
        print('One character: {}'.format(_input.read(1)))
    # move to the middle of the accented character
    with bz2.open('example.bz2', 'rt', encoding='utf8') as _input:
        _input.seek(19)
        try:
            print(_input.read())
        except UnicodeDecodeError:
            print('ERROR: failed to decode')
    
    pass

if __name__ == "__main__":
    bz2_unicode()