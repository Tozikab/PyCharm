import numpy as np
def popit(n):
    """n = int(input())"""
    numbers = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
    """for i in range(n):
        numbers.append(input().split())"""
    o = []
    counter = 0
    for i in range(1):
        for j in range(1):
            numbers[counter][(n - 1) - j] = numbers[i][j]
            counter += 1
        counter = 0
    for pow in numbers:
        print(pow)
def summ():
    accounts = [[7, 1, 3], [2, 8, 7], [1, 9, 5]]
    exia = []
    sasd = 0
    maxsum = 0
    for i in accounts:
        for j in i:
            sasd += j
        if sasd > maxsum:
            maxsum = sasd
        sasd = 0
    return maxsum
def sashsh(n, m):
    matr = [[0] * m for i in range(n)]
    return matr

print(sashsh(5, 6))