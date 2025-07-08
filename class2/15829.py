def atoi(ch):
    return ord(ch)-ord('a')+1


N=int(input())
charlist=list(input())
numlist=[atoi(i) for i in charlist]

H=0
for i in range(0,N):
    H+=numlist[i]*31**i 
H%=1234567891

print(H)

