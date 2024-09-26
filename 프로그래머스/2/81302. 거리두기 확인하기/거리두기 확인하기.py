def check(place, cr, cc):
    dr1 = [1,-1,0,0,2,-2,0,0]
    dc1 = [0,0,-1,1,0,0,-2,2]
    #기준 위치에서 상하좌우에 있는지 체크하기
    for i in range(8):
        nr = cr + dr1[i]
        nc = cc + dc1[i]
        ##OOB 체크
        if(nr < 0 or nc < 0 or nr > 4 or nc > 4): continue
        #2칸 이상일 때는 가운데 칸이 파티션인지 체크해야 함
        if i >= 4:
            if place[nr][nc] == 'P':
                center_r = (nr + cr) // 2
                center_c = (nc + cc) // 2
                if place[center_r][center_c] != 'X': return 0
        else:
            if place[nr][nc] == 'P': return 0

    #기준 위치에서 대각선 체크하기
    dr2 = [-1,1,-1,1]
    dc2 = [-1,1,1,-1]
    
    for i in range(4):
        nr = cr + dr2[i]
        nc = cc + dc2[i]
        if(nr < 0 or nc < 0 or nr > 4 or nc > 4): continue
        #중간에 둘 다 파티션인지 체크해야 함
        if place[nr][nc] == 'P':
            if(place[nr][cc] != 'X' or place[cr][nc] != 'X'): return 0
    

    return 1
        
        


def solution(places):
    answer = []
    for place in places:
        flag = 0
        for i in range (5):
            if flag == 1:
                break
            for j in range(5):
                if place[i][j] == 'P':
                    if check(place, i, j) == 0:
                        flag = 1
                        break
        answer.append(0 if flag == 1 else 1)
    return answer
