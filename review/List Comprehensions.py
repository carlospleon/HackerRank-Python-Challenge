x = int(input("x = "))
y = int(input("y = "))
z = int(input("z = "))
n = int(input("n = "))

i = 0
j = 0
k = 0
print("[", end="")
while i <= x:
    while j <= y:
        while k <= z:
            if n != i + j + k:
                print("[", end="")
                print(str(i) + ", ", end="")
                print(str(j) + ", ", end="")
                print(str(k), end="")
                print("]", end="")
                if k == z and j == y and i == x:
                    print("] ", end="")
                else:
                    print(", ", end="")
            k += 1
        k = 0
        j += 1
    j = 0
    i += 1


