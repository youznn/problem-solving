# 2xn 타일링
# 홀,짝이 나뉠 것 같다
# 그냥 규칙 찾는 것 같은데...
# combination 사용해야 할 것 같으니까 factorial을 dp로 저장해두고 쓰기? 어차피 1000이니까.

# factorial
fac = [1]
for i in range(1, 1001):
    fac.append(fac[i - 1] * i)

n = int(input())

cnt = 0
for i in range(n // 2 + 1):
    cnt += int(fac[n-i] // (fac[i] * fac[n-2*i]))

print(cnt % 10007)