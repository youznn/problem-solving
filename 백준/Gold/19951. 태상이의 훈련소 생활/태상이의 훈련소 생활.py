import sys
input = sys.stdin.readline

N, M = list(map(int,input().split()))

height = [0] + list(map(int,input().split()))
total = [0 for _ in range(N+2)]

for i in range(M):
    a, b, k = list(map(int,input().split()))
    total[a] += k
    total[b+1] -= k

#누적합 구하기
for i in range(1,N+1):
    total[i] += total[i-1]

    height[i] += total[i]


for i in range(1,N+1):
    print(height[i], end=" ")