import sys
import itertools
from collections import deque
input = sys.stdin.readline

# 누적합 ???

T = int(input())
n = int(input())
list_A = list(map(int,input().split()))
m = int(input())
list_B = list(map(int,input().split()))

dic_A = {}
dic_B = {}

ans = 0

def part_sum(curr_list, len):
    sums = [0 for _ in range(len+1)]
    sums[0] = 0
    sums[1] = curr_list[0]
    dic = {}
    for i in range(2,len+1):
        sums[i] = sums[i-1] + curr_list[i-1]

    for i in range(len+1):
        for j in range(i+1, len+1):
            curr_sum = sums[j] - sums[i]
            if curr_sum not in dic:
                dic[curr_sum] = 1
            else:
                dic[curr_sum] += 1

    return dic

dic_A = part_sum(list_A,n)
dic_B = part_sum(list_B,m)

for sum_B in dic_B.keys():
    if T-sum_B in dic_A.keys():
        ans += dic_A[T-sum_B] * dic_B[sum_B]


print(ans)




