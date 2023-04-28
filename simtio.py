import numpy as np
import math
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
def sashsh(n):

    n = int(input())
    matr = []

    for i in range(n):
        matr.append(input().split())
    for i in range(n):
        for j in range(n):
            print(matr[(n - 1) - j][i], end=" ")
        print()
    """for i in range(n):
        for j in range(n):
            print(matr[i][j], end=" ")
        print()
    """
    xy = input()
    y = '87654321'.index(xy[1])
    x = 'abcdefgh'.index(xy[0])
    n = 8
    doska = []
    for i in range(n):
        for j in range(n):
            if x == j and y == i:
                print("N", end=" ")
            elif (x + 2 == j or x - 2 == j) and (y + 1 == i or y - 1 == i):
                print("*", end=" ")
            elif (x + 1 == j or x - 1 == j) and (y - 2 == i or y + 2 == i):
                print("*", end=" ")
            else:
                print(".", end=" ")
        print()
def check_array():
    n = 3
    matr = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '8']]
    for i in range(n):
        matr.append(input().split())
    for i in range(n):
        for j in range(n):
            if int(matr[i][j]) > n ** 2:
                return False
            if set(range(1, n**2+1)) in matr:
                pass
    return
    print("YES" if check_array() else "NO")
def diagonal():
    n = input()
    n = int(n)
    m = n
    matr = [[0] * m for i in range(n)]
    for i in range(m):
        for j in range(n):
            if j > i and ((n - 1) - i) > j or ((n - 1) - i) < j and i > j:
                matr[i][j] = 1
            matr[i][i] = 1
            matr[i][(n - 1) - i] = 1
    for i in range(n):
        for j in range(m):
            print(matr[i][j], end=" ")
        print()
def diagonali():
    n, m = input().split()
    n, m = int(n), int(m)
    matr = [[0] * m for i in range(n)]
    counter = 0
    for i in range(n):
        for j in range(m):
            counter += 1
            if i % 2 != 0:
                matr[i][(m - 1) - j] = counter
            else:
                matr[i][j] = counter
    for i in range(n):
        for j in range(m):
            print(matr[i][j], end=" ")
        print()
def summmatri():
    matr = [[1, 0],
            [4, 1]]
    matro = [[1, 2],
             [3, 4]]
    counter = 0
    c = [[0, 0], [0, 0]]
    for row in range(25):
        for k in range(2):
            for i in range(2):
                for j in range(2):
                    c[k][i] += matr[k][j] * matr[j][i]
    for i in c:
        print(i)
    counter = 4
    for i in range(25):
        counter *= counter
    print(counter)
def umnoj():
    #что-то сложно как-то
    n, m = input().split()
    n, m = int(n), int(m)
    matr1 = []
    matr2 = []
    for i in range(n):
        row = list(map(int, input().split()))
        matr1.append(row)
    input()
    n, m = input().split()
    n, m = int(n), int(m)
    for i in range(n):
        row = list(map(int, input().split()))
        matr2.append(row)
    matrumn = [[0] * m for i in range(n)]
    for k in range():
        for i in range(n):
            for j in range(m):
                matrumn[i][j] = matr1[i][j] + matr2[i][j]
    for i in matrumn:
        print(i)
    print(matrumn)
def spural():
    n, m = input().split()
    n, m = int(n), int(m)
    matrumn = [[0] * m for i in range(n)]
    counter = 0
    for i in range(n):
        for j in range(m):
            counter += 1
            print(m - 1, j, "j")
            if j == (m - 1):
                matrumn[j][i] = counter
            else:
                matrumn[i][j] = counter
    for i in matrumn:
        print(i)
def what():
    n = int(input())
    matr = []
    counter = 1
    for i in range(1, n + 1):
        matr.append(counter)
    for i in matr:
        print(i)
    for i in range(n+1):
        for j in range(i+1):
            b = math.factorial(i) / (math.factorial(j) * math.factorial(i - j))
            print(int(b), end=" ")
        print()
def news():
    n = input().split()
    mass = []
    row = []
    for i in range(len(n) - 1):
        if n[i] == n[i + 1]:
            row.append(n[i + 1])
        elif n[i] != n[i + 1] and len(row) > 0:
            row.append(n[i])
            mass.append(row)
            row = []
        else:
            if len(row) > 0:
                mass.append(row)
            else:
                row.append(n[i])
                mass.append(row)
            row = []
    if len(row) > 0:
        row.append(n[len(n) - 1])
        mass.append(row)
    else:
        row.append(n[len(n) - 1])
        mass.append(row)
    print(mass)

poet_data = ('Пушкин', 1799, 'Санкт-Петербург')
m = ''.join(poet_data)
print(m)

print(poet_data)
