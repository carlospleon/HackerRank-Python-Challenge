from collections import defaultdict
inp = list(map(int, input().split()))
n = inp[0]
m = inp[1]
cont = 0
dn = defaultdict(list)
for i in range(0, n):
    dn['A'].append(input())
for i in range(0, m):
    dn['B'].append(input())
for j in range(0, m):
    cont = 0
    for i in range(0, n):
        if dn['A'][i] == dn['B'][j]:
            print(i + 1, end=" ")
            cont = 1
    if cont == 0:
        print('-1', end=" ")
    print()
