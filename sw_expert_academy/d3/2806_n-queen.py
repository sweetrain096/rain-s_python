import sys
sys.stdin = open("2806_input.txt")


def is_right(r, c):
    for i in range(r):
        # for line in Map:
        #     print(line)
        # print()

        if Map[i][c]:
            return False
    # 좌
    for i in range(r, -1, -1):
        nc = c - (r - i)
        if nc < 0:
            break
        if Map[i][nc]:
            return False
    # 우
    for i in range(r, -1, -1):
        nc = c + (r - i)
        if nc >= n:
            break
        if Map[i][nc]:
            return False
    return True

def backtracking(row, col):
    global cnt
    if row == n-1:
        cnt += 1
        return
    Map[row][col] = 1
    for c in range(n):
        if is_right(row + 1, c):
            backtracking(row + 1, c)

    Map[row][col] = 0

for tc in range(int(input())):
    n = int(input())
    cnt = 0

    for i in range(n):
        Map = [[0 for _ in range(n)] for _ in range(n)]
        backtracking(0, i)


    print(f"#{tc + 1} {cnt}")
