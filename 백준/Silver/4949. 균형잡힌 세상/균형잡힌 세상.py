while True:
    s = input()
    stack = []
    if s == ".":
        break
    ans = True
    for n in s:
        if n == "[":
            stack.append(1)
        elif n == "]":
            if stack and stack[-1] == 1:
                stack.pop()
            else:
                ans = False
        elif n == "(":
            stack.append(2)
        elif n == ")":
            if stack and stack[-1] == 2:
                stack.pop()
            else:
                ans = False
    if not stack and ans == True:
        print("yes")
    else:
        print("no")



