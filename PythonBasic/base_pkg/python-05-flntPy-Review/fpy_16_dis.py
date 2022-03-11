import dis
dis.dis('heapq.nlargest(d, 3)')

co = compile('heapq.nlargest(d, 3)', '<none>', 'eval')
# co.co_code.encode('hex')
print(co.co_names)
print(co.co_consts)