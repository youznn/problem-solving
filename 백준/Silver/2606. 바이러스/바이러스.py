import sys

com_num = int(input())
link_num = int(input())

dic = {}
for i in range (link_num):
    a,b = map(int,sys.stdin.readline().split())
    dic[a] = dic.get(a,[]) + [b]
    dic[b] = dic.get(b,[]) + [a]

def dfs(dic, v, visited= []):
    visited.append(v)
    for node in dic[v]:
        if node not in visited:
            dfs(dic , node , visited)
    return visited

print(len(dfs(dic,1))-1)
