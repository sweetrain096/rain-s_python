import sys
sys.stdin = open("input2.txt")

T = int(input())
for test_case in range(T):
    NxN_list = []
    check = []
    N, M = list(map(int, input().split()))
    for n_time in range(N):
        NxN_list.append(list(map(int, input().split())))
    i = 0
    for row in range(N - M) :

        for col in range(M):
            check.append(NxN_list[col + i][row : row + M])
            # check.append(NxN_list[col + 1])
        i += 1
    print(check)
    print(NxN_list)