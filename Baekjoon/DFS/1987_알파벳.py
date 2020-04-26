import sys
sys.stdin = open("1987_input.txt")

deg = [[-1, 0], [1, 0], [0, -1], [0, 1]]
def is_wall(row, col):
    if row < 0 or row >= r or col < 0 or col >= c:
        return True
def dfs(node, visited, cnt):
    global result
    row, col = node[0], node[1]
    alpha = ord(board[row][col]) - 65

    visited[alpha] = 1
    cnt += 1
    result = max(cnt, result)

    for dr, dc in deg:
        nr = row + dr
        nc = col + dc
        if not is_wall(nr, nc):
            now_alpha = ord(board[nr][nc]) - 65
            if not visited[now_alpha]:
                dfs([nr, nc], visited, cnt)
    cnt -= 1
    visited[alpha] = 0


r, c = map(int, input().split())
board = []
visited = [0 for _ in range(26)]
for i in range(r):
    board.append(sys.stdin.readline()[:-1])

# print(board)

result = 0
dfs([0, 0], visited, 0)
print(result)