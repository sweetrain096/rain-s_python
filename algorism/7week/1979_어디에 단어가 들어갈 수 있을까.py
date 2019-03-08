import sys
sys.stdin = open("1979_input.txt")

for tc in range(int(input())):
    n, k = map(int, input().split())
    base = []
    for i in range(n):
        base.append(list(map(int, input().split())))
    result = 0
    for i in range(n):
        plus_row, plus_col = 0, 0
        for j in range(n):
            if base[i][j]:
                plus_row += 1
            else:
                if plus_row == k:
                    result += 1
                plus_row = 0
            if base[j][i]:
                plus_col += 1
            else:
                if plus_col == k:
                    result += 1
                plus_col = 0
        if plus_row == k:
            result += 1
        if plus_col == k:
            result += 1
    print("#{} {}".format(tc + 1, result))