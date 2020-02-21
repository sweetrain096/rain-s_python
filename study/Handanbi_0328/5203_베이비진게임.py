import sys
sys.stdin = open("5203_input.txt")

def babyGin(arr):
    global flag

    triple, run = 0, 0

    for i in range(2):
        if arr[i] == arr[i + 1]:
            triple += 1
        elif arr[i] == arr[i + 1] + 1:
            run += 1
    if triple == 2 or run == 2:
        flag = 1
        return

    return


def perm(n, k, data):
    if flag:
        return
    if k == n:
        babyGin(data)
        # print(data)
        return
    else:
        for i in range(k, n):
            data[i], data[k] = data[k], data[i]
            perm(n, k + 1, data)
            data[i], data[k] = data[k], data[i]

for tc in range(int(input())):
    p1 = []
    p2 = []
    tmp = list(map(int, input().split()))
    for i in range(12):
        if not i % 2:
            p1.append(tmp[i])
        else:
            p2.append(tmp[i])

            if i > 4:
                flag = 0
                perm(i // 2 + 1, 0, p1)
                if flag:
                    print("#{} {}".format(tc + 1, 1))
                    break
                else:
                    flag = 0
                    perm(i // 2 + 1, 0, p2)
                    if flag:
                        print("#{} {}".format(tc + 1, 2))
                        break

    if not flag:
        print("#{} {}".format(tc + 1, 0))


