from sys import stdin

dic = {0:1, 1:0, 2:1, 3:1}
t = int(stdin.readline())

for i in range (4,42):
    dic[i] = dic[i-1] + dic[i-2]

for _ in range (t):
    n = int(stdin.readline())
    print(dic[n], dic[n+1])

