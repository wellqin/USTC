import heapq

def show_tree(tree: heapq, total_width=36, fill=' '):
    import math, io
    output   = io.StringIO()
    last_row = -1
    for i, n in enumerate(tree):
        if i:
            row = int(math.floor(math.log(i + 1, 2)))
        else:
            row = 0
        if row != last_row:
            output.write('\n')
        columns   = 2 ** row
        col_width = int(math.floor(total_width / columns)) 
        output.write(str(n).center(col_width, fill))
        last_row  = row
    print(output.getvalue())
    print('-' * total_width)
    print()