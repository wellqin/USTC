"""
? why, just why?
In many cases, it it useful to match a part of a pattern only if some other part will also match.

**look ahead**
- look ahead assertion, syntax (?=pattern) says that the pattern
- negative look ahead assertion, syntax (?!pattern) says the pattern does not match the text following the current point.

**look behind**
- negative look behind assertion, syntax (?<!pattern)
- positive look behind assertion, syntax (?<=pattern)
"""

import re, os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

@addBreaker
def re_look_ahead():
    address = re.compile(
        r'''
        # A name is made up of letters, and may include "."
        # for title abbreviations and middle initials.
        ((?P<name>
        ([\w.,]+\s+)*[\w.,]+
        )
        \s+
        ) # ! The name is no longer optional.
        # ! LOOKAHEAD
        # Email addresses are wrapped in angle brackets, but only
        # if both are present or neither is.
        (?= (<.*>$) # Remainder wrapped in angle brackets
        |
        ([^<].*[^>]$) # Remainder *not* wrapped in angle brackets
        )
        <? # Optional opening angle bracket
        # The address itself: username@domain.tld
        (?P<email>
        [\w\d.+-]+ # Username
        @
        ([\w\d.]+\.)+ # Domain name prefix
        (com|org|edu) # Limit the allowed top-level domains.
        )
        >? # Optional closing angle bracket
        ''',
        re.VERBOSE)
        
    candidates = [
        u'First Last <first.last@example.com>',
        u'No Brackets first.last@example.com',
        u'Open Bracket <first.last@example.com',
        u'Close Bracket first.last@example.com>',
    ]
    
    for candidate in candidates:
        print('Candidate:', candidate)
        match = address.search(candidate)
        if match:
            print(' Name :', match.groupdict()['name'])
            print(' Email:', match.groupdict()['email'])
        else:
            print(' No match')

@addBreaker
def re_negative_look_ahead():
    address = re.compile(
        r'''
        ^
        # An address: username@domain.tld
        # Ignore noreply addresses.
        (?!noreply@.*$)
        [\w\d.+-]+ # Username
        @
        ([\w\d.]+\.)+ # Domain name prefix
        (com|org|edu) # Limit the allowed top-level domains.
        $
        ''',
        re.VERBOSE)

    candidates = [
        u'first.last@example.com',
        u'noreply@example.com',
    ]

    for candidate in candidates:
        print('Candidate:', candidate)
        match = address.search(candidate)
        if match:
            print(' Match:', candidate[match.start():match.end()])
        else:
            print(' No match')

@addBreaker
def re_negative_look_behind():
    address = re.compile(
        r'''
        ^
        # An address: username@domain.tld
        [\w\d.+-]+ # Username
        # Ignore noreply addresses.
        (?<!noreply)
        @
        ([\w\d.]+\.)+ # Domain name prefix
        (com|org|edu) # Limit the allowed top-level domains.
        $
        ''',
        re.VERBOSE)

    candidates = [
        u'first.last@example.com',
        u'noreply@example.com',
    ]

    for candidate in candidates:
        print('Candidate:', candidate)
        match = address.search(candidate)
        if match:
            print(' Match:', candidate[match.start():match.end()])
        else:
            print(' No match')

@addBreaker
def re_positive_look_behind():
    twitter = re.compile(
        r'''
        # A twitter handle: @username
        (?<=@)
        ([\w\d_]+) # Username
        ''',
        re.VERBOSE)

    text = '''This text includes two Twitter handles.
    One for @ThePSF, and one for the author, @doughellmann.
    '''

    print(text)
    for match in twitter.findall(text):
        print('Handle:', match)

if __name__ == "__main__":
    # look ahead assertion
    re_look_ahead()
    # negative look ahead assertion
    re_negative_look_ahead()
    # negative look behind assertion
    re_negative_look_behind()
    # positive look behind assertion
    re_positive_look_behind()
