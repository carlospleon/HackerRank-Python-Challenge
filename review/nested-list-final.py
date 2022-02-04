n = int(input())
student = []
grade = []
sortgrade = []
lowest = []

i = 0
for i in range(0, n):
    name = input()
    score = float(input())
    student.append(name)
    grade.append(score)
sortgrade = grade.copy()
sortgrade.sort()
if sortgrade[0] == sortgrade[1]:
    x = (int(sortgrade[0]))
    low1 = grade.index(x)
    copygrade = grade.copy()
    copygrade.remove(x)
    sortgrade = grade.copy()
    sortgrade.sort()
    x = (int(sortgrade[0]))
    low2 = copygrade.index(x) +  n1
    lowest = [str(student[low1]), str(student[low2])]
    lowest.sort()
    print(lowest[0])
    print(lowest[1])
else:
    x = grade.index(float(sortgrade[1]))
    y = grade.index(float(sortgrade[2]))
    print(student[x])
    print(student[y])


