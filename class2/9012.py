
result=[]

N=int(input())

for i in range(N):
    stk=["Z"]

    ps=input()
    for p in ps:
        if p=="(":
            stk.append(p)
        elif p==")":
            if stk[-1]=="(":
                stk.pop(-1)
            else:
                stk.append(p)

    if "Z" in stk and len(stk)==1:
        result.append("YES")
    else:
        result.append("NO")

print(*result,sep='\n')



