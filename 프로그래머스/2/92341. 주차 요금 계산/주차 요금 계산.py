# 주차 요금 계산
# 해시로 풀어보면 될 것 같음.
# 시각 처리만 잘하면 될 듯
def solution(fees, records):
    base_time, base_price, unit_time, unit_price = fees #정수 배열
    dic = {}
    times = {}
    prices = {}
    
    def cal_time(in_time, out_time):
        return (out_time[0] * 60 + out_time[1]) - (in_time[0] * 60 + in_time[1])
    
    
    for record in records:
        time, car_num, inout = record.split()
        #차량번호가 key인 딕셔너리에 value로 time 넣기
        dic[car_num] = dic.get(car_num, []) + [time]
    
        
    #시간 계산하기
    for key in dic.keys():
        temp_in = []
        temp_out = [23,59]
        for i in range(len(dic[key])):
            if i % 2 == 0: #in
                temp_in = list(map(int,dic[key][i].split(":")))
            else: #out
                temp_out = list(map(int,dic[key][i].split(":")))
                times[key] = times.get(key,0) + cal_time(temp_in, temp_out)
                temp_out = [23,59]
        if (len(dic[key]) % 2 == 1): # out 안 찍힌 경우
            times[key] = times.get(key,0) + cal_time(temp_in, temp_out)
            
    #요금 계산하기
    for key in times.keys():
        if times[key] <= base_time:
            prices[key] = base_price
        else:
            prices[key] = base_price + ((times[key] - base_time + unit_time - 1) // unit_time ) * unit_price
        
    prices = sorted(prices.items())
    answer = []
    
    for a in prices:
        answer.append(a[1])
    return answer