k = int(input())
conditions = list(input().split())

visited = [0 for _ in range (10)]
stack = []

idx = 0
plag = 0


def find_small(curr, idx = 0):
    global conditions, stack
    if curr and len(curr) == k+1:
        stack.append(curr[:])
        return
    for i in range(10):
        if i not in curr and conditions[idx] == ">" and curr[-1] > i:
            curr.append(i)
            find_small(curr, idx+1)
            curr.pop()
        elif i not in curr and conditions[idx] == "<" and curr[-1] < i:
            curr.append(i)
            find_small(curr, idx+1)
            curr.pop()


for i in range(10):
    find_small([i])

print(''.join(map(str,stack[-1])))
print(''.join(map(str,stack[0])))














