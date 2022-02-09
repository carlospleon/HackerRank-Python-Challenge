def average(array):
    # your code goes here
    x = 0
    r = 0
    arra = set(array)
    for i in arra:
        x = x + i
    s = len(arra)
    r = float(x / s)
    return format(r, ".3f")


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)