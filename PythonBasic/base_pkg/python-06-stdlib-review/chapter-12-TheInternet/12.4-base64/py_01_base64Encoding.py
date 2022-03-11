import base64, textwrap

# load this scource file and strip the header
with open(__file__, 'r', encoding='utf8') as inp:
    raw          = inp.read()
    initial_data = raw.split('#end_pymotw_header')[1]
print(raw)
print()
print(initial_data)
print()
# cette traduction est trop dure!

byte_string = initial_data.encode('utf8')
# ! The input must be a byte string
encode_data = base64.b64encode(byte_string)

num_initial = len(byte_string)

# there will never be more than 2 padding bytes
padding = 3 - (num_initial % 3)

print('{} bytes before encoding'.format(num_initial))
print('Expect {} padding bytes'.format(padding))
print('{} bytes after encoding\n'.format(len(encode_data)))
print(encode_data)