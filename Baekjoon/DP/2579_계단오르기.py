import sys
sys.stdin = open("2579_input.txt")

def sol(n):
    for i in range(3, n + 1):
        sum_data.append(max(sum_data[i - 3] + data[i - 1] + data[i], sum_data[i - 2] + data[i]))
    # print(sum_data)

    return sum_data[n]



n = int(input())
data = [0]
for i in range(n):
    data.append(int(input()))
sum_data = [0]
for i in range(1, 3):
    sum_data.append(data[i] + data[i - 1])

# print(data)

print(sol(n))
