import sys

N=int(sys.stdin.readline())
lst=[]
for i in range(N):
    x,y=map(int,sys.stdin.readline().split())
    lst.append((x,y))

sorted_lst=sorted(lst, key= lambda x: (x[1],x[0]))
for i in range(N):
    print(*sorted_lst[i])