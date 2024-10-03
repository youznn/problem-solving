def solution(brown, yellow):
    #카펫의 가로, 세로 크기 구하기
    #카펫의 가로 + 세로는 구할 수 있음. (brown + 4) // 2 하면 됨
    answer = []
    
    total = (brown + 4) // 2
    #가로는 최대 total, 최소 3
    
    for i in range(3, total):
        wid = i
        hei = total - i
        if wid < hei: continue
        
        #노란색의 가로는 wid - 2, 세로는 hei - 2
        print(wid, hei)
        
        if (wid - 2) * (hei -2) == yellow:
            answer.append(wid)
            answer.append(hei)
            
            break
    
    
    
    return answer