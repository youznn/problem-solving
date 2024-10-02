def solution(stones, k):
    #01:12
    
    # 가능한 니니즈 친구들은 최대 2억마리 -> 이분탐색 느낌
    # 연속되는 0이 K개를 넘어가는 구간이 있으면 안 됨.
    # 만약 그러한 구간이 있다면 마리수 줄여서 수행. 없다면 마리수 늘려서 수행.
    
    st = 0
    en = max(stones) + 1
    
    while (st < en):
        # upper bound
        mid = (st + en) // 2
        #print(st, en, mid)
        zeros = 0 # 0이 몇번 나오는지
        for stone in stones :
            if stone - mid <= 0:
                zeros += 1 # 0이하면 zeros++
            else:
                zeros = 0
            if zeros == k: # 연속되는 0이 k개가 되면, 니니즈 줄여야 함
                en = mid
                break
        if zeros < k:
            st = mid + 1 #만약 다 통과하면 니니즈 늘려야 함        
    
    answer = st
    return answer