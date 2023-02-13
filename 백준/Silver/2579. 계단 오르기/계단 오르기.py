import sys

n = int(input())
score_list= [0]
for _ in range (n):
    score = int(sys.stdin.readline())
    score_list.append(score)

dp = {0:0}
for i in range (1,n+1):
    if i == 1:
        dp[1] = score_list[1]
    elif i == 2:
        dp[2] = dp[1] + score_list[2]
    else:
        dp[i] = max(dp[i-2]+score_list[i], dp[i-3]+score_list[i]+score_list[i-1])

print(dp[n])