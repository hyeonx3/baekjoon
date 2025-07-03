s=input()
alpha="abcdefghijklmnopqrstuvwxyz"
numlst=[0]*26
index=0

for ch in alpha:
    numlst[alpha.index(ch)]=s.find(ch)

print(*numlst)