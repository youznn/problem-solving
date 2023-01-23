from math import pow
from sys import stdin
n = stdin.readline()
arr = stdin.readline()
sum = 0
j = 0
for i in arr[:-1]:
    sum += (ord(i)-96) * pow(31,j)
    j += 1

print(int(sum))