import sys
sys.stdin = open("3503_input.txt")

for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    data = sorted(arr, reverse=True)
    diff = data[0] - data[1]

    for i in range(n - 2):
        if data[i] - data[i + 2] > diff:
            diff = data[i] - data[i + 2]
    if data[-2] - data[-1] > diff:
        diff = data[-2] - data[-1]


    print(f"#{tc + 1} {diff}")
