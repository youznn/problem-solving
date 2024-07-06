before_star = ['***', '* *', '***']
sections = [[] for _ in range(9)]

N = int(input())
curr = 3
def make_star(n):
    curr_star = [[] for _ in range(n)]
    for i in range(9):
        if i != 4:
            sections[i] = before_star
        else:
            sections[i] = [(' '*(n//3)) for _ in range(n//3)]
    #섹션 이어붙이기
    for i in range(3):
        section = sections[i]
        for j in range(len(section)):
            curr_star[j] += section[j]
    for i in range(3):
        section = sections[i + 3]
        for j in range(len(section)):
            curr_star[j + len(section)] += section[j]
    for i in range(3):
        section = sections[i + 6]
        for j in range(len(section)):
            curr_star[j + len(section)*2] += section[j]

    return curr_star
n = 9
ans = before_star
if N == 9:
    ans = make_star(9)
    
while n < N:
    before_star = make_star(n)
    ans = make_star(n*3)
    n *=3

for i in ans:
    for j in i:
        print(j,end="")
    print()