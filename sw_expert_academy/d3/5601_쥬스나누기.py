import sys
sys.stdin = open("5601_input.txt")

for tc in range(int(input())):
    n = int(input())
    result = [f'1/{n}']*n

    print(f"#{tc + 1} {' '.join(result)}")