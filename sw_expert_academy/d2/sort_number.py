import sys
sys.stdin = open("sort_number_input.txt")

for test_case in range(int(input())):
    n = int(input())
    numbers = list(map(int, input().split()))
    numbers.sort()
    print(f"#{test_case + 1} {' '.join(map(str, numbers))}")