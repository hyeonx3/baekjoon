N=int(input())

score=[]
for i in range(N):
    total=0
    s=input()
    count=0
    for ch in s:
        if ch=="O":
            if count!=0:
                count+=1
            else:
                count=1
        elif ch=="X":
            count=0
            
        total+=count
        
    score.append(total)

print(*score, sep='\n')