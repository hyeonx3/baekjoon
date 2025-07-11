import sys

N=int(sys.stdin.readline())
lst1=list(map(int,sys.stdin.readline().split()))

M=int(sys.stdin.readline())
lst2=list(map(int,sys.stdin.readline().split()))

for i in lst2:
    print(int(i in lst1))