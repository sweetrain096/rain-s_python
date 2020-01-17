import sys
sys.stdin = open("1486_input.txt")

def combination(n, r):
    global result, Min
    if result:
        return
    if not r:
        # print(T)
        if Min and sum(T) > Min:
            return
        if sum(T) > b:
            results.append(sum(T))
            Min = min(results)
        elif sum(T) == b:
            result = b
    elif n < r:
        return
    else:
        T[r - 1] = s[n - 1]
        combination(n - 1, r - 1)
        combination(n - 1, r)



for tc in range(int(input())):
    n, b = map(int, input().split())
    s = list(map(int, input().split()))
    T = [0 for _ in range(n)]
    results = []
    Min = 0
    result = 0
    for i in range(n):
        combination(n, i + 1)
        if result:
            break

    if not result:
        result = min(results)
    print(f"#{tc + 1} {result - b}")
