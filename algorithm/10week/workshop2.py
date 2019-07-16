import sys
sys.stdin = open("workshop2_input.txt")

def powerset(n, k, sum_data):
    global result
    if sum_data >= b:
        result = min(result, sum_data)
        return
    if n == k:
        # print(tmp, sum_data)
        return
    else:
        tmp[k] = 1
        powerset(n, k + 1, sum_data + data[k])
        tmp[k] = 0
        powerset(n, k + 1, sum_data)


t = int(input())
for tc in range(t):
    n, b = map(int, input().split())
    data = list(map(int, input().split()))
    tmp = [0] * n
    result = 9999999999999999999
    powerset(n, 0, 0)
    print("#{} {}".format(tc + 1, result - b))