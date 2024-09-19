def solution(queue1, queue2):
    
    # target 값 구하기
    if (sum(queue1) + sum(queue2)) % 2 == 0:
        target = (sum(queue1) + sum(queue2)) // 2
    else:
        return -1
    
    # 원형 배열 만들기. start랑 end 설정하기
    # 뒤에 붙는 건 insert, 앞에 빼는 건 pop
    circle = queue1 + queue2
    start = 0
    count = 0
    end = len(queue1) - 1
    sum_q = sum(queue1)
    flag = 0
    
    while sum_q != target:
        #한 바퀴 다 돌면
        if start == 0 and end == len(queue1) - 1 and count > 0:
            return -1
        
        #다른 큐가 비어있으면
        if end - start == len(circle) - 1:
            return -1
        
        #최대 횟수 지정
        if count > len(circle)*3:
            return -1
        
        # target보다 작을 경우 insert
        if sum_q < target:
            count += 1
            end = (end + 1 + len(circle)) % len(circle) #new end
            sum_q += circle[end]
            
        # target보다 클 경우 pop
        elif sum_q > target:
            count += 1
            sum_q -= circle[start] #old start
            start = (start + 1 + len(circle)) % len(circle)   
    
    return count
    
    print(target)
    answer = -2
    return answer