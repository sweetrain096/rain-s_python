import sys
sys.stdin = open("4050_input.txt")

for tc in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    data = sorted(arr, reverse=True)
    Sum = 0
    for i in range(n):
        if not (i + 1) % 3:
            continue
        Sum += data[i]

    print(f"#{tc + 1} {Sum}")