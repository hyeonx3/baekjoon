def inhabitant(i,j,apt):
    if apt[i][j-1] != -1:
        return apt[i][j-1]
    else:
        apt[i][j-1] = sum(inhabitant(i-1,k,apt) for k in range(1,j+1))
        return apt[i][j-1]




N=int(input())
floor=[]
room=[]
for i in range(N):
    n=int(input())
    k=int(input())
    room.append(k)
    floor.append(n)

apt=[[i for i in range(1,15)]]
for _ in range(max(floor)):
    apt.append([-1]*14)  


for i in range(N):
    print(inhabitant(floor[i],room[i],apt))