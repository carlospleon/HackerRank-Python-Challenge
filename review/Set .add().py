stack = []
l = 0
if __name__ == '__main__':
    n = int(input())
    for x in range(0, n):
        stack.append(input())
    l = len(set(stack))
    print(l)