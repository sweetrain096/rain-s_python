import sys
sys.stdin = open("sum_input.txt")

T = int(input())
for test_case in range(T):
    N, M = list(map(int, input().split()))
    numbers = list(map(int, input().split()))
    sum_check = []
    sum_num = 0
    for number in range(N - M + 1):
        for i in range(M) :
            sum_num += numbers[number + i]
        sum_check.append(sum_num)
        sum_num = 0
    max_num = sum_check[0]
    min_num = sum_check[0]
    for check_number in sum_check:
        if max_num < check_number:
            max_num = check_number
        if min_num > check_number:
            min_num = check_number
    print(f"#{test_case + 1} {max_num - min_num}")