from sys import stdin


def count_money(money,money_list):
    cnt = 0
    for i in range (1,len(money_list)+1):
        left = money % money_list[-i]
        if left != money:
            cnt += money // money_list[-i]
            money = left
        if money == 0:
            break
    return cnt

n, k = map(int,(input().split()))
money_list = []
for i in range (n):
    money_list.append(int(stdin.readline()))

print(count_money(k,money_list))
