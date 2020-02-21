import sys
sys.stdin = open("strings_input.txt")

for test_case in range(int(input())):
    n, m = list(map(int, input().split()))
    lists = []
    for cnt in range(n):
        lists.append(input())
    result = ""
    for row in range(n):
        for col in range(n - m + 1):
            for cnt in range(int(m/2)):
                if lists[row][col + cnt] != lists[row][col + m - 1 - cnt]:
                    break
                if cnt + 1 == int(m/2) :
                    result = lists[row][col:col + m]

    if not result:
        result2 = [""] * m
        for col in range(n):
            for row in range(n - m + 1):
                for cnt in range(int(m/2)):

                    if lists[row + cnt][col] != lists[row + m - 1 - cnt][col]:
                        result2 = [""] * m
                        break
                    else:

                        result2[cnt] = lists[row + cnt][col]
                        result2[-(cnt + 1)] = lists[row + cnt][col]
                        if "" not in result2:
                            result = ''.join(result2)

                            break

                        if m%2:
                            result2[int(m/2)] = lists[row + cnt + 2][col]


    print(f"#{test_case + 1} {result}")