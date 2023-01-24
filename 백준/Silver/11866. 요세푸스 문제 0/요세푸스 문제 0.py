from sys import stdin

n, k= map(int,input().split())
ans_list = []
queue = [i for i in range(n+1)] #큐 생성
cnt = 1
current = 1
while len(queue) > 1:
    if current > len(queue)-1:
        current = current % len(queue) + 1
    if cnt % k == 0:
        ans_list.append(queue.pop(current))
        cnt += 1
    else:
        cnt += 1
        current += 1

print("<"+", ".join(map(str,ans_list))+">")