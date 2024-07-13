N = int(input())
words = [[] for _ in range(N)]
alphabets = [0 for i in range (26)]
for i in range(N):
    words[i] = input()

#모든 words에서 해당 알파벳이 등장하는 자릿수 모두 구하기

for word in words:
    for i in range(len(word)-1,-1,-1):
        digit = len(word) - i - 1
        alpha_idx = ord(word[i]) - 65 # A-0 B-1 로 인덱스 변환
        alphabets[alpha_idx] += pow(10, digit)

#다시 정렬 후 계산
alphabets.sort(reverse=True)
ans = 0
for i in range (10):
    ans += alphabets[i] * (9-i)
print(ans)