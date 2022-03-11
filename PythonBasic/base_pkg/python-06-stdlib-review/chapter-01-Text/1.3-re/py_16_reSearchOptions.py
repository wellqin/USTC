"""
Table of Regular Expression Flag Abbreviations

+-------------+---------------------------------------+
| Flag        | Abbreviation                          |
+=============+=======================================+
| ASCII       | a                                     |
+-------------+---------------------------------------+
| IGNORECASE  | i                                     |
+-------------+---------------------------------------+
| MULTILINE   | m                                     |
+-------------+---------------------------------------+
| DOTALL      | s                                     |
+-------------+---------------------------------------+
| VERBOSE     | x                                     |
+-------------+---------------------------------------+

"""

import re, os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from pkg.breaker import addBreaker

@addBreaker
def re_flags_ignorecase():
    text         = 'This is some text -- with punctuation.'
    pattern      = r'\bT\w+'
    with_case    = re.compile(pattern)
    without_case = re.compile(pattern, re.IGNORECASE)

    print('Text:\n {!r}'.format(text))
    print('Pattern:\n {}'.format(pattern))
    print('Case-sensitive:')
    for match in with_case.findall(text):
        print(' {!r}'.format(match))
    print('Case-insensitive:')
    for match in without_case.findall(text):
        print(' {!r}'.format(match))

@addBreaker
def re_flags_multiline():
    text        = 'This is some text -- with punctuation. \nA second line.'
    pattern     = r'(^\w+)|(\w+\S*$)'
    single_line = re.compile(pattern)
    multiline   = re.compile(pattern, re.MULTILINE)

    print('Text:\n {!r}'.format(text))
    print('Pattern:\n {}'.format(pattern))
    print('Single Line :')
    for match in single_line.findall(text):
        print(' {!r}'.format(match))
    print('Multline :')
    for match in multiline.findall(text):
        print(' {!r}'.format(match))

@addBreaker
def re_flags_dotall():
    text        = 'This is some text -- with punctuation. \nA second line.'
    pattern     = r'.+'
    no_newlines = re.compile(pattern)
    dotall      = re.compile(pattern, re.DOTALL)

    print('Text:\n {!r}'.format(text))
    print('Pattern:\n {}'.format(pattern))
    print('No newlines :')
    for match in no_newlines.findall(text):
        print(' {!r}'.format(match))
    print('Dotall :')
    for match in dotall.findall(text):
        print(' {!r}'.format(match))

@addBreaker
def re_flags_ascii():
    text            = u'Français łzoty Österreich'
    pattern         = r'\w+'
    ascii_pattern   = re.compile(pattern, re.ASCII)
    unicode_pattern = re.compile(pattern)
    print('Text    :', text)
    print('Pattern :', pattern)
    print('ASCII   :', list(ascii_pattern.findall(text)))
    print('Unicode :', list(unicode_pattern.findall(text)))

@addBreaker
def re_email_compact():
    address     = re.compile(r'[\w\d.+-]+@([\w\d.]+\.)+(com|org|edu)')
    candidates  = [
        u'first.last@example.com',
        u'first.last+category@gmail.com',
        u'valid-address@mail.example.com',
        u'not-valid@example.foo',
    ]

    for candidate in candidates:
        match = address.search(candidate)
        print('{:<30} {}'.format(candidate, 'Matches' if match else 'No match'))
    return

@addBreaker
def re_email_verbose():
    address = re.compile(
        r'''
        [\w\d.+-]+      # username
        @
        ([\w\d.]+\.)+   # domain
        (com|org|edu)   # TODO: support more top-level domains
        ''',
        re.VERBOSE
    )
    candidates  = [
        u'first.last@example.com',
        u'first.last+category@gmail.com',
        u'valid-address@mail.example.com',
        u'not-valid@example.foo',
    ]
    for candidate in candidates:
        match = address.search(candidate)
        print('{:<30} {}'.format(candidate, 'Matches' if match else 'No match'))
    return

@addBreaker
def re_email_with_name():
    address = re.compile(
        r'''
        # A name is made up of letters, and may include "."
        # for title abbreviations and middle initials.
        ((?P<name>
        ([\w.,]+\s+)*[\w.,]+)
        \s*
        # Email addresses are wrapped in angle
        # brackets < >, but only if a name is
        # found, so keep the start bracket in this
        # group.
        <
        )? # The entire name is optional.
        # The address itself: username@domain.tld
        (?P<email>
        [\w\d.+-]+ # Username
        @
        ([\w\d.]+\.)+ # Domain name prefix
        (com|org|edu) # Limit the allowed top-level domains.
        )
        >? # Optional closing angle bracket.
        ''',
        re.VERBOSE
    )
    
    candidates = [
        u'first.last@example.com',
        u'first.last+category@gmail.com',
        u'valid-address@mail.example.com',
        u'not-valid@example.foo',
        u'First Last <first.last@example.com>',
        u'No Brackets first.last@example.com',
        u'First Last',
        u'First Middle Last <first.last@example.com>',
        u'First M. Last <first.last@example.com>',
        u'<first.last@example.com>',
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
def re_flags_embedded():
    text    = 'This is some text -- with punctuation.'
    # flag embedding syntax (?flag)pattern
    pattern = r'(?i)\bT\w+'
    regex   = re.compile(pattern)
    print('Text     :', text)
    print('Pattern  :', pattern)
    print('Matches  :', regex.findall(text))

if __name__ == "__main__":
    # search options: re.IGNORECASE
    re_flags_ignorecase()
    # search options: re.MULTILINE
    re_flags_multiline()
    # search options: re.DOTALL  opposite of multiline
    re_flags_dotall()
    # search options: re.ASCII
    re_flags_ascii()
    # compact vs verbose
    re_email_compact()
    re_email_verbose()
    # name referencing
    re_email_with_name()
    # embedding flags in pattern
    re_flags_embedded()