N=int(input())
result=[]
for _ in range(N):
    A,B= map(int,input().split())
    result.append(A+B)

print(*result, sep='\n')