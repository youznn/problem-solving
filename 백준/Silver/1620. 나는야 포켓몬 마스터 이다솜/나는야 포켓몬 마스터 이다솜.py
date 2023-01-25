from sys import stdin

n, m = map(int,(input().split()))
dic = {}
dic2 = {}
for i in range (1,n+1):
    pokemon = stdin.readline().strip()
    dic[pokemon] = str(i)

dic2 = {str(k+1): v for k, v in enumerate(dic)}
for j in range (m):
    ans = stdin.readline().strip()
    if ans in dic.keys():
        print(dic[ans])
    else:
        print(dic2[ans])

