import sys
sys.stdin = open("17471_input.txt")
n = int(input())
Graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
population = [0]+list(map(int, input().split()))
A = [0 for _ in range(n+1)]
B = [0 for _ in range(n+1)]

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(1, len(data)):
        Graph[i+1][data[j]] = 1
        Graph[data[j]][i+1] = 1

for i in Graph:
    print(i)