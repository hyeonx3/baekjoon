import sys

def push(stk,N):
    stk.append(N)

def pop(stk):
    if not stk:
        print(-1)
    else:
        print(stk.pop())

def size(stk):
    print(len(stk))

def empty(stk):
    if not stk:
        print(1)
    else:
        print(0)

def top(stk):
    if not stk:
        print(-1)
    else:
        print(stk[-1])


stk=[]

N=int(sys.stdin.readline())
for i in range(N):
    parts=sys.stdin.readline().split()
    if len(parts)>1:
        comm=parts[0]
        param=parts[1]
    else:
        comm=parts[0]

    func=globals().get(comm)
    if callable(func):
        if comm=="push":
            func(stk,param)
        else:
            func(stk)
        

