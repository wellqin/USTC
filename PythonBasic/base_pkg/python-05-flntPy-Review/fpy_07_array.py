import array
import random
floats = array.array('d', (random.random() for i in range(10**7)))
print(floats[-1])

with open("floats.bin", "wb") as f:
    floats.tofile(f)

floats2 = array.array("d")
with open('floats.bin', 'rb') as nf:
    floats2.fromfile(nf, 10**7)

print(floats2[-1])
assert floats == floats2