def solution(record):
    arr =[]
    dic_name = {}
    for rec in record:
        if rec[0] == 'L':
            temp, user = rec.split(' ')
            arr.append((user, 'L'))
        else:
            temp, user, name = rec.split(' ')
            if rec[0] == 'E':
                arr.append((user,'E'))
                dic_name[user] = name
            else:
                dic_name[user] = name
    
    answer = []
    for i in arr:
        if i[1] == 'E':
            answer.append(f"{dic_name[i[0]]}님이 들어왔습니다.")
        elif i[1] == 'L':
            answer.append(f"{dic_name[i[0]]}님이 나갔습니다.")
        
    
    return answer