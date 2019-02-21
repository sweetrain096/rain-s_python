import sys
sys.stdin = open("4881_input.txt")

MAXCANDIDATES = 100
NMAX = 100

def process_solution(a, k, sum_data):
    if sum_data != 10:
        return
    for i in range(1, k + 1):
        if a[i]:
            print(table[i], end=" ")
    print()

def make_candidates(a, k, input, c):
    c[0] = True
    c[1] = False
    return 2

def backtrack(a, k, input, sum_data):
    if sum_data > 10:
        return
    global MAXCANDIDATES
    c = [0] * MAXCANDIDATES

    if k == input:
        process_solution(a, k, sum_data)
    else:
        k += 1
        ncands = make_candidates(a, k, input, c)
        for i in range(ncands):
            a[k] = c[i]
            # 가지치기. a[k]가 1일 때 data[k]의 값을 확인하여 더한다.
            if a[k]:
                backtrack(a, k, input, sum_data + table[k])
            else:
                backtrack(a, k, input, sum_data)



for tc in range(int(input())):
    n = int(input())
    table = [0] * n
    for row in range(n):
        table[row] = [0] + list(map(int, input().split()))
    table.insert(0, [0] * (n + 1))

    for row in table:
        print(row)


    a = [0 for _ in range(n + 1)]
    result = 9999999999999999

    backtrack(a, 0, n, 0)

    print(f"#{tc + 1} {result}")
    # print(f"#{tc + 1}")


