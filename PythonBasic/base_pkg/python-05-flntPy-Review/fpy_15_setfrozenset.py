# why set? why frozenset?

# example 01, set
l = ['hello', 'world', 'spam', 'spamm', 'eggs', 'spam']
s = set(l)
print(s)

# example 02, frozenset
fs = frozenset(l)
print(fs)

# __eq__, just like deque
assert s == fs

# setcomp
import unicodedata
set_names = {chr(i) for i in range(32, 256) if 'SIGN' in unicodedata.name(chr(i), '')}
print(set_names)