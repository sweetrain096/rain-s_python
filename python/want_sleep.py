T = int(input())

for test_case in range(1, T + 1):
    check_lists = [i for i in range(10)]
    N = input()
    cnt = 1
    while True :

        for number in N :
            if number in check_lists:
                check_lists.remove(int(number))
        N = 2 * N
        cnt += 1
        if not check_lists :
            break
    print(f"#{test_case+1}")