import sys
input = sys.stdin.read

data = input().split()
N = int(data[0])
P = int(data[1])

# 스택을 관리
stack = [[] for _ in range(6)]
cnt = 0

index = 2
for i in range(N):
    nn = int(data[index])
    np = int(data[index + 1])
    index += 2
    
    nn -= 1  # 리스트 인덱스는 0부터 시작하므로 줄 번호를 1 감소

    # 현재 줄의 스택에서 프렛을 관리합니다.
    while stack[nn] and stack[nn][-1] > np:
        stack[nn].pop()
        cnt += 1

    if not stack[nn] or stack[nn][-1] != np:
        stack[nn].append(np)
        cnt += 1

print(cnt)
