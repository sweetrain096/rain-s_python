import sys
sys.stdin = open("4875_input.txt")

def start():
    for row in range(n-1, -1, -1):
        for col in range(n):
            if maze[row][col] == 2:
                return row, col
def end():
    for row in range(n):
        for col in range(n):
            if maze[row][col] == 3:
                return row, col



def make_candidate():
    d_row = [1, -1, 0, 0]
    d_col = [0, 0, 1, -1]
    return 4, d_row, d_col


def backtrack(stack, k, row, col):
    global end_row, end_col
    visited[row][col] = 1


    if row == end_row and col == end_col:
        result.append(1)



    else:
        k += 1
        ncands, d_row, d_col = make_candidate()
        for i in range(ncands):
            # print('new_row', row + d_row[i], 'new_col', col + d_col[i])
            if row + d_row[i] >= 0 and row + d_row[i] < n and col + d_col[i] >= 0 and col + d_col[i] < n:
                if maze[row + d_row[i]][col + d_col[i]] != 1 and visited[row + d_row[i]][col + d_col[i]] == 0:
                    backtrack(stack, k, row + d_row[i], col + d_col[i])







for tc in range(int(input())):
    n = int(input())
    maze = []
    for i in range(n):
        tmp = []
        for j in input():
            tmp.append(int(j))
        maze.append(tmp)


    # for i in maze:
    #     print(i)

    start_row, start_col = start()
    # print('start', maze[start_row][start_col], start_row, start_col)

    end_row, end_col = end()
    # print('end', maze[end_row][end_col], end_row, end_col)


    stack = [0] * 100
    visited = [[0 for _ in range(n)] for _ in range(n)]
    visited[start_row][start_col] = 1
    result = []



    backtrack(stack, 0, start_row, start_col)
    if not result:
        result.append(0)
    print(f"#{tc + 1} {result[0]}")





