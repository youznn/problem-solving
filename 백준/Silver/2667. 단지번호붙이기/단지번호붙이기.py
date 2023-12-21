# Using BFS. Push all 1s in queue. make two direction lists dx, dy.
import sys
from collections import deque

n = int(input())
houses = []
for _ in range(n):
    houses.append(list(map(int, (input()))))

empty = houses

def bfs(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = set()
    queue = deque()
    queue.append((x, y))
    while queue:
        node = queue.popleft()
        x , y = node
        if node not in visited:  # house
            visited.add(node)
            empty[x][y] = 0
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                if 0 <= nx < n and 0 <= ny < n and houses[nx][ny] == 1:
                    queue.append((nx,ny))
    return len(visited)

num_list = []
for i in range (n):
    for j in range (n):
        if empty[i][j]:
            num_list.append(bfs(i,j))

lens = len(num_list)
print(lens)
num_list.sort()
for z in num_list:
    print(z)