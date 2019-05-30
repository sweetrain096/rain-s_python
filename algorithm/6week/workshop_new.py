import sys

sys.stdin = open("workshop.txt")
n = int(input())
for tc in range(n):
    n = int(input())
    table = []
    for row in range(n):
        table.append(list(map(int, input().split())))

    check_list = []

    plus, check_col = 0, 0
    for col in range(n):
        for row in range(n):
            # print(check_list, [row, col], table[row][col])
            if row + 1 < n and col + 1 < n and table[row][col]:

                plus += 1

            else:
                if row + 1 == n and col + 1 < n and table[row][col]:
                    plus += 1

                # print(plus)
                flag = False
                for cl in check_list:
                    if plus == cl[0]:
                        flag = True
                        plus, check_plus = 0, 0
                if not flag and plus != 0:

                    check_list.append([plus])
                    plus = 0
                    check_plus = 0
                    for check_col in range(n):
                        # print(check_list, [row - 1, col + check_col])
                        if col + check_col + 1 <= n and table[row - 1][col + check_col]:
                            check_plus += 1
                        else:
                            check_list[-1] += [check_plus]
                            break

    check_list.sort()
    result_list1 = []
    # print(check_list)
    ind = 0
    for i in check_list:
        calc = i[0] * i[1]
        i.insert(0, calc)
        result_list1.append(calc)
        # print(calc)
    result_list1.sort()
    check_list.sort()
    # print(result_list1)
    for i in range(len(check_list)):
        # print(result_list1[i], check_list[i])
        if result_list1[i] == check_list[i][0]:
            result_list1[i] = check_list[i][1:]
    result = []
    # print(result_list1)
    for i in result_list1:
        # print(result, i)
        result += i

    print(f"#{tc + 1} {len(check_list)} {' '.join(map(str, (result)))}")