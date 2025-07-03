s=input()
count=1

for i in s:
    if i==" ":
        count +=1

if s[0]==" ":
    count -=1
if s[-1]==" ":
    count -=1

print(count)