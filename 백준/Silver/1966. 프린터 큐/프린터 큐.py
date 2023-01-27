from sys import stdin

def add_zero(n):
    return [n,0]

t = int(input()) #테스트케이스의 개수
for i in range (t):
    n, m = map(int, input().split())
    importance_list = []
    importance_list = list(map(int,stdin.readline().split()))
    importance_list = list(map(add_zero,importance_list))
    importance_list[m] = [importance_list[m][0], -1]

    cnt = 0
    while True:
        if importance_list[0][0] == (max(importance_list))[0]:
            paper = importance_list.pop(0)
            cnt += 1
            if paper[1] == -1:
                break
        else:
            importance_list.append(importance_list.pop(0))
    print(cnt)