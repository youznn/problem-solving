#15:50
#함께 주문한 단품메뉴들을 코스요리 메뉴로 구성
#최소 2가지 이상 단품메뉴
#최소 2명 이상 손님으로부터 주문되었어야 함
from itertools import combinations

def solution(orders, course):
    # course
    all_combs = {}
    courses = {}
    for order in orders:
        for i in course:
            compounds = list(combinations(order, i))
            for compound in compounds:
                compound = tuple(sorted(list(compound)))
                #compound = list(compound).sort()
                all_combs[compound] = all_combs.get(compound, 0) + 1
                courses[i] = courses.get(i, []) 
                #print(all_combs[compound])
                if all_combs[compound] < 2:
                    continue
                if (not courses[i]) or all_combs[compound] > all_combs[courses[i][0]]:
                    courses[i] = [compound]
                elif compound == courses[i][0]:
                    courses[i] = [compound]
                elif all_combs[compound] == all_combs[courses[i][0]]:
                    courses[i] += [compound]
                    
    answer = []
    for values in courses.values():
        for i in range(len(values)):
            answer.append(''.join(values[i]))
    answer.sort()
    
    return answer