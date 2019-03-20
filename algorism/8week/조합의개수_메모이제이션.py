'''
중복되지 않게 4C3
'''

def combination(n, r):
    memo = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(n+ 1):
        for j in range(min(i, r) + 1):
            if not j or j == i:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i - 1][j - 1] + memo[i - 1][j]
    return memo[n][r]



print(combination(100, 50))