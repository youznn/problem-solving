n = int(input())

meetings = []
for _ in range(n):
    a, b = map(int, input().split())
    meetings.append((a, b))

# 회의가 끝나는 시간을 기준으로 오름차순 정렬
meetings.sort(key=lambda x: (x[1], x[0]))

end_time = 0
cnt = 0

for meeting in meetings:
    start, end = meeting
    # 이전 회의가 끝난 시간 이후에 시작하는 회의인 경우
    if start >= end_time:
        end_time = end
        cnt += 1

print(cnt)
