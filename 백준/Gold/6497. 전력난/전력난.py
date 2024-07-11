#MST
#무조건 최소 간선만을 사용하여 사이클을 형성하는지 확인하기
#n-1개 간선이 만들어졌으면 끝

#부모 노드를 찾는 find 함수

import sys
input = sys.stdin.readline

while True:
    V,E = map(int, input().split())
    if V == E == 0:
        break
    kruskal = []
    weight = 0

    for i in range(E):
        a, b, w = map(int,input().split())
        kruskal.append((a,b,w))
        weight += w


    kruskal.sort(key=lambda x: x[2])
    parent = [i for i in range(V+1)]
    weight_sum = 0
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(a,b):
        a = find(a)
        b = find(b)

        if a > b:
            parent[a] = b
        else:
            parent[b] = a


    for edge in kruskal:
        a, b, w = edge
        if find(a) != find(b):
            union(a,b)
            weight_sum += w






    print(weight - weight_sum)
