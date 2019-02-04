import sys
sys.stdin = open("5162_input.txt")

for tc in range(int(input())):
    a, b, c = map(int, input().split())
    result1 = (c // b) + ((c % b) // a)
    result2 = (c // a) + ((c % a) // b)

    if result1 <= result2:
        result = result2
    else:
        result = result1

    print(f"#{tc + 1} {result}")