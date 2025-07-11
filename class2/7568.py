N=int(input())
lst=[[0,0,0] for _ in range(N)]
for i in range(N):
    x,y=map(int,input().split())
    lst[i][0]=x
    lst[i][1]=y

count=0


for _ in range (5):
    for i in range(N):
        if lst[i][2]!=0:
            count+=1
        #이번 반복의 count 세팅
    

    for i in range(N):
        for j in range(N):
            if lst[j][2]!=0:
                continue
            for j in range(N):
                if lst[i][0]< lst[j][0] and lst[i][1]<lst[i][1]:
                    break
                else:
                    lst[i][2]=count+1
    print(lst,'\n')



