import sys
sys.stdin = open("1217_input.txt")


def exponentiation(n, m):
    global result, cnt
    if cnt == m:
        return result
    else:
        cnt += 1
        result *= n
        return exponentiation(n, m)

for tc in range(10):
    result = 1
    cnt = 0
    test_case = input()
    n, m = map(int, input().split())
    result = exponentiation(n, m)

    print(f"#{test_case} {result}")