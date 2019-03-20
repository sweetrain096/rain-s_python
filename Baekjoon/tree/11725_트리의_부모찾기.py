import sys
sys.stdin = open("11725_input.txt")

n = int(input())
data = []
# tree = [[0, 0, 0, 0] for _ in range(n + 1)]
# tree[1][0] = 1

tree = [0] * (2 ** n)
tree[1] = 1
for i in range(n - 1):
    data.append(list(map(int, input().split())))
data.sort()



for i in range(n - 1):
    num1, num2 = data[i]
    data_list = [num1, num2]
    for j in range(1, n + 1):
        if tree[j] == num1:
            if not tree[2 * j]:
                tree[2 * j] = num2
            elif not tree[2 * j + 1]:
                tree[2 * j + 1] = num2
            break
        elif tree[j] == num2:
            if not tree[2 * j]:
                tree[2 * j] = num1
            elif not tree[2 * j + 1]:
                tree[2 * j + 1] = num1
            break


# print(data)
# for i in range(n - 1):
#     num1, num2 = data[i]
#     data_list = [num1, num2]
#
#     for j in data_list:
#         if tree[j][0] == num1:
#             if not tree[j][1]:
#                 tree[j][1] = num2
#                 tree[num2][0] = num2
#                 tree[num2][3] = num1
#             elif not tree[j][2]:
#                 tree[j][2] = num2
#                 tree[num2][0] = num2
#                 tree[num2][3] = num1
#             break
#         elif tree[j][0] == num2:
#             if not tree[j][1]:
#                 tree[j][1] = num1
#                 tree[num1][0] = num1
#                 tree[num1][3] = num2
#             elif not tree[j][2]:
#                 tree[j][2] = num1
#                 tree[num1][0] = num1
#                 tree[num1][3] = num2
#             break

    # for j in range(1, n + 1):
    #     if tree[j] == num1:
    #         if not tree[2 * j]:
    #             tree[2 * j] = num2
    #         elif not tree[2 * j + 1]:
    #             tree[2 * j + 1] = num2
    #         break
    #     elif tree[j] == num2:
    #         if not tree[2 * j]:
    #             tree[2 * j] = num1
    #         elif not tree[2 * j + 1]:
    #             tree[2 * j + 1] = num1
    #         break
    print(tree)
for i in range(2, n + 1):
    print(tree[i][3])