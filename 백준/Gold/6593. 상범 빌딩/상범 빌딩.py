from collections import deque

#동서남북상하
#막혔거나 갈 수 있거나
#탈출여부, 걸리는 시간 -> BFS쓰면 될 것 같음

#방향 리스트
dr = [1,-1,0,0,0,0]
dc = [0,0,1,-1,0,0]
dl = [0,0,0,0,1,-1]

def bfs(start, visited, depth): #start = [r,c,l]
    q = deque()
    q.append(start)
    visited[start[2]][start[0]][start[1]] = 1
    while q:
        cr, cc, cl = q.popleft()
        for i in range(6):
            nr = cr + dr[i]
            nc = cc + dc[i]
            nl = cl + dl[i]
            #outofbound
            if  R > nr >= 0 and C >nc >=0 and L >nl >= 0 and visited[nl][nr][nc] == 0:
                if building[nl][nr][nc] == '.':
                    visited[nl][nr][nc] = 1
                    q.append([nr,nc,nl])
                    depth[nl][nr][nc] = depth[cl][cr][cc] + 1
                elif building[nl][nr][nc] == 'E':
                    depth[nl][nr][nc] = depth[cl][cr][cc] + 1
                    return depth[nl][nr][nc]
                else:
                    continue
    return False

def find_start(building , L, R, C):
    for i in range (L):
        for j in range(R):
            for k in range(C):
                if building[i][j][k] == 'S':
                    return [j,k,i]

while True:
    L, R, C = list(map(int,input().split()))
    if L == R == C == 0:
        break

    #건물 저장하는 리스트
    building = [[] for _ in range(L)]
    for i in range(L):
        for j in range(R):
            building[i].append(list(input()))
        input()

    visited = [[[0 for _ in range (C)] for _ in range(R)] for _ in range(L)]
    depth = [[[0 for _ in range (C)] for _ in range(R)] for _ in range(L)]


    ans = bfs(find_start(building,L,R,C),visited,depth)
    if ans:
        print(f'Escaped in {ans} minute(s).')

    else:
        print("Trapped!")


