import sys
sys.stdin = open("1912_input.txt")

def dp(n):
    sum_list = [data[0]]
    for i in range(1, n):
        sum_list.append(max(sum_list[-1] + data[i], data[i]))
    return max(sum_list)
n = int(input())
data = list(map(int, input().split()))
result = dp(n)
print(result)