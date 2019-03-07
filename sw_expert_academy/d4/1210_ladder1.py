import sys
sys.stdin = open("1210_input.txt")

deg = [-1, 1]
for test_case in range(10):
    tc = int(input())
    ladder = []
    for i in range(100):
        ladder.append(list(map(int, input().split())))
    cnt = 0
    col = 0
    for i in ladder[-1]:
        if i == 2:
            col = cnt
            break
        cnt += 1


    for row in range(1, 101):
        check = 0
        for plus_col in deg:
            # print(col + plus_col, ladder[-row][col + plus_col])
            if col + plus_col >= 0 and col + plus_col < 100 and ladder[-row][col + plus_col]:
                check = plus_col
                col += check
                break
        # print(row, check)
        if check:
            while True:
                if col < 0 or col >= 100 or not ladder[-row][col]:
                    break
                col += check
            col -= check
    print("#{} {}".format(tc, col))