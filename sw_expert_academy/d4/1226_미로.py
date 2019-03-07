import sys
sys.stdin = open("1226_input.txt")

def iswall(r, c):
    if r < 0 or r >= 16 or c < 0 or c >= 16:
        return True

def dfs(node):
    row, col = node[0], node[1]
    # visited[row][col] = 1

    for plus_r, plus_c in deg:
        new_r, new_c = row + plus_r, col + plus_c
        if [new_r, new_c] == end:
            maze[new_r][new_c] = 999
        if not iswall(new_r, new_c) and not maze[new_r][new_c]:
            maze[new_r][new_c] = 9
            dfs([new_r, new_c])



for test_case in range(10):
    tc = int(input())
    maze = []
    visited = [[0 for _ in range(16)] for _ in range(16)]
    deg = [[-1, 0], [1, 0], [0, -1], [0, 1]]

    start, end = [0, 0], [0, 0]
    for i in range(16):
        tmp = []
        cnt = 0
        for j in input():
            tmp.append(int(j))
            if j == '2':
                start = [i, cnt]
            elif j == '3':
                end = [i, cnt]
            cnt += 1
        maze.append(tmp)



    # print(start, end)
    dfs(start)
    if maze[end[0]][end[1]] == 999:
        print("#{} 1".format(tc))
    else:
        print("#{} 0".format(tc))
    #
    # for i in maze:
    #     print(i)