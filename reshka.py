n = 3
slova = [['1', '4', '9'], ['6', '7', '8'], ['1', '1', '6']]
counter = 0
"""for i in range(n):
    slova.append(input().split())"""
counter = int(slova[0][0])
for i in range(n):
    if int(slova[i][(n - 1) - i]) > counter:
        counter = int(slova[i][(n - 1) - i])
    if int(slova[i][i]) > counter:
        counter = int(slova[i][i])
    for j in range(i+1):
        if int(slova[i][j]) > counter:
            counter = int(slova[i][j])
print(counter)