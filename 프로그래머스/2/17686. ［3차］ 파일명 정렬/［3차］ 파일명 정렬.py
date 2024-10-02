def solution(files):
    #2시
    
    #숫자 반영 정렬 기능
    #N <= 1000, M <= 100 10^5 
    #알고리즘 정렬 -> 배열 쓰면 될 듯
    
    
    
    N = len(files)
    dic = {}
    div = []
    
    idx = 0
    
    for file in files:
        dic[idx] = file
        
        st = -1
        en = N
        num = 0
        for i in range(len(file)):
            if 0 <= ord(file[i]) - ord('0') <= 9:
                if st == -1:
                    st = i
                num = 1
            else:
                if num:
                    en = i
                    break
            
        div.append([file[:st].lower(), int(file[st:en]) , idx])
        idx += 1
            
    div.sort()
    
    answer = []
    for i in range(N):
        answer.append(dic[div[i][2]])
    return answer