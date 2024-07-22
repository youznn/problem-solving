import sys
input = sys.stdin.read
from collections import deque

data = input().split()
N, M, K = int(data[0]), int(data[1]), int(data[2])

dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]

board = []
index = 3
for i in range(N):
    board.append(list(map(int, data[index + i])))

def bfs():
    q = deque()
    q.append((0,0,K))
    visited = [[[0 for _ in range (K+1)] for _ in range(M)] for _ in range(N)]
    visited[0][0][K] = 1
    while q:
        cr ,cc, ck = q.popleft()
        #print(cr,cc,ck)
        # out of bound
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc][ck] == 0:
                #print(board[nr][nc])
                if board[nr][nc] == 0:
                    q.append((nr,nc,ck))
                    visited[nr][nc][ck] = visited[cr][cc][ck] + 1
                if board[nr][nc] == 1 and ck > 0 and visited[nr][nc][ck-1] == 0:
                    q.append((nr,nc,ck-1))
                    visited[nr][nc][ck-1] = visited[cr][cc][ck] + 1
    return visited[N-1][M-1]

ans_list = bfs()
#print(ans_list)
if sum(ans_list) == 0:
    print(-1)
else:
    ans_list.sort()
    for m in ans_list:
        if m != 0:
            print(m)
            break
