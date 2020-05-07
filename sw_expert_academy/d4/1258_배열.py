import sys
sys.stdin = open("1258_input.txt")


def find(pr, pc):
    cnt_r = 0
    cnt_c = 0
    r2 = 0
    c2 = 0
    for r in range(pr, n):
        if Map[r][pc]:
            cnt_r += 1
        else:
            r2 = r
            break
    for c in range(pc, n):
        if Map[pr][c]:
            cnt_c += 1
        else:
            c2 = c
            break
    for r in range(pr, r2):
        for c in range(pc, c2):
            Map[r][c] = 0
    # print(cnt_r, cnt_c)
    # print(pr, r, pc, c)
    # range_list.append((pr, r, pc, c))
    arr_size.append([cnt_r, cnt_c, cnt_r*cnt_c])



for tc in range(int(input())):
    n = int(input())

    Map = []
    for line in range(n):
        Map.append(list(map(int, input().split())))

    range_list = []
    arr_size = []

    for r in range(n):
        for c in range(n):
            if Map[r][c]:
                find(r, c)
    # print(arr_size)
    arr_size.sort(key=lambda x:(x[2], x[0]))

    result = []
    for r, c, mul in arr_size:
        result.append(r)
        result.append(c)

    print(f"#{tc + 1} {int(len(result)/2)} {' '.join(map(str, result))}")


