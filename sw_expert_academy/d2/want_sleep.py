import sys
sys.stdin = open("want_sleep_input.txt")

T = int(input())

for test_case in range(T):
    check_lists = [i for i in range(10)]
    N = input()
    init = N[:]
    cnt = 0


    while True :

        for number in N :
            number = int(number)
            if number in check_lists:
                check_lists.remove(number)
        cnt += 1
        N = str((cnt + 1) * int(init))
        if not check_lists :
            break
    print(f"#{test_case+1} {cnt * int(init)}")