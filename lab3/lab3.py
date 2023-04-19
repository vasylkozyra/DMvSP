import numpy as np
from python_tsp.exact import solve_tsp_brute_force

matrix = np.loadtxt('lab3/1.txt')

path, distance = solve_tsp_brute_force(matrix)
print(f"Оптимальний шлях: {path}")
print(f"Довжина маршруту: {distance}")