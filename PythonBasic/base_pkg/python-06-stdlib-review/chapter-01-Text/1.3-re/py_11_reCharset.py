from py_09_rePatterns import test_patterns

if __name__ == "__main__":
    test_patterns(
        [
            ('[ab]', 'either a or b'),
            ('a[ab]+', 'a followed by 1 or more a or b'),
            ('a[ab]+?', 'a followed by 1 or more a or b, not greedy'),
        ],
        'abbaabbba'
    )
    # exclude using ^. [^ ]
    test_patterns(
        [
            ('[^-. ]+', 'sequences without -, ., or space'),
        ],
        'This is some text -- with punctuation.'
    )
    # ranges
    test_patterns(
        [
            ('[a-z]+', 'sequences of lowercase letters'),
            ('[A-Z]+', 'sequences of uppercase letters'),
            ('[a-zA-Z]+', 'sequences of lower- or uppercase letters'),
            ('[A-Z][a-z]+', 'one uppercase followed by lowercase'),
        ],
        'This is some text -- with punctuation.'
    )
    # dot
    test_patterns(
        [('a.', 'a followed by any one character'),
        ('b.', 'b followed by any one character'),
        ('a.*b', 'a followed by anything, ending in b'),
        ('a.*?b', 'a followed by anything, ending in b')],
        'abbaabbba'
    )
