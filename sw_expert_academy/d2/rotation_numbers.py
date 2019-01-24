import sys
sys.stdin = open("rotation_input.txt")

for test_case in range(int(input())):
    n = int(input())
    numbers = []
    rotation_90 = []
    rotation_180 = []
    rotation_270 = []
    for i in range(n):
        numbers.append(list(map(int, input().split())))
