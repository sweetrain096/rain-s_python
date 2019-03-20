import sys
sys.stdin = open("workshop2_input.txt")

def find_mul(j):
    global mul

    for check_cnt in range(2, 9):
        check_mul = []
        now = j
        cnt_mul = 0
        flag = False
        for i in range(7):
            for plus in range(1, check_cnt):
                if data[-now] != data[-(now + plus)]:
                    flag = True
                    break
            check_mul.append(data[-now])
            now += check_cnt
            cnt_mul += 1

            if flag:
                break
        if cnt_mul == 7:
            mul = check_cnt

    if not mul:
        mul = 1





asc = [[0,0,0,0],
        [0,0,0,1],
        [0,0,1,0],
        [0,0,1,1],
        [0,1,0,0],
        [0,1,0,1],
        [0,1,1,0],
        [0,1,1,1],
        [1,0,0,0],
        [1,0,0,1],
        [1,0,1,0],
        [1,0,1,1],
        [1,1,0,0],
        [1,1,0,1],
        [1,1,1,0],
        [1,1,1,1]]

patterns = [[0, 0, 0, 1, 1, 0, 1],
            [0, 0, 1, 1, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 1],
            [0, 1, 1, 1, 1, 0, 1],
            [0, 1, 0, 0, 0, 1, 1],
            [0, 1, 1, 0, 0, 0, 1],
            [0, 1, 0, 1, 1, 1, 1],
            [0, 1, 1, 1, 0, 1, 1],
            [0, 1, 1, 0, 1, 1, 1],
            [0, 0, 0, 1, 0, 1, 1]]

for tc in range(int(input())):
    r, c = map(int, input().split())
    result = []
    before = ""
    for i in range(r):
        input_data = input()
        if before != input_data:
            before = input_data
            while_cnt = len([x for x in input_data.split('000') if len(x) > 4])
            input_data = list(input_data)
            data = []
            # print('while_cnt', while_cnt)
            for i in input_data:
                if ord(i) >= 65:
                    data += asc[ord(i) - 55]
                else:
                    data += asc[int(i)]

            if 1 in data:
                total = len(data)
                # print(data)
                j = 1

                for while_cnt_check in range(while_cnt):
                    cnt = 0
                    mul = 0
                    tmp = []

                    while True:
                        if j >= total:
                            break
                        if cnt == 8:
                            break
                        # if cnt and not cnt % 7:
                        if data[-j]:
                            check_mul = find_mul(j)
                            # print(mul)

                            for now_pattern in range(10):
                                flag = False
                                for plus in range(7):
                                    if patterns[now_pattern][-(plus + 1)] != data[-(j + plus * mul)]:
                                        flag = True
                                        break
                                if not flag:
                                    # print(patterns[now_pattern])
                                    # result.append(now_pattern)
                                    tmp.append(now_pattern)
                                    j += 7 * mul
                                    cnt += 1
                                    break
                        else:
                            j += 1

                    tmp = tmp[::-1]
                    if tmp not in result and tmp:
                        result.append(tmp)




    # result = result[::-1]

    # print(len(result), result)
    plus_even, plus_odd, check = 0, 0, 0
    final = 0

    for i in range(len(result)):
        for j in range(8):
            if not j % 2:
                plus_even += result[i][j]
            else:
                plus_odd += result[i][j]

        check = plus_even * 3 + plus_odd
        # print(check)
        if not check % 10:
            final += sum(result[i])
        check, plus_even, plus_odd = 0, 0, 0

    print("#{} {}".format(tc + 1, final))
    # if not check % 10:
    #     print("#{} {}".format(tc + 1, sum(result)))
    # else:
    #     print("#{} {}".format(tc + 1, 0))

# for now_pattern in range(10):
#     if patterns[now_pattern] == data[-(j + 7 - 1) : -(j - 1)]:
#         result.append(now_pattern)
#         cnt += 1
#         j += 7
#         mul = 1
#         break


# now = j
# cnt_mul = 0
# for check_cnt in range(2, 9):
#     check_mul = []
#     for plus in range(1, check_cnt):
#         if data[-now] != data[-(now + plus)]:
#             break
#         now += check_cnt
#         cnt_mul += 1
#         check_mul.append(data[-now])
#     if cnt_mul == 7:
#         mul = check_cnt
#         check_mul = check_mul[::-1]
#         break
# if not mul:
#     mul = 1
