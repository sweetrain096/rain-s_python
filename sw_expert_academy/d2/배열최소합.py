import sys
sys.stdin = open("4881_input.txt")




def make_result(k, sum_data):
    global result
    # if sum_data >= result:
    #     return
    # print(a, k)
    print('result', a)
    for i in range(1, k + 1):
        result = sum_data
        # print(a[i][0], a[i][1])

        print(table[a[i][0]][a[i][1]], end=" ")
    print()

def make_candidates(a, k, c):
    visi_row = [0] * (n + 1)
    visi_col = [0] * (n + 1)

    ncands = 0

    for i in range(1, k + 1):
        visi_row[a[i][0]] += 1
        visi_col[a[i][1]] += 1

    for i in range(1, k + 1):
        for j in range(1, k + 1):
            if visi_row[i] == 0 and visi_col[j] < 2:
                c[ncands] = [i, j]
                # [i] = i
                # c[ncands][j] = j
                ncands += 1
    print('c', c, ncands)
    return ncands



def backtrack(a, k, depth, sum_data):
    global result

    c = [0 for _ in range(n + 1)]
    # if sum_data > result:
    #     return

    if k == depth:
        make_result(k, sum_data)
    else:
        k += 1
        ncands = make_candidates(a, k, c)
        for i in range(ncands):
            a[k] = c[i]
            print('a[k]', a, a[k])
            backtrack(a, k, depth, sum_data + table[a[k][0]][a[k][1]])





MAXCANDIDATES = 100

for tc in range(int(input())):
    n = int(input())
    table = [0] * n
    for row in range(n):
        table[row] = [0] + list(map(int, input().split()))
    table.insert(0, [0] * (n + 1))

    for row in table:
        print(row)


    a = [[0 for _ in range(2)] for _ in range(n + 1)]
    result = 9999999999999999
    #
    backtrack(a, 0, n, 0)
    #
    #
    print(f"#{tc + 1} {result}")
    # print(f"#{tc + 1}")


