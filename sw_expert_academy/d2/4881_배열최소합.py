import sys
sys.stdin = open("4881_input.txt")

def permutation(N, r):
    global result
    if not r:
        tmp = 0

        for i in range(n):
            # print("hi", base[i][candidates[i] - 1])
            tmp += base[i][candidates[i] - 1]
            if tmp > result:
                break
        result = min(result, tmp)
        print(t)
    else:
        for i in range(N - 1, -1, -1):
            candidates[i], candidates[N - 1] = candidates[N - 1], candidates[i]
            t[r - 1] = candidates[N - 1]
            permutation(N - 1, r - 1)
            candidates[i], candidates[N - 1] = candidates[N - 1], candidates[i]


for tc in range(int(input())):
    n = int(input())
    base = []
    for i in range(n):
        base.append(list(map(int, input().split())))

    # for i in base:
    #     print(i)
    # print()

    result = 999999999999999

    candidates = [i for i in range(1, n + 1)]
    t = [0] * n
    permutation(n, n)
    print("#{} {}".format(tc + 1, result))


# def make_result(k, sum_data):
#     global result
#     if sum_data > result:
#         return
#     # print(a, k)
#     print('result', a)
#     for i in range(1, k + 1):
#         result = sum_data
#         # print(a[i][0], a[i][1])
#
#         print(table[a[i][0]][a[i][1]], end=" ")
#     print()
#
# def make_candidates(a, k, c):
#     visi_row = [0] * (n + 1)
#     visi_col = [0] * (n + 1)
#
#     ncands = 0
#
#     for i in range(1, k + 1):
#         visi_row[a[i][0]] += 1
#         visi_col[a[i][1]] += 1
#
#     for i in range(1, k + 1):
#         for j in range(1, k + 1):
#             if visi_row[i] == 0 and visi_col[j] < 2:
#                 c[ncands] = [i, j]
#                 # [i] = i
#                 # c[ncands][j] = j
#                 ncands += 1
#     print('c', c, ncands)
#     return ncands
#
#
#
# def backtrack(a, k, depth, sum_data):
#     global result
#
#     c = [0 for _ in range(n + 1)]
#     if sum_data > result:
#         return
#
#     if k == depth:
#         make_result(k, sum_data)
#     else:
#         k += 1
#         ncands = make_candidates(a, k, c)
#         for i in range(ncands):
#             a[k] = c[i]
#             print('a[k]', a[k])
#             backtrack(a, k, depth, sum_data + table[a[k][0]][a[k][1]])
#
#
#
# # def process_solution(a, k, sum_data):
# #     if sum_data != 10:
# #         return
# #     for i in range(1, k + 1):
# #         if a[i]:
# #             print(table[i], end=" ")
# #     print()
# #
# # def make_candidates(a, k, input, c):
# #     c[0] = True
# #     c[1] = False
# #     return 2
# #
# # def backtrack(a, k, k_delta, input, sum_data):
# #     if sum_data > 10:
# #         return
# #     global MAXCANDIDATES
# #     c = [0] * MAXCANDIDATES
# #
# #     if k == input:
# #         process_solution(a, k, sum_data)
# #     else:
# #         k += 1
# #
# #         ncands = make_candidates(a, k, input, c)
# #         for i in range(ncands):
# #             a[k] = c[i]
# #             # 가지치기. a[k]가 1일 때 data[k]의 값을 확인하여 더한다.
# #             if a[k]:
# #                 backtrack(a, k, k_delta, input, sum_data + table[k])
# #             else:
# #                 backtrack(a, k, k_delta, input, sum_data)
# #     print('a', a)
#
#
#
#
#
#
# MAXCANDIDATES = 100
#
# for tc in range(int(input())):
#     n = int(input())
#     table = [0] * n
#     for row in range(n):
#         table[row] = [0] + list(map(int, input().split()))
#     table.insert(0, [0] * (n + 1))
#
#     for row in table:
#         print(row)
#
#
#     a = [[0 for _ in range(2)] for _ in range(n + 1)]
#     result = 9999999999999999
#     #
#     backtrack(a, 0, n, 0)
#     #
#     #
#     # print(f"#{tc + 1} {result}")
#     print(f"#{tc + 1}")
#
#
# #
# # def make_result(k, sum_data):
# #     global result
# #     if sum_data > result:
# #         return
# #     # print(a, k)
# #     for i in range(1, k + 1):
# #         result = sum_data
# #         # print(a[i][0], a[i][1])
# #
# #         print(table[a[i][0]-1][a[i][1]-1], end=" ")
# #     print()
# #
# # def make_candidates(a, k, c):
# #     visi_row = [0] * (n + 1)
# #     visi_col = [0] * (n + 1)
# #
# #     ncands = 0
# #
# #     for i in range(1, k + 1):
# #         visi_row[a[i][0]] += 1
# #         visi_col[a[i][1]] += 1
# #
# #     print(visi_row)
# #     print(visi_col)
# #     for i in range(1, k + 1):
# #         for j in range(1, k + 1):
# #             if visi_row[i] == 0 and visi_col[j] < 2:
# #                 c[ncands] = [i, j]
# #                 # [i] = i
# #                 # c[ncands][j] = j
# #                 ncands += 1
# #     print('c', c, ncands)
# #     return ncands
# #
# #
# #
# # def backtrack(a, k, depth, sum_data):
# #     global result
# #
# #     c = [0 for _ in range(n + 1)]
# #     if sum_data > result:
# #         return
# #
# #     if k == depth:
# #         make_result(k, sum_data)
# #     else:
# #         k += 1
# #         ncands = make_candidates(a, k, c)
# #         for i in range(ncands):
# #             a[k] = c[i]
# #             print('a[k]', a[k])
# #             backtrack(a, k, depth, sum_data + table[a[k][0] - 1][a[k][1] - 1])
# #
# #
