import sys
sys.stdin = open("5097_input.txt")

for tc in range(int(input())):
    n, m = map(int, input().split())
    data = list(input().split())
    for i in range(m):
        data.append(data.pop(0))
    print(f"#{tc + 1} {data[0]}")
