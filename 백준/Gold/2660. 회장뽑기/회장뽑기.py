#bfs!
#가장 점수가 낮은 사람이 회장 후보임. 만약에 min보다 값이 작을 경우 bfs 중단하기

import sys
from collections import deque


N = int(input())
members = [[] for _ in range(N+1)]
min_score = 10e9 #후보 점수
ans = [] #후보 넘버

while True:
    a, b = map(int,sys.stdin.readline().split())
    if a == b == -1:
        break
    members[a].append(b)
    members[b].append(a)


#bfs
def bfs(target_mem):
    visited = [0 for _ in range (N+1)]
    score = [0 for _ in range(N+1)]
    q = deque()
    q.append(target_mem)
    visited[target_mem] = 1
    while q:
        curr_mem = q.popleft()
        for next_mem in members[curr_mem]:
            if visited[next_mem] == 0:
                visited[next_mem] = 1
                q.append(next_mem)
                score[next_mem] = score[curr_mem] + 1

    return max(score)



#회장 후보 고르기
for i in range (1,N+1):
    if bfs(i) < min_score:
        min_score = bfs(i)
        ans = [i]
    elif bfs(i) == min_score:
        ans.append(i)

print(min_score, len(ans))
ans.sort()
for a in ans:
    print(a, end= " ")
    