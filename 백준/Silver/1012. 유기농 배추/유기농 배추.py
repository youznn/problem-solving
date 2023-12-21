# Using BFS. Make a dictionary!
import sys
from collections import deque

def bfs(s, box):
    q = deque()
    q.append(s)
    visited = set()
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    while q:
        node = q.popleft()
        x, y = node
        if node not in visited:
            visited.add(node)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if 0 <= nx < m and 0 <= ny < n and (nx, ny) in box:
                    q.append((nx, ny))
                    box.remove((nx,ny))
    return len(visited)

t = int(input())
for _ in range(t):
    m, n, k = map(int, (input().split()))
    box = []

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        box.append((x, y))

    cnt = 0
    for i in range (m):
        if not box:
            break
        for j in range (n):
            if (i,j) in box:
                bfs((i,j),box)
                cnt += 1
    print(cnt)


