from sys import stdin
n = int(input())
num_list = []
num_dic = {}
for i in range (n):
    num = int(stdin.readline())
    num_list.append(num)
    if num not in num_dic:
        num_dic[num] = 1
    else:
        num_dic[num] += 1
num_list.sort()
num_dic = dict(sorted(num_dic.items()))
print(round(sum(num_list)/n))
print(num_list[n//2])
cnt = 0
idx = 0
for i in num_dic:
    if num_dic[i] == max(num_dic.values()):
       cnt += 1
       idx = i
    if cnt == 2:
        break

print(idx)
print(num_list[-1] - num_list[0])