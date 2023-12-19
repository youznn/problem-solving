import sys

com_num = int(input())
link_num = int(input())

dic = {}
for i in range(link_num):
    a, b = map(int, sys.stdin.readline().split())
    dic[a] = dic.get(a, []) + [b]
    dic[b] = dic.get(b, []) + [a]


def dfs(s, dict):
    stack_dfs= []
    visited = set()
    start_node = s
    stack_dfs.append(start_node)
    if s not in dic.keys():
        return [s]
    while stack_dfs:
        node = stack_dfs.pop()
        if node not in visited:
            visited.add(node)
            stack_dfs.extend(dict[node])
    return visited

print(len(dfs(1,dic))-1)
