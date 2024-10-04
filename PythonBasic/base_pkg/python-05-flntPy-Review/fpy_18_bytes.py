# built-in bytes type
cafe = bytes('café', encoding='utf8')
print(cafe)
# each element of a bytes object is some integer in range(256)
print(cafe[0])
# slice of a bytes object is always bytes, even its length is 1
print(cafe[:1])

# bytearray type
cafe_arr = bytearray(cafe) # parameter is bytes object
print(cafe_arr)
print(cafe_arr[-1:]) # slice of a bytearray is still a bytearray object

# * Bytes are bits, just 8 at a time
# ? hex -> bytes -> string
h = '31 4B CE A9'
b = bytes.fromhex(h)
print(b)
# decode bytes object
print(b.decode('utf8'))
# ? hmm, it means string -> bytes -> hex process works too
# let's do it
bonjour = "Bonjour tout le monde"
# string -> bytes obj
b = bonjour.encode('utf8')
# or
b = bytes(bonjour, encoding='utf8')
print(b)
# bytes obj -> hex
h = b.hex()
print(h)