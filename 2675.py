N=int(input())
res=[]
for i in range(N):
    num,s=input().split()
    num=int(num)
    slist=list(s)

    res.append(''.join(ch*num for ch in slist))
    
    
print(*res,sep='\n')

