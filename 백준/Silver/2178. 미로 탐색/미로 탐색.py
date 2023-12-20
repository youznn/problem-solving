import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
miro = []
for _ in range(n):
    miro.extend(list(sys.stdin.readline().rstrip()))

# 이중반복문 시간 오래 걸릴 것 같으니까 배열 하나로 만들어서 해보자 extend 사용
# 한 줄에 m개니까 index/m 하면 될듯 현재 index를 i라고 하면 왼쪽은 i-1 오른쪽 i+1 아래쪽 i + m 위쪽 i-m 이겠지요 .. 이제 딕셔너리!
dic = {}

for i in range(n * m):
    dic[i] = []
    ways = []
    if i % m != m-1 and 0 <= i + 1 < n * m and miro[i + 1] == '1':
        ways.append(i + 1)
    if 0 <= i - m< n * m and miro[i - m] == '1':
        ways.append(i - m)
    if i % m != 0 and 0 <= i - 1 < n * m and miro[i - 1] == '1':
        ways.append(i - 1)
    if 0 <= i + m < n * m and miro[i + m] == '1':
        ways.append(i + m)
    dic[i] = ways


# 이제 bfs 쓰면 될 듯
def bfs(s):
    queue = deque()
    visited = set()
    cnt = {s:1}
    queue.append(s)
    while(queue):
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            queue.extend(dic[node])
            for v in dic[node]:
                if v not in visited:
                    cnt[v] = cnt[node] + 1
        if node == m * n - 1:
            return visited,cnt

print((bfs(0)[1][m*n-1]))
