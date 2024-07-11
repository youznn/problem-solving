#stack, queue

from collections import deque

N = int(input()) #Pn에서의 n. 총 2n+1개이며, n이 홀수일 때 I, 짝수일 때 O
M = int(input())
S = deque(list(input()))

def push_stack():
    idx = 1
    cnt = 0
    temp = 0
    q = deque()
    while S:
        item = S.popleft()
        temp += 1
        if (item == 'I' and idx % 2 == 1) or (item == 'O' and idx % 2 == 0):
            q.append(item)
            idx += 1
        else:
            q = deque()
            if item == "I":
                q.append(item)
                idx = 2
            else:
                idx = 1
        if len(q) == 2*N + 1:
            cnt += 1
            q.popleft()
            q.popleft()
            idx = len(q) + 1
    return cnt

print(push_stack())


