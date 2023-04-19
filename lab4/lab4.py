with open('lab4/1.txt', 'r') as f:
    matrix = [[int(num) for num in line.split()] for line in f]

def ford_fulkerson(matrix, source, sink):
    n = len(matrix)
    flow = 0
    parent = [-1] * n
    while True:
        queue = [source]
        parent[source] = -2
        while queue:
            u = queue.pop(0)
            for v in range(n):
                if parent[v] == -1 and matrix[u][v] > 0:
                    parent[v] = u
                    queue.append(v)
                    if v == sink:
                        break
        if parent[sink] == -1:
            break
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, matrix[parent[s]][s])
            s = parent[s]
        flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            matrix[u][v] -= path_flow
            matrix[v][u] += path_flow
            v = u
        parent = [-1] * n
    return flow

source, sink = 0, 7
max_flow = ford_fulkerson(matrix, source, sink)
print(f"Максимальний потік: {max_flow}")