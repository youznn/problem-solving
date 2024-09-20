from collections import deque
import string

def solution(cacheSize, cities):
    q = deque()
    answer = 0
    #hit인 경우 실행시간은 1
    for city in cities:
        city = city.lower()
        
        #hit cases
        if city in q:
            q.append(city)
            q.remove(city)
            answer += 1
        
        elif len(q) < cacheSize:
            q.append(city)
            answer += 5

        #miss cases
        elif cacheSize == 0:
            return len(cities) * 5
        
        else:
            q.popleft()
            q.append(city)
            answer += 5
        
    
    return answer