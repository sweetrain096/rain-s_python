import sys
sys.stdin = open("2156_input.txt")

def dp(n):
    choice = []
    for i in range(1, n + 1):
        if i == 1:
            choice.append(data[i - 1])
        elif i == 2:
            choice.append(choice[-1] + data[i - 1])
        elif i == 3:
            choice.append(max(choice[-1], data[0] + data[i - 1], data[1] + data[i - 1]))
        else:
            choice.append(max(choice[i - 2], choice[i - 3] + data[i - 1], choice[i - 4] + data[i - 2] + data[i - 1]))
    return choice[n - 1]


n = int(input())
data = []
for i in range(n):
    data.append(int(input()))

# print(data)
print(dp(n))