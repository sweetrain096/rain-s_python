import sys
sys.stdin = open("6960_input.txt")

def merge_sort(list):
    if len(list) <= 1:
        return list
    mid = len(list) // 2
    leftList = list[:mid]
    rightList = list[mid:]
    leftList = merge_sort(leftList)
    rightList = merge_sort(rightList)
    return merge(leftList, rightList)

def merge(left, right):
    result = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left[0])
                left = left[1:]
            else:
                result.append(right[0])
                right = right[1:]
        elif len(left) > 0:
            result.append(left[0])
            left = left[1:]
        elif len(right) > 0:
            result.append(right[0])
            right = right[1:]
    return result


# for tc in range(int(input())):
#     n = int(input())
#     sf_list = []
#     for test_case in range(n):
#
#         sf_list.append(list(map(int, input().split())))
#
#     sort_list = merge_sort(sf_list)
#
#
#     sec = 0
#     result = 0
#
#     for fs in sort_list:
#             # print(fs)
#             sec += fs[1]
#             if fs[0] >= fs[1] and fs[0] >= sec:
#                 result += 1
#             if fs[0] < fs[1] or fs[0] < sec:
#                 sec -= fs[1]
#             print(sec)
#
#
#     sec = 0
#     result = 0
#     # for sf in sort_list:
#     #     sec += sf[0]
#     #     if sf[0] <= sf[1] and sf[1] >= sec:
#     #         result += 1
#     #     if sf[0] > sf[1] or sf[1]< sec:
#     #         sec -= sf[0]
#     #     print(sec)
#
#
#
#
#     print(f"#{tc + 1} {sort_list} {result}")
#     # print(f"#{tc + 1} {result}")


for tc in range(int(input())):
    n = int(input())
    sf_list = []
    for test_case in range(n):
        s, f = map(int, input().split())
        sf_list.append([f, s])
    sort_list = merge_sort(sf_list)

    sec = 0
    result = 0

    stack = []
    cnt = 0
    for fs in range(n):
        if sort_list[fs][0] >= sort_list[fs][1]:
            if not stack:
                stack.append(sort_list[fs])
            elif stack[-1] != sort_list[fs]:
                stack = [sort_list[fs]]
            else:
                stack.append(sort_list[fs])
        print(stack)



    #
    # for fs in sort_list:
    #     # print(fs)
    #     sec += fs[1]
    #     if fs[0] >= fs[1] and fs[0] >= sec:
    #         result += 1
    #     if fs[0] < fs[1] or fs[0] < sec:
    #         sec -= fs[1]
    #     print(sec)


    print("#{} {} {}".format(tc + 1, sort_list, result))
    # print(f"#{tc + 1} {sort_list} {result}")
    # print(f"#{tc + 1} {result}")



#
# for tc in range(int(input())):
#     n = int(input())
#     sf_list = []
#     for test_case in range(n):
#         s, f = map(int, input().split())
#         sf_list.append([f, s])
#     sort_list = merge_sort(sf_list)
#
#     sec = 0
#     result = 0
#     for fs in sort_list:
#         # print(fs)
#         sec += fs[1]
#         if fs[0] >= fs[1] and fs[0] >= sec:
#             result += 1
#         if fs[0] < fs[1] or fs[0] < sec:
#             sec -= fs[1]
#         print(sec)
#
#
#
#
#     print(f"#{tc + 1} {sort_list} {result}")
#     # print(f"#{tc + 1} {result}")