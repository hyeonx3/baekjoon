ISBM=list(input())

for i in ISBM:
    if i=="*":
        damaged=ISBM.index(i)
        ISBM[damaged]=0

ISBM=list(map(int,ISBM))

for i in range(1,12,2):
    ISBM[i]=ISBM[i]*3

for i in range (0,10):
    ISBM[damaged]=i if damaged%2==0 else i*3
    check=10-(sum(ISBM[:12])%10)
    if ISBM[12]==check or (check==10 and ISBM[12]==0):
        print(i)
