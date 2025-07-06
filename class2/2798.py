N,M=map(int,input().split())
numlist=list(map(int,input().split()))
min=0

def is_blackjack(num,cards,pick,min):
    if num==3:
        pick=[]

        
    for i in cards:
        pick.append(i)
        if sum(pick)<=M:
            is_blackjack(num-1,cards.pop(i),pick,min)
            if num==0:
                if sum(pick)<=M and sum(pick)>=min:
                    min=sum(pick)

is_blackjack(3,numlist,[],min)
print(min)