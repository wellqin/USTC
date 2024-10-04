import re, os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from py_09_rePatterns import test_patterns, test_patterns_updated_ver
from pkg.breaker import addBreaker

@addBreaker
def re_groups_match():
    text = 'This is some text -- with punctuation.'
    print(text)
    print()
    
    patterns = [
        (r'^(\w+)', 'word at start of string'),
        (r'(\w+)\S*$', 'word at end, with optional punctuation'),
        (r'(\bt\w+)\W+(\w+)', 'word starting with t, another word'),
        (r'(\w+t)\b', 'word ending with t'),
    ]

    for pattern, desc in patterns:
        regex = re.compile(pattern)
        match = regex.search(text)
        print("'{}' ({})\n".format(pattern, desc))
        print('  ', match.groups())
        print()

@addBreaker
def re_group_individual():
    text = 'This is some text -- with punctuation.'
    print('Input text            :', text)
    
    # word starting with 't' then another word
    regex = re.compile(r'(\bt\w+)\W+(\w+)')
    print('Pattern               :', regex.pattern)

    match = regex.search(text)
    print('Entire match          :', match.group(0))
    print('Word starting with "t":', match.group(0))
    print('Word after "t" word   :', match.group(0))
    
@addBreaker
def re_groups_named():
    text = 'This is some text -- with punctuation.'
    print(text)
    print()
    # default is index reference
    # using names to refer to groups makes it easier to modify the pattern over time
    # name reference syntax(?P<name>pattern)
    patterns = [
        r'^(?P<first_word>\w+)',
        r'(?P<last_word>\w+)\S*$',
        r'(?P<t_word>\bt\w+)\W+(?P<other_word>\w+)',
        r'(?P<ends_with_t>\w+t)\b',
    ]

    for pattern in patterns:
        regex = re.compile(pattern)
        match = regex.search(text)
        print("'{}'".format(pattern))
        print('  ', match.groups())
        print('  ', match.groupdict())
        print()


if __name__ == "__main__":
    test_patterns(
        [
            ('a(ab)', 'a followed by literal ab'),
            ('a(a*b*)', 'a followed by 0-n a and 0-n b'),
            ('a(ab)*', 'a followed by 0-n ab'),
            ('a(ab)+', 'a followed by 1-n ab'),
        ],
        'abbaaabbbbaaaaa'
    )
    # match.groups()
    re_groups_match()
    # index reference: match.group(index)
    re_group_individual()
    # name reference: match.groupdict()
    re_groups_named()
    # match.groupdict()
    test_patterns_updated_ver(
        [(r'a((a*)(b*))', 'a followed by optional 0-n a and 0-n b')],
        'abbaabbba'
    )
    # match.groups() is useful for specifying alternative patterns. using pipe symbol(|)
    test_patterns_updated_ver(
        [
            (r'a((a+)|(b+))', 'a then seq. of a or seq. of b'),
            (r'a((a|b)+)', 'a then seq. of [ab]'),
        ],
        'abbaabbba'
    )
    # non-capturing group: a group containing a subpattern is also useful 
    # in cases where the string matching the subpattern
    # is not part of what should be extracted from the full text
    # To create a non-capturing group, use the syntax (?:pattern)
    test_patterns_updated_ver(
        [
            (r'a((a+)|(b+))', 'capturing form'),
            (r'a((?:a+)|(?:b+))', 'non-capturing'),
        ],
        'abbaabbba'
    )