import sys
sys.stdin = open("3431_input.txt")

for tc in range(int(input())):
    l, u, x = map(int, input().split())
    if x > u:
        result = -1
    elif x < l:
        result = l - x
    else:
        result = 0



    print(f"#{tc + 1} {result}")