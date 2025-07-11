N=int(input())

for i in range(1,N):
    if i + sum(int(j) for j in str(i))==N:
        print(i)
        quit()

print(0)
