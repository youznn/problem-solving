from sys import stdin

n, m = map(int,(stdin.readline().split()))
tree_list = list(map(int, stdin.readline().split()))
tree_list.sort(reverse=True)

start = 0
end = tree_list[0]
mid = end

while start <= end:
    ans = 0
    for tree in tree_list:
        if tree > mid:
            ans += tree - mid
        else:
            break
    if ans >= m: #자르는 부분을 늘려야 함
        start = mid + 1
    else: #자르는 부분을 줄여야 함
        end = mid - 1
    mid = (start + end) // 2

print(mid)