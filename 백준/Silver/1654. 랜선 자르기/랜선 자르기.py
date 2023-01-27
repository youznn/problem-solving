from sys import stdin
k, n = map(int,input().split())
length_list = []

for i in range (k):
    length = int(stdin.readline())
    length_list.append(length)

length_list.sort()

start = 1
end = length_list[-1]
mid = (start + end) // 2

while True:
    cnt = 0
    mid = (start + end) // 2
    for i in length_list:
        cnt += i // mid
    if cnt >= n:
        if start >= mid:
            break
        start = mid
    else:
        end = mid

cnt = 0
for i in length_list:
    cnt += i // end
if cnt == n:
    print(end)
else:
    print(mid)