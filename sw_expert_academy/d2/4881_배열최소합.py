import sys
sys.stdin = open("4881_input.txt")

def permutation(N, r, tmp_sum):
    global result
    if tmp_sum > result:
        return

    if not r:
        if result == 999999999999999:
            result = tmp_sum
        else:
            result = min(result, tmp_sum)

        # print(t)
    else:
        for i in range(N - 1, -1, -1):
            candidates[i], candidates[N - 1] = candidates[N - 1], candidates[i]
            t[r - 1] = candidates[N - 1]

            permutation(N - 1, r - 1, tmp_sum + base[r - 1][candidates[N - 1] - 1])
            candidates[i], candidates[N - 1] = candidates[N - 1], candidates[i]


for tc in range(int(input())):
    n = int(input())
    base = []
    for i in range(n):
        base.append(list(map(int, input().split())))


    result = 999999999999999

    candidates = [i for i in range(1, n + 1)]
    t = [0] * n
    permutation(n, n, 0)
    print("#{} {}".format(tc + 1, result))
