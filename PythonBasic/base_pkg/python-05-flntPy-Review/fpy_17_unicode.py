# example 01, using unicode to display 'hello world'
hellworld = dict(
    H = '\u0048', # \u0048 is charactor H's code number in unicode charactor set
    e = '\u0065',
    l = '\u006c',
    o = '\u006f',
    space = '\u0020',
    w = '\u0077',
    r = '\u0072',
    d = '\u0064',)

for word in "Hello world":
    print("{0!r}".format(hellworld.get(word, 'N/A')))

print('\u0048\u0065\u006c\u006c\u006f\u0020\u0077\u006f\u0072\u006c\u0064')

# encode: codenumber -> bytecode 
print(u'\u0048'.encode('utf8'))
print(u'\u0048'.encode('utf16'))
# decode: bytecode -> codenumber
print(b'\u0048'.decode('utf8'))

# encode: string -> bytecode
s = 'café'
print(len(s))
b = s.encode('utf8')
print(b)
print(len(b))
# decode: bytecode -> string
print(b.decode('utf8'))

# example 04, chinese
nihao = "你"
# encode
byts = nihao.encode('utf8')
print("{0} encoding result is: {1}".format(nihao, byts))
# decode
print(byts.decode('utf8'))