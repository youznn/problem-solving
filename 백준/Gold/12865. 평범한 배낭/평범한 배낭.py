arr = []
N , K = list(map(int,input().split()))
for _ in range (N):
    arr.append(list(map(int,input().split())))


dp = [[0 for _ in range (K+1)] for _ in range(N+1)]


for i in range(1,N+1):
    for j in range(1,K+1):
        w = arr[i-1][0]
        v = arr[i-1][1]
        if w > j:
            dp[i][j] = dp[i-1][j]
        else:
            if v + dp[i-1][j-w] > dp[i-1][j]:
                dp[i][j] = v + dp[i-1][j-w]
            else:
                dp[i][j] = dp[i-1][j]

print(dp[-1][-1])