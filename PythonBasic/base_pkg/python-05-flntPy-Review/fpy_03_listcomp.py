# list comprehension
symbols = '$¢£¥€¤'
codes = [ord(symbol) for symbol in symbols]
print(codes)

# or map
codes = list(map(ord, symbols))
print(codes)

# implement filtering
codes = [ord(symbol) for symbol in symbols if ord(symbol) > 127]
print(codes)
# or
codes = list(filter(lambda x: x > 127, map(ord, symbols)))
print(codes)