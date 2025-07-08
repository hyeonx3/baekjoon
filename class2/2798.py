from itertools import combinations

N,M=map(int,input().split())
cards=list(map(int,input().split()))

best=0
for comb in combinations(cards,3):
    s=sum(comb)
    if s<=M:
        best=max(best,s)

print(best)


#경우의 수가 그렇게 크지 않아 그냥 brute-force로 접근해도 무리 없음