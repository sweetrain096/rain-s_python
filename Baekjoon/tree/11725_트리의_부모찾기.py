import sys
sys.stdin = open("11725_input.txt")
from collections import deque
sys.setrecursionlimit(100000)

def make_tree(nodes):
    # print(nodes, tree_parents)
    node1, node2 = nodes
    if tree_parents[node1] and not tree_parents[node2]:
        tree_parents[node2] = node1

        if data and data[0][0] == node2:
            make_tree(data.popleft())
        # for i in range(len(data)):
        #     if data[i][0] == node2:
        #         print(data[i][0], node2, i, data)
        #         make_tree(data.pop(i))

    elif tree_parents[node2] and not tree_parents[node1]:
        tree_parents[node1] = node2
        if data and data[0][0] == node1:
            make_tree(data.popleft())

        # for i in range(len(data)):
        #     if data[i][0] == node1:
        #         make_tree(data.pop(i))
    else:
        data.append(nodes)


n = int(input())
data = deque()
tree_parents = [0] * (n + 1)
tree_parents[0] = 999
tree_parents[1] = 999
for i in range(n - 1):
    data.append(list(map(int, input().split())))

# print(data)
while data:
    make_tree(data.popleft())

for i in range(2, len(tree_parents)):
    print(tree_parents[i])


#
# def make_tree(data):
#     for i in range(n - 1):
#         num1, num2 = data[i]
#         data_list = [num1, num2]
#
#         for j in data_list:
#             if tree[j][0] == num1:
#                 if not tree[j][1]:
#                     tree[j][1] = num2
#                     tree[num2][0] = num2
#                     tree[num2][3] = num1
#                 elif not tree[j][2]:
#                     tree[j][2] = num2
#                     tree[num2][0] = num2
#                     tree[num2][3] = num1
#                 break
#             elif tree[j][0] == num2:
#                 if not tree[j][1]:
#                     tree[j][1] = num1
#                     tree[num1][0] = num1
#                     tree[num1][3] = num2
#                 elif not tree[j][2]:
#                     tree[j][2] = num1
#                     tree[num1][0] = num1
#                     tree[num1][3] = num2
#                 break
#
#         for j in range(1, n + 1):
#             if tree[j] == num1:
#                 if not tree[2 * j]:
#                     tree[2 * j] = num2
#                 elif not tree[2 * j + 1]:
#                     tree[2 * j + 1] = num2
#                 break
#             elif tree[j] == num2:
#                 if not tree[2 * j]:
#                     tree[2 * j] = num1
#                 elif not tree[2 * j + 1]:
#                     tree[2 * j + 1] = num1
#                 break
#
#
#
# n = int(input())
# data = []
# tree = [[0, 0, 0, 0] for _ in range(n + 1)]
# tree[1][0] = 1
#
# # tree = [0] * (2 ** n)
# # tree[1] = 1
# for i in range(n - 1):
#     data.append(list(map(int, input().split())))
#
# make_tree(data)
#
# data.sort()
# make_tree(data)
#
#
# # for i in range(n - 1):
# #     num1, num2 = data[i]
# #     data_list = [num1, num2]
# #     for j in range(1, n + 1):
# #         if tree[j] == num1:
# #             if not tree[2 * j]:
# #                 tree[2 * j] = num2
# #             elif not tree[2 * j + 1]:
# #                 tree[2 * j + 1] = num2
# #             break
# #         elif tree[j] == num2:
# #             if not tree[2 * j]:
# #                 tree[2 * j] = num1
# #             elif not tree[2 * j + 1]:
# #                 tree[2 * j + 1] = num1
# #             break
#
#
# # print(data)
# # for i in range(n - 1):
# #     num1, num2 = data[i]
# #     data_list = [num1, num2]
# #
# #     for j in data_list:
# #         if tree[j][0] == num1:
# #             if not tree[j][1]:
# #                 tree[j][1] = num2
# #                 tree[num2][0] = num2
# #                 tree[num2][3] = num1
# #             elif not tree[j][2]:
# #                 tree[j][2] = num2
# #                 tree[num2][0] = num2
# #                 tree[num2][3] = num1
# #             break
# #         elif tree[j][0] == num2:
# #             if not tree[j][1]:
# #                 tree[j][1] = num1
# #                 tree[num1][0] = num1
# #                 tree[num1][3] = num2
# #             elif not tree[j][2]:
# #                 tree[j][2] = num1
# #                 tree[num1][0] = num1
# #                 tree[num1][3] = num2
# #             break
# #
# #     for j in range(1, n + 1):
# #         if tree[j] == num1:
# #             if not tree[2 * j]:
# #                 tree[2 * j] = num2
# #             elif not tree[2 * j + 1]:
# #                 tree[2 * j + 1] = num2
# #             break
# #         elif tree[j] == num2:
# #             if not tree[2 * j]:
# #                 tree[2 * j] = num1
# #             elif not tree[2 * j + 1]:
# #                 tree[2 * j + 1] = num1
# #             break
# # print(tree)
#
#
# for i in range(2, len(tree)):
#     if tree[i]:
#         print(tree[i][3])