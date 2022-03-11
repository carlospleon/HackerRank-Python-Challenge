from collections import deque

db = deque()
n = int(input())

for i in range(0, n):
    inp = input().split()
    if(inp[0] == 'append'):
        db.append(inp[1])
    elif(inp[0] == 'popleft'):
        db.popleft()
    elif(inp[0] == 'appendleft'):
        db.appendleft(inp[1])
    elif(inp[0] == 'pop'):
        db.pop()

print(' '.join(db))