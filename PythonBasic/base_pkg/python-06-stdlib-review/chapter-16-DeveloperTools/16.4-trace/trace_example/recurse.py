def recurse(level):
    print('recurse({})'.format(level))
    if level:
        recurse(level - 1)
    
def not_called():
    print('this function is never called.')