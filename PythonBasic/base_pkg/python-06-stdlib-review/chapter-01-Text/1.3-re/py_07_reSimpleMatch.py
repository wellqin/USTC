import re

def addBreaker(func):
    def inner(*args, **kwargs):
        Breaker = '\n{:-^50}'
        print(Breaker.format(''))
        func(*args, **kwargs)
    return inner

# finding patterns in text by re.search()
@addBreaker
def find_pattern_in_text(p, t):
    # w/o precompiling pattern
    match = re.search(pattern, text)
    s     = match.start()
    e     = match.end()
    print('Found "{}"\nin "{}"\nfrom {} to {} ("{}")'.format(match.re.pattern, 
                                                            match.string, 
                                                            s, 
                                                            e, 
                                                            text[s:e]))

# precompiling by re.compile()
@addBreaker
def find_pattern_compiled():
    regexes = [re.compile(p) for p in ['this', 'that']]
    text    = 'Does this text match the pattern?'
    print('Text: {!r}\n'.format(text))
    for regex in regexes:
        print('Seeking "{}" ->'.format(regex.pattern), end=' ')
        if regex.search(text):
            print('match!')
        else:
            print('no match')

if __name__ == "__main__":
    # finding patterns in text without precompiling
    pattern = r'this'
    text    = 'Does this text match the pattern?'
    find_pattern_in_text(p=pattern, t=text)
    # precompiling
    find_pattern_compiled()
