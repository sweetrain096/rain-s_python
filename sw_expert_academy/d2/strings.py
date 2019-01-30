import sys
sys.stdin = open("strings_input.txt")

for test_case in range(int(input())):
    n, m = list(map(int, input().split()))
    a_list = list(map(int, input().split()))
    b_list = list(map(int, input().split()))
    result = 0


    if n >= m :
        shorter = m
        cnts = n - m
        for cnt in range(cnts + 1):
            check_result = 0
            for check in range(shorter):
                check_result += a_list[check + cnt] * b_list[check]
            if result < check_result:
                result = check_result


    else :
        shorter = n
        cnts = m - n
        for cnt in range(cnts + 1):
            check_result = 0
            for check in range(shorter):
                check_result += a_list[check] * b_list[check + cnt]
            if result < check_result:
                result = check_result


    print(f"#{test_case + 1} {result}")