import sys
sys.stdin = open("2580_input.txt")


def find_row(r, c):
    visited = [0 for _ in range(10)]
    for i in range(9):
        if i == c:
            continue
        if board[r][i]:
            visited[board[r][i]] = 1
        else:
            return 0
    for i in range(1, 10):
        if not visited[i]:
            return i

def find_col(r, c):
    visited = [0 for _ in range(10)]
    for i in range(9):
        if i == r:
            continue
        if board[i][c]:
            visited[board[i][c]] = 1
        else:
            return 0
    for i in range(1, 10):
        if not visited[i]:
            return i

def find_square(r, c):
    visited = [0 for _ in range(10)]
    sr = (r//3) * 3
    sc = (c//3) * 3
    for nr in range(sr, sr+3):
        for nc in range(sc, sc+3):
            if nr == r and nc == c:
                continue
            if board[nr][nc]:
                visited[board[nr][nc]] = 1
            else:
                return 0
    for i in range(1, 10):
        if not visited[i]:
            return i

board = []
for _ in range(9):
    board.append(list(map(int, input().split())))

stack = []
for r in range(9):
    for c in range(9):
        if not board[r][c]:
            stack.append((r, c))
# print(stack)

while stack:
    r, c = stack.pop(0)
    # print(r, c)
    # for line in board:
    #     print(line)
    val = find_row(r, c)
    if val:
        board[r][c] = val
        continue

    val = find_col(r, c)
    if val:
        board[r][c] = val
        continue

    val = find_square(r, c)
    if val:
        board[r][c] = val
        continue
    stack.append((r, c))

for line in board:
    print(' '.join(map(str, line)))