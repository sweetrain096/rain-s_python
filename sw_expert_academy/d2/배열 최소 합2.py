import sys
sys.stdin = open("4881_input.txt")

def process_solution(a, k, sum_data):
    global result
    if sum_data < result:
        result = sum_data
    else:
        return
    for i in range(1, k + 1):
        if a[i]:
            print(data[i][a[i]], end=" ")
    print()

def make_candidates(a, k, input, c):
    c[0] = 1
    c[1] = 2
    c[2] = 3
    return 3

def backtrack(a, k, input, sum_data):
    print(a)
    global result
    print('sum', sum_data, a)
    visited = []

    if sum_data > result:
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
                visited.append(a[k])
                backtrack(a, k, input, sum_data + data[k][a[k]])

            else:
                backtrack(a, k, input, sum_data)



# 임의의 값(공간)을 미리 확보


MAXCANDIDATES = 100
NMAX = 100



for tc in range(int(input())):
    n = int(input())
    data = [0] * n

    for row in range(n):
        data[row] = [0] + list(map(int, input().split()))
    data.insert(0, [0] * (n + 1))

    for row in data:
        print(row)


    a = [0 for _ in range(n + 1)]
    result = 9999999999999999

    backtrack(a, 0, n, 0)

    print(f"#{tc + 1} {result}")
    # print(f"#{tc + 1}")


