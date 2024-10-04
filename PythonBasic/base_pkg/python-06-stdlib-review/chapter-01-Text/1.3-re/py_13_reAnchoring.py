"""
table: regular expression Anchoring codes

+--------+------------------------------------------------------+
| code   | meaning                                              |
+========+======================================================+
| ^      | Start of string, or line                             |
+--------+------------------------------------------------------+
| $      | End of string, or line                               |
+--------+------------------------------------------------------+
| \A     | Start of string                                      |
+--------+------------------------------------------------------+
| \Z     | End of string                                        |
+--------+------------------------------------------------------+
| \b     | Empty string at the beginning or end of a word       |
+--------+------------------------------------------------------+
| \B     | Empty string NOT at the beginning or end of a word   |
+--------+------------------------------------------------------+

"""

from py_09_rePatterns import test_patterns


if __name__ == "__main__":
    test_patterns(
        [
            (r'^\w+', 'word at start of string'),
            (r'\A\w+', 'word at start of string'),
            (r'\w+\S*$', 'word near end of string'),
            (r'\w+\S*\Z', 'word near end of string'),
            (r'\w*t\w*', 'word containing t'),
            (r'\bt\w+', 't at start of word'),
            (r'\w+t\b', 't at end of word'),
            (r'\Bt\B', 't, not start or end of word')
        ],
        'This is some text -- with punctuation.'
    )