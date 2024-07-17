#능력치 합들의 차의 최소 출력
#그리디?
import sys
import itertools
input = sys.stdin.readline

N = int(input())
board = [[] for _ in range(N+1)]
sums = [[0 for i in range(N+1)] for _ in range(N+1)]
for i in range(1,N+1):
    board[i] = [0] + list(map(int,(input().split())))

for i in range(1,N+1):
    for j in range(1,N+1):
        sums[i][j] += board[i][j]
        sums[i][j] += board[j][i]

nums = [i for i in range(1,N+1)]
comb = []
for i in range(N):
    comb += list(itertools.combinations(nums,i))
ans = 10e9

def cal_sums(comb):
    comb_sum = 0
    #print(comb)
    for i in comb:
        for j in comb:
            if i == j:
                continue
            comb_sum += sums[i][j]
    return comb_sum

for i in range(len(comb)):
    if(comb[i]) and comb[-i]:
        ans = min(ans, abs(cal_sums(comb[i]) - cal_sums(comb[-i])))

print(ans//2)