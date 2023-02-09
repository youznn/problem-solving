import sys

n, m = map(int,(input().split()))

dic = {}
for _ in range (n):
    add, pw = sys.stdin.readline().strip().split()
    dic[add] = pw

for _ in range (m):
    print(dic[sys.stdin.readline().strip()])