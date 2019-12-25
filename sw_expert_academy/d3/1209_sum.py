import sys
sys.stdin = open("1209_input.txt")

for tc in range(10):
    tn = int(input())
    arr = []
    Max = 0
    for i in range(100):
        arr.append(list(map(int, input().split())))
        if sum(arr[i]) > Max:
            Max = sum(arr[i])

    for c in range(100):
        temp_sum = 0
        for r in range(100):
            temp_sum += arr[r][c]
        if temp_sum > Max:
            Max = temp_sum

    temp_sum = 0
    for i in range(100):
        temp_sum += arr[i][i]
    if temp_sum > Max:
        Max = temp_sum

    temp_sum = 0
    for i in range(100):
        temp_sum += arr[i][-1-i]
    if temp_sum > Max:
        Max = temp_sum


    print(f"#{tn} {Max}")
