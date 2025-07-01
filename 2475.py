lst=list(map(int,input().split()))
val=sum([x**2%10 for x in lst])
print(val%10)

