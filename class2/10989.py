import sys

N=int(input())
cnt=[0]*10000

for _ in range(N):
    x=int(sys.stdin.readline().rstrip())
    cnt[x-1]+=1

for i in range(10000):
    if cnt[i]==0:
        continue
    else:
        for _ in range(cnt[i]):
            print(i+1)