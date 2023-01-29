from sys import stdin
n = int(stdin.readline())
time_list = list(map(int,stdin.readline().split()))
time_list.sort()
ans = 0
for i in range(n):
    ans += sum(time_list[:i+1])
print(ans)
