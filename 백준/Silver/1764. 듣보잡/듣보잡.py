from sys import stdin

n, m = map(int,(input().split()))
dic = {}
ans_list = []
for i in range (n):
    name = stdin.readline().strip()
    dic[name] = 1
for j in range (m):
    name = stdin.readline().strip()
    if name in dic:
        ans_list.append(name)

print(len(ans_list))
for k in sorted(ans_list):
    print(k)
