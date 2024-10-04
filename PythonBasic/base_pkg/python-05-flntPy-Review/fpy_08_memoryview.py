import array

# signed short array
numbers = array.array('h', [-2, -1, 0, 1, 2])
# puts the array into a memoryview
memv = memoryview(numbers)
# length
print(len(memv))
# retrieve element
print(memv[0])
# changes memv into unsinged char
memv_oct = memv.cast('B')
print(memv_oct.tolist())
# unsigned char -> singed short
memv_oct[5] = 4
print(numbers)

