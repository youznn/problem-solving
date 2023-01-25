from sys import stdin

a, b = map(list,input().split())
a = a[::-1] #문자열 뒤집기
b = b[::-1]

a = int("".join(a))
b = int("".join(b))
print(max(a,b))