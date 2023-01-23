from sys import stdin
n = int(stdin.readline())
stack = []
ans = []
current = 1

for i in range(0,n):
    num = int(stdin.readline())
    while current <= num:
        stack.append(current)
        current += 1
        ans.append("+")
    if stack[-1] == num:
        stack.pop()
        ans.append("-")

if not stack:
    for a in ans:
        print(a)
else:
    print("NO")

