import sys
sys.stdin = open("10026_input.txt")

def dfs(node):



data = []
n = int(input())
for i in range(n):
    data.append(list(input()))

print(data)