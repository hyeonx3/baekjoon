lst=[]

for i in range(10):
    lst.append(int(input()))

st={i%42 for i in lst}
print(len(st))