import sys
sys.stdin = open("11726_input.txt")

def find(n):
    data = [1, 2]
    for i in range(2, n + 1):
        data.append(data[i - 2] + data[i - 1])
    return data[n - 1]

n = int(input())

print(find(n) % 10007)