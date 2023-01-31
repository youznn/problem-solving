import sys

box = []
n = int(input())
for _ in range (n):
    box.append(int(input()))

for i in sorted(box):
    print(i)
