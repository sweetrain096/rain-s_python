import sys
sys.stdin = open("9663_input.txt")

#### 벽세우기

def iswall(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True

def make_wall(now_r, now_c, board):
    # print(now_r, now_c)
    for pr, pc in deg:
        row, col = now_r, now_c
        while True:
            row += pr
            col += pc
            # print(row, col)
            if not iswall(row, col) and board[row][col]:
                board[row][col] = 0
            if iswall(row, col):
                break
    return True

def dfs(r, c, board):
    global result
    if board[r][c]:
        visited[r] = 1
        make_wall(r, c, board)

    for i in board:
        print(i)
    print()

    # if sum(visited) == n:
    #     result += 1
    #     # for i in board:
    #     #     print(i)
    #     # print()
    #     # print("result", result)
    #     # return
    #
    # for row in range(r + 1, n):
    #     for col in range(n):
    #         if row and not visited[row - 1]:
    #             break
    #
    #         if is_safe(row, col, board):
    #             dfs(row, col, board)
    #
    #         for i in board:
    #             print(i)
    #         print()
    #
    # # print('last', r, c)
    # board[r][c] = 0
    # visited[r] = 0



# deg = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
deg = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
n = int(input())
board = [[1 for _ in range(n)] for _ in range(n)]
result = 0
visited = [[1 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in board:
        print(j)
    print()
    dfs(0, i, visited)


print(result)





#### 기본 for 4개
# def iswall(r, c):
#     if r < 0 or r >= n or c < 0 or c >= n:
#         return True
#
# def is_safe(now_r, now_c):
#     # print(now_r, now_c)
#     for pr, pc in deg:
#         row, col = now_r, now_c
#         while True:
#             row += pr
#             col += pc
#             # print(row, col)
#             if not iswall(row, col) and board[row][col]:
#                 return False
#             if iswall(row, col):
#                 break
#     return True
#
# def dfs(r, c):
#     global result
#     if not board[r][c]:
#         board[r][c] = 1
#         visited[r] = 1
#     if sum(visited) == n:
#         result += 1
#         # for i in board:
#         #     print(i)
#         # print()
#         # print("result", result)
#         # return
#
#     for row in range(r + 1, n):
#         for col in range(n):
#             if row and not visited[row - 1]:
#                 break
#
#             if is_safe(row, col):
#                 dfs(row, col)
#
#             for i in board:
#                 print(i)
#             print()
#
#     # print('last', r, c)
#     board[r][c] = 0
#     visited[r] = 0
#
#
#
# deg = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
# n = int(input())
# board = [[0 for _ in range(n)] for _ in range(n)]
# result = 0
# visited = [0] * n
#
# for i in range(n):
#     dfs(0, i)
#
# print(result)


#### 4 for
# def iswall(r, c):
#     if r < 0 or r >= n or c < 0 or c >= n:
#         return True
#
# def is_safe(now_r, now_c):
#     # print(now_r, now_c)
#     for pr, pc in deg:
#         row, col = now_r, now_c
#         while True:
#             row += pr
#             col += pc
#             # print(row, col)
#             if not iswall(row, col) and board[row][col]:
#                 return False
#             if iswall(row, col):
#                 break
#     return True
#
# def dfs(r, c):
#     global result
#     if not board[r][c]:
#         board[r][c] = 1
#         visited[r] = c + 1
#     if not visited.count(0):
#         result += 1
#         # for i in board:
#         #     print(i)
#         # print()
#         # print("result", result)
#         # return
#
#     for row in range(r + 1, n):
#         for col in range(n):
#             if row and not visited[row - 1]:
#                 break
#
#             if is_safe(row, col):
#                 dfs(row, col)
#
#             for i in board:
#                 print(i)
#             print()
#
#     # print('last', r, c)
#     board[r][c] = 0
#     visited[r] = 0
#
#
#
# deg = [[0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1]]
# n = int(input())
# board = [[0 for _ in range(n)] for _ in range(n)]
# result = 0
# visited = [0] * n
#
# for i in range(n):
#     dfs(0, i)
#
# print(result)




