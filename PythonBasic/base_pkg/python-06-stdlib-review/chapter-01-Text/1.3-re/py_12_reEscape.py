"""
table: regular expression Escape codes

+--------+---------------------------------------+
| code   | meaning                               |
+========+=======================================+
| \d     | A digit                               |
+--------+---------------------------------------+
| \D     | A non-digit                           |
+--------+---------------------------------------+
| \s     | Whitespace (tab, space, newline, etc.)|
+--------+---------------------------------------+
| \S     | Non-whitespace                        |
+--------+---------------------------------------+
| \w     | Alphanumeric                          |
+--------+---------------------------------------+
| \W     | Non-alphanumeric                      |
+--------+---------------------------------------+

"""

from py_09_rePatterns import test_patterns

if __name__ == "__main__":
    test_patterns(
        [
            (r'\d+', 'sequence of digits'),
            (r'\D+', 'sequence of non-digits'),
            (r'\s+', 'sequence of whitespace'),
            (r'\S+', 'sequence of non-whitespace'),
            (r'\w+', 'alphanumeric characters'),
            (r'\W+', 'non-alphanumeric')
        ],
        'A prime #1 example!'
    )