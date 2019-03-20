import sys
sys.stdin = open("6603_input.txt")

def dfs(start):
    now = data[start]
    visited[now] = 1
    result.append(now)
    # print(result)
    if len(result) == 6:
        print(' '.join(map(str, result)))
    for i in range(start + 1, total + 1):
        if not visited[data[i]]:
            dfs(i)
    visited[now] = 0
    result.pop()


while True:
    data = list(map(int, input().split()))
    total = data[0]
    if not total:
        break

    result = []

    for start in range(1, total - 6 + 2):
        visited = [0] * 50
        dfs(start)
    print()




# import sys
# sys.stdin = open("6603_input.txt")
#
# def dfs(start):
#     start = data[start]
#     visited[start] = 1
#     result.append(start)
#     # print(result)
#     if len(result) == 6:
#
#         print(result)
#     for i in range(start + 1, total + 1):
#         if not visited[data[i]]:
#             dfs(i)
#     visited[start] = 0
#     result.pop()
#
#
# while True:
#     data = list(map(int, input().split()))
#     total = data[0]
#     if not total:
#         break
#     print(data)
#     result = []
#     visited = [0] * 50
#     for start in range(1, total - 6 + 2):
#         dfs(start)
#
#
# # def dfs(start, visited):
# #     now = data[start]
# #     print(now)
# #     if not visited[now]:
# #         print(visited)
# #         visited[now] = 1
# #         result.append(now)
# #
# #         if len(result) == 6:
# #             print("result", result)
# #             return
# #
# #         for i in range(start, total + 1):
# #             next = data[i]
# #             if not visited[next] and len(result) < 6:
# #
# #                 # print(' '.join(map(str, result)))
# #                 print(result)
# #
# #                 dfs(i, visited)
# #         t = result.pop()
# #         visited[t] = 0
# #         print("pop", t, result)