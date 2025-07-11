import sys

N=int(input())
strings=[]
for _ in range(N):
    temp=sys.stdin.readline().rstrip()
    if temp in strings:
        continue
    strings.append(temp)
print(*sorted(strings,key=lambda x: (len(x),x)),sep='\n')