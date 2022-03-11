from collections import namedtuple
student = namedtuple('student', 'ID MARKS CLASS NAME')
n = int(input())
average = 0
column = list(map(str, input().split()))
cid = 0
cmarks = 0
cclass = 0
cname = 0
for i in range(0, 4):
    if column[i] == "ID":
        cid = i
    if column[i] == 'CLASS':
        cclass = i
    if column[i] == 'MARKS':
        cmarks = i
    if column[i] == 'NAME':
        cname = i
for i in range(0, n):
    inpt = list(map(str, input().split()))
    new = student(ID=inpt[cid], MARKS=inpt[cmarks], CLASS=inpt[cclass], NAME=inpt[cname])
    average = int(new.MARKS) + average
print(average/n)