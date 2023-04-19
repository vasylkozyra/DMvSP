import heapq

with open('lab1/1.txt', 'r') as f:
    matrix = [[int(num) for num in line.split()] for line in f]

n = len(matrix)
visited = set()
min_heap = []
start_vertex = 0
mst = []
total = 0

visited.add(start_vertex)

for j in range(n):
    if matrix[start_vertex][j] != 0:
        heapq.heappush(min_heap, (matrix[start_vertex][j], start_vertex, j))

while len(visited) < n:
    weight, u, v = heapq.heappop(min_heap)
    if v in visited:
        continue
    mst.append((u, v))
    total += weight
    visited.add(v)
    for j in range(n):
        if matrix[v][j] != 0 and j not in visited:
            heapq.heappush(min_heap, (matrix[v][j], v, j))

print('Мінімальне остовне дерево:')
for edge in mst:
    print(f'{edge[0]} - {edge[1]}')
print(f'Вага мінімального остовного дерева: {total}')