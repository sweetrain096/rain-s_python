import sys
sys.stdin = open("5105_input.txt")

def BFS(g, start, depth):
    global n
    deg = [[0, -1], [-1, 0], [0, 1], [1, 0]]
    Q.append(start)
    visited[start[0]][start[1]] = 1
    check = start

    while Q:
        # print("Q", Q)
        t = Q.pop(0)
        # print('t', t)

        for i in range(4):
            row, col = t[0] + deg[i][0], t[1] + deg[i][1]
            if row >= 0 and row < n and col >= 0 and col < n:
                if g[row][col] == '3':
                    return depth
                # print(t[0] + deg[i][0], t[1] + deg[i][1])
                if g[row][col] != '1' and not visited[row][col]:
                    Q.append([row, col])
                    visited[row][col] = 1
        if Q and t == check:
            depth += 1
            check = Q[-1]
    if not Q:
        return 0


for tc in range(int(input())):
    n = int(input())
    maze = []
    Q = []
    visited = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        tmp = []
        cnt = 0
        for j in input():
            tmp.append(j)
            if j == "2":
                start = [i, cnt]
            cnt += 1
        maze.append(tmp)



    # for i in maze:
    #     print(i)
    # print(start)

    result = BFS(maze, start, 0)
    print("#{} {}".format(tc + 1, result))