
n, m = int(input()), int(input())
slob = []
for i in range(n):
        slob.append(input().split())
print(slob)
top = "0"
i, j = [int(_) for _ in input().split()]
for o in range(n):
    top = slob[o][i]
    slob[o][i] = slob[o][j]
    slob[o][j] = top
    print(top)
for i in range(n):
    for j in range(m):
        print(slob[i][j], end=" ")
    print()


























"""from random import *
from math import *
import re
n, m = int(input()), int(input())

number = []
for i in range(n):
    number.append(input().split())
maxin = int(number[0][0])
mao = [0, 0]
for i in range(n):
    for j in range(m):
        if int(number[i][j]) > maxin:
            maxin = int(number[i][j])
            mao.clear()
            mao.append(i)
            mao.append(j)
print(*mao)"""
