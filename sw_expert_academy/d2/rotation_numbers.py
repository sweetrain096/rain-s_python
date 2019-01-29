import sys
sys.stdin = open("rotation_input.txt")

for test_case in range(int(input())):
    n = int(input())
    numbers = []
    rotation_90 = []
    rotation_180 = []
    rotation_270 = []
    for i in range(n):
        numbers.append(list(map(int, input().split())))

    check_nums = ""
    # 90
    for row in range(n):
        for col in range(n):
            check_nums += str(numbers[-(col + 1)][row])
        rotation_90.append(check_nums)
        check_nums = ""

    # 180
    for row in range(n):
        check_nums += "".join(map(str, numbers[-(row+1)][::-1]))
        rotation_180.append(check_nums)
        check_nums = ""

    # 270
    for row in range(n):
        for col in range(n):
            check_nums += str(numbers[col][-(row+1)])
        rotation_270.append(check_nums)
        check_nums = ""

    print(f"#{test_case + 1}")
    for row in range(n):
        print(rotation_90[row], rotation_180[row], rotation_270[row])
