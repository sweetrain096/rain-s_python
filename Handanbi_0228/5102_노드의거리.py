import sys
sys.stdin = open("5102_input.txt")

for tc in range(int(input())):
    v, e = map(int, input().split())
    table = [[0 for _ in range(v)] for _ in range(v)]
    for i in range(e):
        num1, num2 = map(int, input().split())
        table[num1 - 1][num2 - 1] = 1
    s, g = map(int, input().split())
