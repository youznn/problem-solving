# 어피치보다 점수가 높아야지만 해당 점수를 가져감.
# 어피치보다 점수가 낮으면 의미가 없음.


apeach_box = []
max_diff = 0
max_diff_box = [0 for _ in range (11)]
def solution(n, info):
    global apeach
    global apeach_box
    apeach_box = info
    backtracking(n,[0 for _ in range(11)],0)
    answer = max_diff_box
    if calculate_score(max_diff_box) == False:
        answer = [-1]
    return answer


def choose_curr(score_box):
    global max_diff_box
    for i in range(10,-1,-1):
        if score_box[i] > max_diff_box[i]:
            print(i)
            return True
        if max_diff_box[i] > score_box[i]:
            print(i)
            return False


def calculate_score(score_box):
    global apeach_box
    score = 0
    apeach_score = 0
    for i in range(11):
        if score_box[i] > apeach_box[i]:
            score += (10-i)
        elif score_box[i] == apeach_box[i] == 0:
            continue
        else:
            apeach_score += (10-i)
    if apeach_score > score:
        return False
    else:
        #print(score, apeach_score, score_box)
        return score - apeach_score

def backtracking(left_score, curr_score_box, next_idx):
    global max_diff
    global max_diff_box

    if next_idx == 10:
        curr_score_box[10] = left_score
        curr_diff = calculate_score(curr_score_box)
        #print(curr_diff)
        if curr_diff:
            if curr_diff > max_diff:
                max_diff = curr_diff
                max_diff_box = curr_score_box[:]
            elif curr_diff == max_diff:
                if choose_curr(curr_score_box):
                    max_diff = curr_diff
                    max_diff_box = curr_score_box[:]

        return

    else:
        #만약 left_score가 없으면 검사하고 return
        if left_score == 0:
            backtracking(left_score, curr_score_box, next_idx + 1)
            return

        #현재 스코어 박스에 next_idx로 온 값 넣기
        ryan_idx_score = apeach_box[next_idx] + 1
        if ryan_idx_score <= left_score:
            curr_score_box[next_idx] = ryan_idx_score
            #넣기로 결정한 경우에, 다음 스탭
            backtracking(left_score-ryan_idx_score, curr_score_box, next_idx+1)

        # 결정 안 한 경우에, 다음 스탭
        curr_score_box[next_idx] = 0
        backtracking(left_score, curr_score_box, next_idx + 1)
        return
