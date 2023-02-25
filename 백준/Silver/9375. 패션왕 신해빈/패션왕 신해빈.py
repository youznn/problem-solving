import sys

t = int(input())
for _ in range (t):
    n = int(sys.stdin.readline())
    dic = {}
    for _ in range(n):
        a,b = sys.stdin.readline().strip().split()
        dic[b] = dic.get(b,0) + 1
    sum = 1
    for i in dic.values():
        sum *= (i+1)
    print(sum-1)
