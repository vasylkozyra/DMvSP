import itertools

def read_matrix(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        matrix = []
        for line in lines:
            row = list(map(int, line.strip().split()))
            matrix.append(row)
        return matrix

def is_isomorphic(A, B):
    n = len(A)
    if len(B) != n:
        return False
    
    degrees_A = [sum(row) for row in A]
    degrees_B = [sum(row) for row in B]
    if sorted(degrees_A) != sorted(degrees_B):
        return False
    
    num_edges_A = sum(sum(row) for row in A) // 2
    num_edges_B = sum(sum(row) for row in B) // 2
    if num_edges_A != num_edges_B:
        return False
    
    for perm in itertools.permutations(range(n)):
        permuted_B = [[B[perm[i]][perm[j]] for j in range(n)] for i in range(n)]
        if permuted_B == A:
            return True
    
    return False

A = read_matrix('lab5\A.txt')
B = read_matrix('lab5\B.txt')

if is_isomorphic(A, B):
    print("Isomorphic")
else:
    print("Not isomorphic")