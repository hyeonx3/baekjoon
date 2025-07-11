strings=["Fizz","Buzz","FizzBuzz"]
lst=[]
for _ in range (3):
    lst.append(input())

if lst[-1] not in strings:
    next=int(lst[-1])+1
    if next%3==0:
        if next%5==0:
            print(strings[2])
        else:
            print(strings[0])
    elif next%5==0:
        print(strings[1])
    else:
        print(next)
elif lst[-2] not in strings:
    next=int(lst[-2])+2
    if next%3==0:
        if next%5==0:
            print(strings[2])
        else:
            print(strings[0])
    elif next%5==0:
        print(strings[1])
    else:
        print(next)
elif lst[-3] not in strings:
    next=int(lst[-3])+3
    if next%3==0:
        if next%5==0:
            print(strings[2])
        else:
            print(strings[0])
    elif next%5==0:
        print(strings[1])
    else:
        print(next)
