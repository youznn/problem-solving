import sys

t = int(input())

dic ={1:[[1]],2:[[2],[1,1]],3:[[1,1,1],[1,2],[2,1],[3]]}
for i in range (4,12):
    for j in dic[i-1]:
        dic[i] = dic.get(i,[])+[j + [1]]
    for j in dic[i-2]:
        if [j+[1]] not in dic[i]:
            dic[i] = dic.get(i,[])+[j + [1]]
    for j in dic[i-3]:
        if [j + [1]] not in dic[i]:
            dic[i] = dic.get(i,[])+[j + [1]]

for n in range (t):
    n = int(sys.stdin.readline())
    print(len(dic[n]))



