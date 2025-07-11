import sys

N=int(sys.stdin.readline())
lst=[[0,""] for i in range(N)]

for i in range (N):
    lst[i][0],lst[i][1]=sys.stdin.readline().split()
    lst[i][0]=int(lst[i][0])

dic={}
for age,name in lst:
    if age in dic.keys():
        dic[age].append(name)
    else:
        dic[age]=[name]


for age in (sorted(dic.keys())):
    for name in dic[age]:
        print(age,name)