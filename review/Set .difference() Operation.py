ne = int(input())
arrne = set(map(int, input().split()))
nf = int(input())
arrnf = set(map(int, input().split()))
s = arrne - arrnf
print(len(s))