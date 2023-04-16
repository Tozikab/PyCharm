import random
n,m = int(input()), int(input())
mult = []
matrix = [[0]*m for _ in range(n)]


for r in range(n):                     # выводим матрицу
    for c in range(n):
        print(matrix[r][c], end=' ')
    print()