import sys
sys.stdin = open("5789_input.txt")

for tc in range(int(input())):
    n, q = map(int, input().split())
    arr = [0 for _ in range(n)]
    data = []
    for i in range(1, q + 1):
        l, r = map(int, input().split())
        data.append([l, r, i])
    for i in range(len(data)):
        l, r, val = data[-i-1]
        for j in range(l - 1, r):
            if not arr[j]:
                arr[j] = val
    print(f"#{tc + 1} {' '.join(map(str, arr))}")