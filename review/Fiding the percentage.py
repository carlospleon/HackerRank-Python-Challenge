if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    i = 0
    average = 0
    for i in range(3):
        average = student_marks[query_name][i] + average
    average = average / 3
    print(format(average, ".2f"))
