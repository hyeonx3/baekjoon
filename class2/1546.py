import sys

N=int(sys.stdin.readline())
scores=list(map(int,sys.stdin.readline().split()))
M=max(scores)

new_scores=[i/M*100 for i in scores]
new_mean=sum(new_scores)/N

print(new_mean)