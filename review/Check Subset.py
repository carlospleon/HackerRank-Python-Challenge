t = int(input())
for i in range(0, t):
    ne = int(input())
    arrne = set(input().split())
    nf = int(input())
    arrnf = set(input().split())
    s = arrne - arrnf
    if len(s) == 0:
        print("True")
    else:
        print("False")