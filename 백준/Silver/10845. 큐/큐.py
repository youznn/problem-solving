import sys
num = int(input())
stack = []

for i in range(num):
    ord = sys.stdin.readline().strip()
    if ord[:4] == "push":
        stack.append(ord[5:])
    elif ord == "pop":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop(0))
    elif ord == "size":
        print(len(stack))
    elif ord == "empty":
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif ord == "front":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[0])
    elif ord == "back":
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])