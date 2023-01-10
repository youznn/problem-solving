ans_row1 = "WBWBWBWB"
ans_row2 = "BWBWBWBW"

ans1 = [ans_row1,ans_row2,ans_row1,ans_row2,ans_row1,ans_row2,ans_row1,ans_row2]
ans2 = [ans_row2,ans_row1,ans_row2,ans_row1,ans_row2,ans_row1,ans_row2,ans_row1]

n_row, n_col = map(int,input().split())

arr = []
for i in range(n_row):
    arr.append(input())

def compare (array, ans):
    num = 0
    for j in range(8):
        for k in range(8):
            if array[j][k] != ans[j][k]:
                num += 1
    return num


min = compare(arr[:8][:8],ans1)
for i in range(n_col - 7):
    for j in range(n_row - 7):
        arr2 = []
        for k in range (8):
            arr2.append(arr[j+k][i:i+8])
        if min > compare(arr2,ans1):
            min = compare(arr2,ans1)
        if min > compare(arr2, ans2):
            min = compare(arr2, ans2)

print(min)

