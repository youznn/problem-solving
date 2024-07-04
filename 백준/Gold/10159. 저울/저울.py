#그래프탐색
from collections import deque
N = int(input())
M = int(input())

dic = {} #더 무거운거
reverse_dic = {} #더 가벼운거

for i in range (N+1):
    dic[i] = []
    reverse_dic[i] = []


for i in range (M):
    a , b = map(int,input().split())
    dic[a] = dic.get(a,[]) + [b]
    reverse_dic[b] = reverse_dic.get(b,[]) + [a]

arr = [N for _ in range(N+1)]

def bfs(start, graph):
    visited = [0 for _ in range(N + 1)]
    q = deque()
    q.append(start)
    visited[start] = 1
    while (q):
        node = q.popleft()
        if graph[node]:
            for next_node in graph[node]:
                if visited[next_node] == 0:
                    visited[next_node] = 1
                    q.append(next_node)
    return sum(visited)

for i in range (1,N+1):
    bigger = bfs(i,dic)
    smaller = bfs(i,reverse_dic)
    print(N+1-bigger-smaller)



