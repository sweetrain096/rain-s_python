import sys
sys.stdin = open("15655_input.txt")


def combination(n, r, result):
    if not r:
        print(' '.join(map(str, result)))
        return
    if n < r:
        return
    result.append(arr[n-1])
    combination(n-1, r-1, result)
    result.pop()
    combination(n-1, r, result)

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
combination(n, m, [])
