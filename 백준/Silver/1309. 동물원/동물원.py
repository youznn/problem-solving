# 사자들이 붙어있으면 안 됨
# 사자를 배치하는 경우의 수?

# 위에 아무것도 없으면 해당 라인 양쪽 사자 가능 (경우의 수 3)
# 바로 위 오른쪽에 사자가 있으면 해당 라인에는 왼쪽에 사자 가능 (경우의 수 2)
# 바로 위 왼쪽에 사자가 있으면 해당 라인에는 오른쪽 사자 가능 (경우의 수 2)
# 아무것도 배치하지 않는 경우는 모두 가능
import sys
case = [1 for _ in range (3)]

N = int(sys.stdin.readline())

for i in range (N-1):
    temp = sum(case)
    case[1] += case[0]
    case[2] += case[0]
    case[0] = temp

print(sum(case) % 9901)


