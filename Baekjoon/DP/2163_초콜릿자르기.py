import sys
sys.stdin = open("2163_input.txt")

n, m = map(int, input().split())
print(n * m - 1)