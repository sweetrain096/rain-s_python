import sys
sys.stdin = open("numbercard_input.txt")

T = int(input())
for test_case in range(T) :
    N = int(input())
    numbers = input()
    check_list = [0] * 10
    for number in numbers:
        check_list[int(number)] += 1
    max_num = check_list[0]
    result_num = 0
    for num in range(len(check_list)):
        if max_num <= check_list[num] :
            max_num = check_list[num]
            result_num = num
    print(f"#{test_case + 1} {result_num} {max_num}")