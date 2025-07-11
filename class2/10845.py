from collections import deque
import sys

dq=deque()
N=int(sys.stdin.readline())

for i in range(N):
    parts=sys.stdin.readline().split()
    if len(parts)>1:
        comm,val=parts[0],parts[1]

        if comm=="push":
            dq.append(val)        
    else:
        comm=parts[0]

        if comm=="pop":
            if not dq:
                print(-1)
            else:
                print(dq.popleft())
        elif comm=="size":
            print(len(dq))
        elif comm=="empty":
            if not dq:
                print(1)
            else:
                print(0)
        elif comm=="front":
            if not dq:
                print(-1)
            else:
                print(dq[0])
        elif comm=="back":
            if not dq:
                print(-1)
            else:
                print(dq[-1])




