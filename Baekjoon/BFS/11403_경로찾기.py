import sys
sys.stdin = open("11403_input.txt")

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

