N=int(input())
lst=[]
for i in range(N):
    x,y=map(int,input().split())
    lst.append((x,y))

sorted_lst=sorted(lst, key= lambda x: (x[0],x[1]))
for i in range(N):
    print(*sorted_lst[i])