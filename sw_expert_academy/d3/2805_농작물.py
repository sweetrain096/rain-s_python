import sys
sys.stdin = open("2805_input.txt")

for tc in range(int(input())):
    n = int(input())
    Map = [input() for _ in range(n)]
    # print(Map)
    result = 0
    for i in range(n // 2):
        for j in range(n//2 - i, n // 2 + i + 1):
            result += int(Map[i][j])
            result += int(Map[n - i - 1][j])
    for i in range(n):
        result += int(Map[n//2][i])

    print(f"#{tc + 1} {result}")