# * struct module deals with bytes, bytearray, memoryview objects
# it has basic functionalities
# packed bytes -> tuple consists of different types of variables
# or depack, tuple -> packed bytes 
import struct
import os

# ? wtf is this fmt...
# ! 结构体的格式：< 是小字节序，3s3s 是两个 3 字节序列，HH 是两个 16 位二进制整数。
# more details on page: https://docs.python.org/3/library/struct.html
"""

"""
fmt = '<3s3sHH' 
img_path = os.path.join(os.path.dirname(__file__), "static\\skyscale1.ico")
# read an image as binary
with open(img_path, 'rb') as fp:
    img = memoryview(fp.read())
print(img.shape)
header = img[:10]
print(bytes(header))
# struct.unpack(): bytes -> tuple
unpack = struct.unpack(fmt, header)
print(unpack)
del header
del img