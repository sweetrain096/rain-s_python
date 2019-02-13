def fibo(n):
    if n < 2:
        return n
    else:
        return fibo(n - 1) + fibo(n - 2)

# print(fibo(7))


memo = [0, 1]
def fibo_memoization(n):
    if n >= 2 and len(memo) <= n:
        memo.append(fibo_memoization(n - 1) + fibo_memoization(n - 2))
    # print(memo)
    return memo[n]

# print(fibo_memoization(998))


def fibo_DP(n):
    f = [0, 1]

    for i in range(2, n + 1):
        f.append(f[i - 1] + f[i - 2])

    return f[n]

print(fibo_DP(1000))