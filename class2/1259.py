import math

def is_pelin(str):
    strlen=len(str)
    
    for i in range(0,math.ceil(strlen/2)):
        if str[i]!=str[strlen-i-1]:
            return "no"
    
    return "yes"

lst=[]
while True:
    s=input()
    if s=='0':
        break
    lst.append(s)

for i in lst:
    print(is_pelin(i))

