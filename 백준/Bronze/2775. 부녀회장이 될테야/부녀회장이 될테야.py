from sys import stdin

num = int(stdin.readline())


def residents(k, n):
    if n == 2:
        return k+2
    elif k == 1:
        return n*(n+1)//2
    else:
        return residents(k,n-1) + residents(k-1,n)

for i in range (num):
    k = int(stdin.readline()) #k층
    n = int(stdin.readline()) #n호
    if k == 0:
        print(n)
    elif n == 1:
        print(1)
    else:
        print(residents(k,n))