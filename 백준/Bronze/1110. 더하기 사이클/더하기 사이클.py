import sys

n = int(input())


goal = n
cnt = 1
if n < 10:
    n = "0"+str(n)
n = str(n)
n_sum = str(int(n[0]) + int(n[1]))
n = int(n[-1] + n_sum[-1])
while n != goal:
    if n < 10:
        n = "0" + str(n)
    n = str(n)
    n_sum = str(int(n[0]) + int(n[1]))
    n = int(n[-1] + n_sum[-1])
    cnt += 1
print(cnt)