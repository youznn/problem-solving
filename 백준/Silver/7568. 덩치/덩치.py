from sys import stdin
n = int(stdin.readline())
box = []
ans = []

for i in range(n):
    box.append(list(map(int,stdin.readline().split())))


for j in box:
    cnt = 1
    for k in box:
        if j[0] < k[0] and j[1] < k[1]:
            cnt += 1
    ans.append(cnt)

print(' '.join(map(str,ans)))
