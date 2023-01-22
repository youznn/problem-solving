from collections import deque
num = int(input())

arr = deque()
if num % 2 == 1:
    arr.append(num)
for i in range (2,num+1,2):
    arr.append(i)

if num == 1:
    print(1)
elif num == 2:
    print(2)
else:
    while len(arr) > 1:
        arr.popleft()
        n = arr.popleft()
        arr.append(n)
    print(n)