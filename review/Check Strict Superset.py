seta = set(input().split())
t = int(input())
cont = 0
for i in range(0, t):
    setb = set(input().split())
    if (len(setb-seta)) == 0:
        cont = cont + 1
if cont == t :
    print("True")
else:
    print("False")