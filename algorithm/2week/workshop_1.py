import sys
sys.stdin = open("sum_input.txt")

def list_sum(lists):
    result = 0
    for i in lists:
        result += i
    return result

for test in range(10):
    test_case = int(input())
    lists = []
    for lines in range(100):
        lists.append(list(map(int, input().split())))

    max_result = -1

    col_list = []
    cross1 = []
    cross2 = []

    for i in range(100):
        if max_result < list_sum(list(map(list, zip(*lists)))[i]):
            max_result = list_sum(list(map(list, zip(*lists)))[i])

        if max_result < list_sum(lists[i][:]):
            max_result = list_sum(lists[i][:])

        cross1.append(lists[i][i])
        cross2.append(lists[-(i+1)][i])

    if max_result < list_sum(cross1):
        max_result = list_sum(cross1)
    if max_result < list_sum(cross2):
        max_result = list_sum(cross2)

    print(f"#{test_case} {max_result}")

