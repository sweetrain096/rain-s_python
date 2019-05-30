import sys
sys.stdin = open("4615_input.txt")

def iswall(row, col):
    if row < 0 or row >= n or col < 0 or col >= n:
        return True

def find(r, c, stone):
    if stone == 1:
        stone2 = 2
    else:
        stone2 = 1
    board[r][c] = stone
    for pr, pc in deg:
        new_r, new_c = r + pr, c + pc
        # print(new_r, new_c)
        flag = False
        if not iswall(new_r, new_c) and board[new_r][new_c] == stone2:
            while True:
                if not iswall(new_r, new_c):
                    if board[new_r][new_c] == 0:
                        break
                    elif board[new_r][new_c] == stone:
                        flag = True
                        break
                    new_r += pr
                    new_c += pc
                else:
                    break

            if flag:
                new_r, new_c = r + pr, c + pc
                while True:
                    # for i in board:
                    #     print(i)
                    # print()
                    if not iswall(new_r, new_c):
                        if board[new_r][new_c] == stone:
                            break
                        board[new_r][new_c] = stone
                        new_r += pr
                        new_c += pc
                    else:
                        break
    return

deg = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
for tc in range(int(input())):
    n, m = map(int, input().split())
    board = [[0 for _ in range(n)] for _ in range(n)]
    board[n // 2 - 1][n // 2 - 1] = 2
    board[n // 2 - 1][n // 2] = 1
    board[n // 2][n // 2 - 1] = 1
    board[n // 2][n // 2] = 2

    for i in range(m):
        col, row, stone = map(int, input().split())
        row, col = row - 1, col - 1
        find(row, col, stone)

    black, white = 0, 0
    for i in board:
        for j in i:
            if j == 1:
                black += 1
            elif j == 2:
                white += 1

    print("#{} {} {}".format(tc + 1, black, white))