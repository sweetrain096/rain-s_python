import sys
sys.stdin = open("input2.txt")

T = int(input())
for test_case in range(T):
    NxN_list = []
    N, M = list(map(int, input().split()))
    for n_time in range(N):
        NxN_list.append(list(map(int, input().split())))

    plus_sum = []
    i = 0
    row = 0

    while True:
        plus = 0
        for col in range(M):
            plus += sum(NxN_list[col + i][row : row + M])
        plus_sum.append(plus)
        row += 1
        if row + M - 1 == N :
            row = 0
            i += 1
            if col + i == N :
                break

    print(f"#{test_case + 1} {max(plus_sum)}")

