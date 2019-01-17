import sys
sys.stdin = open("word_puzzle_input.txt")

T = int(input())
for test_case in range(T):
    N, K = list(map(int, input().split()))
    test_lists = []
    for cases in range(N) :
        test_lists.append(list(map(int, input().split())))
    print(test_lists)
    cnt = 0

    check_row = 0
    check_col = 0
    for i in range(N):
        for j in range(N):
            # row
            if test_lists[i][j] :
                check_row += 1
            else :
                if check_row == K :
                    cnt += 1
                check_row = 0
            # col
            if test_lists[j][i] :
                check_col += 1
            else :
                if check_col == K :
                    cnt += 1
                check_col = 0

        if check_row == K :
            cnt += 1
        check_row = 0

        if check_col == K :
            cnt += 1
        check_col = 0
    print(f"#{test_case + 1} {cnt}")
