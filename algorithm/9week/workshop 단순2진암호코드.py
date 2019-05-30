import sys
sys.stdin = open("workshop_input.txt")

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
    for i in range(r):
        data = list(map(int, input().strip()))
        if not result and 1 in data:
            # print(data)
            cnt = 0
            j = 1
            while cnt <= 7:
            # for j in range(1, c + 1):
                if data[-j]:
                    for now_pattern in range(10):
                        if patterns[now_pattern] == data[-(j + 7 - 1) : -(j - 1)]:
                            result.append(now_pattern)
                            cnt += 1
                            j += 7
                            break
                else:
                    j += 1
    result = result[::-1]
    plus_even, plus_odd = 0, 0
    for i in range(8):
        if not i % 2:
            plus_even += result[i]
        else:
            plus_odd += result[i]

    final = plus_even * 3 + plus_odd
    if not final % 10:
        print("#{} {}".format(tc + 1, sum(result)))
    else:
        print("#{} {}".format(tc + 1, 0))
