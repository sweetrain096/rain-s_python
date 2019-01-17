import sys
sys.stdin = open("minmax_input.txt")

T = int(input())
for test_case in range(T) :
    N = int(input())
    numbers = list(map(int, input().split()))
    max_num = numbers[0]
    min_num = numbers[0]
    for number in numbers:
        if max_num < number :
            max_num = number
        if min_num > number :
            min_num = number
    result = max_num - min_num

    print(f"#{test_case + 1} {result}")