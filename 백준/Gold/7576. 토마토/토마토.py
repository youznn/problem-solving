import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
tomato = []
ripe_tomatos = []
num_empty_box = 0

for _ in range(m):
    tomato.append(list(map(int, (sys.stdin.readline().split()))))

for i in range(m):
    for j in range(n):
        if tomato[i][j] == 1:
            ripe_tomatos.append((i, j))
        elif tomato[i][j] == -1:
            num_empty_box += 1

def bfs(start_nodes):
    if len(ripe_tomatos) == m * n - num_empty_box:
        return 0
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    queue = deque()
    visited = set()
    for starts in start_nodes:
        queue.append(starts)  # 모든 1인 토마토들을 일단 큐에 넣는다.
    # bfs 진행
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            x, y = node
            for k in range(4):
                nx = x + dx[k]
                ny = y + dy[k]
                if 0 <= nx < m and 0 <= ny < n and tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    queue.append((nx, ny))

    if len(visited) == n * m - num_empty_box:
        return max(max(row) for row in tomato) - 1
    else:
        return -1


print(bfs(ripe_tomatos))
