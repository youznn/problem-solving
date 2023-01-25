from sys import stdin
dic = {}
for i in range(10):
    n = int(input())
    if n % 42 not in dic:
        dic[n%42] = 1

print(len(dic))