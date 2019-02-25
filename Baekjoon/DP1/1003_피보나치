import sys
sys.stdin = open("1003_input.txt")


# def memo_fibo(n):
#     if n >= 2 and len(memo) <= n:
#         memo.append(memo_fibo(n - 1)[0] + memo_fibo(n - 2)[0])
#         cnt_0.append(memo_fibo(n - 1)[1] + memo_fibo(n - 2)[1])
#         cnt_1.append(memo_fibo(n - 1)[2] + memo_fibo(n - 2)[2])
#     return memo[n], cnt_0[n], cnt_1[n]
#
#
# for tc in range(int(input())):
#     result = [0, 0]
#     memo = [0, 1]
#     cnt_0 = [1, 0]
#     cnt_1 = [0, 1]
#     n = int(input())
#     f = memo_fibo(n)
#
#     print(cnt_0[n], cnt_1[n])
#


f = [0, 1]
def DP_fibo(n):
    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])
        cnt_0.append(cnt_0[i - 1] + cnt_0[i - 2])
        cnt_1.append(cnt_1[i - 1] + cnt_1[i - 2])

    return f[n]




for tc in range(int(input())):
    result = [0, 0]
    memo = [0, 1]
    cnt_0 = [1, 0]
    cnt_1 = [0, 1]

    n = int(input())
    f = DP_fibo(n)

    print(cnt_0[n], cnt_1[n])

