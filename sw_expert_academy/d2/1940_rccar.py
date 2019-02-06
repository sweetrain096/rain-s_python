import sys
sys.stdin = open("1940_rc_car_input.txt")

for test_case in range(int(input())):
    a = 0
    m = 0
    for n in range(int(input())):
        drive = list(map(int, input().split()))
        if not drive[0]:
            m += a
        elif drive[0] == 1:
            a += drive[1]
            m += a
        else:
            a -= drive[1]
            if a < 0:
                a = 0
            m += a



    print(f"#{test_case + 1} {m}")