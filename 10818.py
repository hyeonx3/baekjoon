import sys

N=input()
lst = list(map(int,sys.stdin.readline().split()))

print(min(lst),max(lst))
