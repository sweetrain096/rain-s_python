import sys
sys.stdin = open("workshop_input.txt")

for test_case in range(10):
    tn = int(input())
    lists = []
    for i in range(100):
        lists.append(input())

    result = 0
    m = 100
    while m >= 1 :
        for row in range(100):
            for col in range(100 - m + 1):
                for cnt in range(int(m / 2)):
                    if lists[row][col + cnt] != lists[row][col + m - 1 - cnt]:
                        break
                    if cnt + 1 == int(m / 2):
                        result = m
                        break

        for col in range(100):
            for row in range(100 - m + 1):
                for cnt in range(int(m / 2)):

                    if lists[row + cnt][col] != lists[row + m - 1 - cnt][col]:
                        break
                    else:
                        if cnt + 1 == int(m / 2):
                            result = m
                            break

        if result:
            break
        m -= 1


    print(f"#{tn} {result}")

