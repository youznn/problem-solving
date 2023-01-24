from sys import stdin
from collections import deque

n = int(stdin.readline())
deq = deque()

for i in range (n):
    comm = stdin.readline()
    comm = comm[:-1]
    if comm[:9] == "push_back":
        deq.append(comm[10:])
    elif comm[:10] =="push_front":
        deq.appendleft(comm[11:])
    elif comm == "front":
        if deq:
            print(deq[0])
        else:
            print("-1")
    elif comm == "back":
        if deq:
            print(deq[-1])
        else:
            print("-1")
    elif comm == "pop_front":
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif comm == "pop_back":
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif comm == "size":
        print(len(deq))
    elif comm == "empty":
        if deq:
            print("0")
        else:
            print("1")
    else:
        print("???")