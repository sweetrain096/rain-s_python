import sys
sys.stdin = open("mid_avr_input.txt")

for test_case in range(int(input())):
    numbers = list(map(int, input().split()))
    del numbers[numbers.index(max(numbers))]
    del numbers[numbers.index(min(numbers))]
    print(f"#{test_case + 1} {int(round(sum(numbers)/8, 0))}")