from sys import stdin
n, k = map(int,stdin.readline().split())

def pac(num):
    if num == 0:
        return 1
    else:
        return num*pac(num-1)

ans = int(pac(n) / ((pac(n-k)) * pac(k)))
print(ans)