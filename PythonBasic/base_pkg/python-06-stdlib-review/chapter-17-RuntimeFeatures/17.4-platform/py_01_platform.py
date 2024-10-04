import platform

print('Normal :', platform.platform())
print('Aliased:', platform.platform(aliased=True))
print('Terse :', platform.platform(terse=True))

print()

print('uname:', platform.uname())
print('system :', platform.system())
print('node :', platform.node())
print('release :', platform.release())
print('version :', platform.version())
print('machine :', platform.machine())
print('processor:', platform.processor())

print()
print('interpreter:', platform.architecture())
print('/bin/ls :', platform.architecture('/bin/ls'))