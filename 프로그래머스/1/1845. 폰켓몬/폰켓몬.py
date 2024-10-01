def solution(nums):
    #최대한 많은 종류
    dic = {}
    for n in nums:
        dic[n] = dic.get(n, 0) + 1
    
    if (len(dic) >= len(nums)//2):
        answer = len(nums)//2
    else:
        answer = len(dic)
    return answer