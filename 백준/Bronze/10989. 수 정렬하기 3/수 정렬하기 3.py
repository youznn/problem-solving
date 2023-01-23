from sys import stdin
n = int(stdin.readline())
dic = {}
for i in range(n):
    num = int(stdin.readline())
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1

dic = sorted(dic.items())

for i in dic:
    for j in range(i[1]):
        print(i[0])