import sys
sys.stdin = open("1945_input.txt")

for test_case in range(int(input())):
    n = int(input())
    result = [0] * 5
    cnt = 0
    while 1:

        if n // 2 == n / 2:
            n = n // 2
            result[0] += 1
        elif n // 3 == n / 3:
            n = n // 3
            result[1] += 1
        elif n // 5 == n / 5:
            n = n // 5
            result[2] += 1
        elif n // 7 == n / 7:
            n = n // 7
            result[3] += 1
        elif n // 11 == n / 11:
            n = n // 11
            result[4] += 1
        else:
            break

    print(f"#{test_case + 1} {' '.join(map(str, result))}")