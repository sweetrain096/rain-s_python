import sys
sys.stdin = open("workshop2_input.txt")

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
# check_mul = [[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
#              [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
#              ]

for tc in range(int(input())):
    r, c = map(int, input().split())
    result = []
    before = []
    for i in range(r):
        input_data = list(input())
        if before != input_data:
            before = input_data
            mul = 0
            data = []
            for i in input_data:
                if ord(i) >= 65:
                    data += asc[ord(i) - 55]
                else:
                    data += asc[int(i)]

            if 1 in data:
                total = len(data)
                print(data)
                cnt = 0
                j = 1
                while True:
                    if j >= total:
                        break
                    # if cnt and not cnt % 7:

                    if data[-j]:
                        # for now_pattern in range(10):
                        #     if patterns[now_pattern] == data[-(j + 7 - 1) : -(j - 1)]:
                        #         result.append(now_pattern)
                        #         cnt += 1
                        #         j += 7
                        #         mul = 1
                        #         break
                        if not mul:
                            now = j
                            cnt_mul = 0
                            for check_cnt in range(2, 9):
                                check_mul = []
                                for plus in range(1, check_cnt):
                                    if data[-now] != data[-(now + plus)]:
                                        break
                                    now += check_cnt
                                    cnt_mul += 1
                                    check_mul.append(data[-now])
                                if cnt_mul == 7:
                                    mul = check_cnt
                                    check_mul = check_mul[::-1]
                                    break
                            if not mul:
                                mul = 1
                        print(check_mul)
                        if mul:
                            for now_pattern in range(10):
                                if patterns[now_pattern] == check_mul[-(j + 7 - 1): -(j - 1)]:
                                    result.append(now_pattern)
                                    cnt += 1
                                    j += 7
                                    mul = 1
                                    break


                                # check_mul[-(j + (check_cnt) - 1) : -(j - 1)]


                    else:
                        j += 1


    result = result[::-1]
    plus_even, plus_odd = 0, 0
    for i in range(8):
        if not i % 2:
            plus_even += result[i]
        else:
            plus_odd += result[i]

    check = plus_even * 3 + plus_odd
    if not check % 10:
        print("#{} {}".format(tc + 1, sum(result)))
    else:
        print("#{} {}".format(tc + 1, 0))
