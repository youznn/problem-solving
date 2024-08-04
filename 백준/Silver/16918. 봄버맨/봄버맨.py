#폭탄 있으면 3초 뒤 폭발, 인접 네 칸도 같이 폭발 연쇄 반응 없음
#처음에 폭탄 설치함
#1초간 아무것도 안 함
#다음 1초간 폭탄 없는 모든 칸에 폭탄을 설치함
#1초 지난 후, 3초전에 설치한 모든 폭탄이 파괴됨
#위 두개 반복함

R, C, N  = list(map(int,input().split()))
tick = 0
board = []
bombs = [[-1 for _ in range(C)] for _ in range(R)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]


for _ in range (R):
    board.append(list(map(str,input().rstrip())))

#clock update
for i in range(R):
    for j in range(C):
        if board[i][j] == 'O':
            bombs[i][j] = 2

tick += 1 # 처음 1초

    #다음 1초간 폭탄 없는 모든 칸에 폭탄 설치하기
while tick < N:
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                bombs[i][j] = 3
                board[i][j] = 'O'
            else:
                bombs[i][j] -= 1

    tick += 1
    if tick == N:
        break

    #1초 뒤에, timer = 1인 폭탄 파괴됨
    for i in range(R):
        for j in range(C):
            if bombs[i][j] == 1:
                bombs[i][j] = -1
                board[i][j] = '.'
                for k in range(4):
                    nr = i + dr[k]
                    nc = j + dc[k]
                    if 0<=nr<R and 0<=nc<C:
                        if bombs[nr][nc] == 1: #터져야 하는 폭탄이면
                            continue
                        bombs[nr][nc] = -1
                        board[nr][nc] = '.'
            if bombs[i][j] > 1:
                bombs[i][j] -= 1
    tick += 1



for i in range (R):
    for j in range(C):
        print(board[i][j], end='')
    print()
