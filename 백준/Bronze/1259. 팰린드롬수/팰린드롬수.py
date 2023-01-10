def check(num):
    half = len(num) // 2
    box = list(num)
    for i in range(half):
        if box[i] == box[-1]:
            box.pop()
        else:
            return "no"
    return "yes"

while True:
    number = input()
    if number == "0":
        break
    print(check(number))