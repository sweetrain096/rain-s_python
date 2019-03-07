import sys
sys.stdin = open("1987_input.txt")

def iswall(row, col):
    if row < 0 or row >= r or col < 0 or col >= c:
        return True
def dfs(node, visited):
    global cnt, result
    row, col = node[0], node[1]
    alpha = ord(board[row][col]) - 65
    visited[alpha] = 1
    cnt += 1
    result = max(cnt, result)

    for plus_r, plus_c in deg:
        if not iswall(row + plus_r, col + plus_c):
            now_alpha = ord(board[row + plus_r][col + plus_c]) - 65
            if not visited[now_alpha]:
                dfs([row + plus_r, col + plus_c], visited)
    cnt -= 1
    visited[alpha] = 0


r, c = map(int, input().split())
board = []
visited = [0 for _ in range(26)]
deg = [[-1, 0], [1, 0], [0, -1], [0, 1]]
for i in range(r):
    tmp = []
    for j in input():
        tmp.append(j)
    board.append(tmp)

# print(board)

cnt, result = 0, 0
dfs([0, 0], visited)
print(result)