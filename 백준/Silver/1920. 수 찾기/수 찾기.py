n = int(input())
n_list = list(map(int,input().split()))
n_list.sort()
m = int(input())
m_list = list(map(int,input().split()))


def bs(num):
    head = 0
    tail = n - 1
    while head <= tail:
        mid = (head + tail) // 2
        if n_list[mid] == num:
            return 1
        elif n_list[mid] < num:
            head = mid+1
        elif n_list[mid] > num:
            tail = mid - 1
    return 0


for i in m_list:
    print(bs(i))