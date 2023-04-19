import math

with open('test/1.txt', 'r') as f:
    matrix = [[int(num) for num in line.split()] for line in f.readlines()]

def dijkstra(graph, source, dest):
    n = len(graph)
    distances = [math.inf] * n
    visited = [False] * n
    distances[source] = 0
    if source == dest:
        return 0
    for i in range(n):
        min_dist = math.inf
        min_index = None
        for j in range(n):
            if not visited[j] and distances[j] < min_dist:
                min_dist = distances[j]
                min_index = j        
        for j in range(n):
            if graph[min_index][j] != 0 and not visited[j]:
                new_dist = distances[min_index] + graph[min_index][j]
                if new_dist < distances[j]:
                    distances[j] = new_dist
    return distances[dest]

def sum_edges(graph):
    return sum(graph[i][j] for i in range(len(graph)) for j in range(i, len(graph)))

def get_odd(graph):
    degree = [sum(1 for j in range(len(graph)) if graph[i][j] != 0) for i in range(len(graph))]
    odds = [i for i in range(len(degree)) if degree[i] % 2 != 0]
    print(f'Непарні: {odds}')
    return odds

def pair(odds):
    pairs = []
    for i in range(len(odds) - 1):
        pairs.append([])
        for j in range(i + 1, len(odds)):
            pairs[i].append([odds[i], odds[j]])
    print(f"Пари: {pairs}")
    return pairs

def chinese_postman(graph):
    odds = get_odd(graph)
    if len(odds) == 0:
        return sum_edges(graph)
    pairs = pair(odds)
    l = (len(pairs) + 1) // 2
    pairing = []
    def get_pair(pairs, done=[], final=[]):
        if pairs[0][0][0] not in done:
            done.append(pairs[0][0][0])
            for i in pairs[0]:
                f = final[:]
                val = done[:]
                if i[1] not in val:
                    f.append(i)
                else:
                    continue
                if len(f) == l:
                    pairing.append(f)
                    return
                else:
                    val.append(i[1])
                    get_pair(pairs[1:], val, f)
        else:
            get_pair(pairs[1:], done, final)
    get_pair(pairs)
    min_sums = [sum(dijkstra(graph, i[j][0], i[j][1]) for j in range(len(i))) for i in pairing]

    added_dis = min(min_sums)

    chinese_dis = added_dis + sum_edges(graph)
    return chinese_dis

print('Шлях листоноші:', chinese_postman(matrix))