import sys
sys.stdin = open("workshop2_input.txt")

for test_case in range(int(input())):
    n = int(input())
    cases = list(map(int, input().split()))
    result = []
    first_num = 0

    for first in range(n):
        if not cases[first * 2] in cases[1 : : 2] :
            first_num = first
    result.append(cases[first_num * 2])
    result.append(cases[first_num * 2 + 1])

    check = 0

    while True:

        if result[-1] == cases[check * 2] :
            result.append(cases[check * 2])
            result.append(cases[check * 2 + 1])
            check = 0
        check += 1
        if len(result) == len(cases):
            break
        if check == n :
            check = 0
            continue



    print(f"#{test_case + 1} {' '.join(map(str, result))}")