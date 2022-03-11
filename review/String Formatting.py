def print_formatted(number):
    # your code goes here
    l = len(format(number, "b"))
    for i in range(1, number+1):
        print(str(i).rjust(l, " "), end=" ")
        print(str(format(i, "o")).rjust(l, " "), end=" ")
        print(str(format(i, "X")).rjust(l, " "), end=" ")
        print(str(format(i, "b")).rjust(l, " "))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)