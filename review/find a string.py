def count_substring(string, sub_string):
    cont = 0
    x = len(string)
    y = len(sub_string)
    n = x - y

    for j in range(n + 1):
        m = j + y
        if string[j:m] == sub_string:
            cont = cont + 1
    return str(int(cont))


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
