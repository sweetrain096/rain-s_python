import sys
sys.stdin = open("zigzag_num_input.txt")

for test_case in range(int(input())):
    result = 0
    for test in range(1, int(input()) + 1):
        if test % 2 :
            result += test
        else :
            result -= test
    print(f"#{test_case + 1} {result}")