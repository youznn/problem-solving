#bfs나 dfs 쓰면 되는 문제
#이차원배열

from collections import deque

n, m = list(map(int, input().split()))
board = [[] for _ in range(n)] #그림저장하는 이차원배열
dr = [1,-1,0,0]
dc = [0,0,1,-1]
cnt = 0 #bfs 시행횟수
max_size = 0

for i in range(n):
    board[i] = list(map(int, input().split()))


#bfs로 그림의 개수 찾기
visited = [[0 for _ in range (m)] for _ in range(n)]

def bfs(r,c):
    q = deque()
    q.append([r,c])
    visited[r][c] = 1
    size = 1
    while q:
        cr, cc = q.popleft()
        for i in range (4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            #범위 체크
            if (nr >= 0 and nc >=0 and nr < n and nc < m):
                if visited[nr][nc] == 0 and board[nr][nc] == 1:
                    visited[nr][nc] = 1
                    q.append([nr,nc])
                    size += 1
    return size

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and board[i][j] == 1:
            cnt += 1
            max_size = max(max_size, bfs(i,j))

print(cnt)
print(max_size)