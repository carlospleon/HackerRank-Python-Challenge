n = int(input())
set2 = list(map(int, input().split()))
set1 = set(set2)
cmd = int(input())
comands = []
for i in range(0, cmd):
    arr = list(map(str, input().split()))
    if arr[0] == "remove":
        set1.discard(int(arr[1]))
    if arr[0] == "discard":
        set1.discard(int(arr[1]))
    if arr[0] == "pop":
        set1.pop()
print(sum(set1))




