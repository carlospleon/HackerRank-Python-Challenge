if __name__ == '__main__':
    alphanum = False
    alpha = False
    digit = False
    lower = False
    upper = False
    s = input()
    l = len(s)
    for i in range(0, l):
        if s[i].isalnum():
            alphanum = True
        if s[i].isalpha():
            alpha = True
        if s[i].isdigit():
            digit = True
        if s[i].islower():
            lower = True
        if s[i].isupper():
            upper = True
    print(alphanum)
    print(alpha)
    print(digit)
    print(lower)
    print(upper)
