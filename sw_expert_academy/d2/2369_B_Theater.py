import sys
sys.stdin = open("theater_input.txt")

for n in range(int(input())):
    check_list = [0] * 100000
    for test_case in range(int(input())):
        l, r = list(map(int, input().split()))
        for plus in range(l, r + 1):
            check_list[plus - 1] += 1

    print(f"#{n + 1} {sum(check_list)}")