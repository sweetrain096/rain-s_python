import sys
sys.stdin = open("workshop1_input.txt")

def perm(n, k, sum_data):
    global result
    if result < sum_data:
        return

    if n == k:
        last_check = sum_data + abs(data[k - 1][0] - er) + abs(data[k - 1][1] - ec)
        result = min(last_check, result)
        # print(data)
    else:
        for i in range(k, n):
            data[i], data[k] = data[k], data[i]
            if not k:
                tmp_sum = abs(sr - data[k][0]) + abs(sc - data[k][1])
                perm(n, k + 1, sum_data + tmp_sum)
            else:
                tmp_sum = abs(data[k - 1][0] - data[k][0]) + abs(data[k - 1][1] - data[k][1])
                perm(n, k + 1, sum_data + tmp_sum)
            data[i], data[k] = data[k], data[i]

t = int(input())
for tc in range(t):
    n = int(input())
    tmp = list(map(int, input().split()))
    sr, sc, er, ec = tmp[0], tmp[1], tmp[2], tmp[3]
    data = []
    a = []
    for i in range(4, 4 + (n * 2)):
        a.append(tmp[i])
        if len(a) == 2:
            data.append(a)
            a = []
    # print(sr, sc, er, ec)
    # print(data)
    result = 99999999999999999999999999999
    perm(n, 0, 0)
    print("#{} {}".format(tc + 1, result))



