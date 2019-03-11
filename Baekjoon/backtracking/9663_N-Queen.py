import sys
sys.stdin = open("9663_input.txt")

def iswall(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True

def is_not_safe(now_r, now_c):
    for pr, pc in deg:
        while True:
            now_r += pr
            now_c += pc
            if not iswall(now_r, now_c) and board[now_r][now_c]:
                return False
            if iswall(now_r, now_c):
                break

def dfs(r, c, cnt):
    global result
    if not board[r][c]:
        board[r][c] = 1
        cnt += 1
    if cnt == n:
        result += 1
        print(result)
        return

    for row in range(r + 1, n):
        for col in range(c, n):

            for i in board:
                print(i)
            print()
            if not is_not_safe(row, col):
                dfs(row, col, cnt)
    # board[r][c] = 0






deg = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
n = int(input())
board = [[0 for _ in range(n)] for _ in range(n)]
result = 0

dfs(0, 0, 0)

print(result)