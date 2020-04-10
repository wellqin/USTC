Graph = {'A': ['B', 'C', 'D'], 'B': ['A', 'E'], 'C': ['A', 'F'], 'D': ['A', 'G', 'H'], 'E': ['B', 'F'], 'F': ['E', 'C'],
         'G': ['D', 'H', 'I'], 'H': ['G', 'D'], 'I': ['G']}


def DFS(G, start):
    stack, res, visited = [start], [], set()
    while stack:
        node = stack.pop(0)
        if node in visited:
            continue
        else:
            res.append(node)
            visited.add(node)
            for i in G[node]:
                if i not in visited:
                    stack.append(i)
    return res


print(DFS(Graph, 'A'))
