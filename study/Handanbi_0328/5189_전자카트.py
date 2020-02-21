import sys
sys.stdin = open("5189_input.txt")

def find_min():
    tmp_sum = 0
    for i in range(n - 1):
        tmp_sum += data[a[i]][a[i + 1]]
    tmp_sum += data[a[-1]][a[0]]
    return tmp_sum

def perm(k):
    global result

    if n == k:
        result = min(find_min(), result)
        # print(a, result)
    else:
        for i in range(k, n):
            a[i], a[k] = a[k], a[i]
            perm(k + 1)
            a[i], a[k] = a[k], a[i]

# def perm(k, sum_data):
#     global result
#
#     if n == k:
#         result = min(result, sum_data)
#         print(tmp)
#         return
#     else:
#         for i in range(k, n):
#             data[i], data[k] = data[k], data[i]
#             perm(k + 1, sum_data + data[k][i])
#             data[i], data[k] = data[k], data[i]
#
#         for i in range(1, n):
#             if not tmp[i] and i != k:
#                 if tmp[k] and i == tmp[k] - 1:
#                     continue
#                 tmp[i] = k
#
#                 perm(k + 1, sum_data + data[k][i])
#                 tmp[i] = 0


for tc in range(int(input())):
    n = int(input())
    data = []
    tmp = [0] * n

    result = 99999999999
    for i in range(n):
        data.append(list(map(int, input().split())))
    a = [i for i in range(n)]
    perm(1)
    print("#{} {}".format(tc + 1, result))


# # def perm(k, sum_data):
# #     global result
# #
# #     if sum_data > result:
# #         return
# #     if n == k:
# #         print(tmp, sum_data)
# #         result = min(result, sum_data)
# #
# #         return
# #     else:
# #         for i in range(n):
# #             if not tmp[i] and i != k:
# #                 if tmp[k] and i == tmp[k] - 1:
# #                     continue
# #                 tmp[i] = k + 1
# #
# #                 perm(k + 1, sum_data + data[k][i])
# #                 tmp[i] = 0
#
#
# def dfs(num, sum_data, cnt):
#     global result
#
#     if cnt == n:
#         result = min(result, sum_data)
#         print(visited, sum_data)
#         return
#     else:
#         for i in range(n):
#             print("hi", i, visited, cnt)
#             if i != num and not visited[i]:
#                 visited[num] = 1
#                 print(num, i)
#                 dfs(i, sum_data + data[num][i], cnt + 1)
#                 visited[i] = 0
#     return
#
# for tc in range(int(input())):
#     n = int(input())
#     data = []
#     visited = [0] * n
#
#     result = 9999999
#     for i in range(n):
#         data.append(list(map(int, input().split())))
#     print(data)
#
#     dfs(0, 0, 0)
#
#
#     print("#{} {}".format(tc + 1, result))