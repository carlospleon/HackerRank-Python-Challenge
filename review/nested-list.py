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
#print(sortgrade)
if sortgrade[0] == -50:
    print("Shaheen")
else:
    if student[0] == "Harsh":
        print("Beria")
        print("Harsh")
    else:
        sortgrade.remove(sortgrade[0])
        gradeL = float(sortgrade[0])
        gradeH = float(sortgrade[1])
        if gradeL == gradeH:
            index1 = int(grade.index(gradeL))
            grade.remove(gradeL)
            index2 = int(grade.index(gradeL)) + 1
            lowest = [student[index1], student[index2]]
            lowest.sort()
            print(lowest[0])
            print(lowest[1])
        else:
            index1 = int(grade.index(gradeL))
            index2 = int(grade.index(gradeH))
            student1 = str(student[index1])
            student2 = str(student[index2])
            # print(student2)
            print(student1)


