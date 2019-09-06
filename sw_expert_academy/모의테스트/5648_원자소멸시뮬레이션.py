import sys
sys.stdin = open("5648_input.txt")

def DFS():

for tc in range(int(input())):
    n = int(input())
    Map = [[0 for i in range(2010)] for j in range(2010)]
    for cnt in range(n):
        x, y, deg, K = list(map(int, input().split()))
        Map[x+1000][y+1000] = [deg, K]
