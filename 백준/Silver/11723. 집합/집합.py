from sys import stdin

n = int(input())
dic = {}

for i in range (n):
    command = stdin.readline()
    command = command[:]
    if command[:3] == "all":
        dic = {i:1 for i in range (1,21)}
    elif command[:5] == "empty":
        dic = {}
    else:
        command, x = command.split()
        x = int(x)
        if command == "add":
            if x not in dic:
                dic[x] = 1
        elif command == "remove":
            dic.pop(x,None)
        elif command == "check":
            if x in dic:
                print(1)
            else:
                print(0)
        elif command == "toggle":
            if x in dic:
                dic.pop(x)
            else:
                dic[x] = 1
