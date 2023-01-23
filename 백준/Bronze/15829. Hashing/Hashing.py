from sys import stdin
n = stdin.readline()
arr = stdin.readline()
sum = 0
j = 0
for i in range(len(arr)-1):
    sum += (ord(arr[i])-96) * 31 ** i
    j += 1

sum %= 1234567891
print(int(sum))