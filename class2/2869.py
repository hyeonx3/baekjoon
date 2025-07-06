A,B,V=map(int,input().split())

for i in range(V):
    if (A-B)*i +A >=V:
        print(i+1)
        break