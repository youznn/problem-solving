from sys import stdin
dic = {}

_ = stdin.readline()
sang_list = list(map(int,stdin.readline().split()))
_ = stdin.readline()
card_list = list(map(int,stdin.readline().split()))
ans_list = []
#해시 사용하기!
for i in sang_list:
    if i not in dic:
        dic[i] = 1
    else:
        dic[i] += 1

for j in card_list:
    if j not in dic.keys():
        ans_list.append(0)
    else:
        ans_list.append(dic[j])

print(" ".join(map(str,ans_list)))
