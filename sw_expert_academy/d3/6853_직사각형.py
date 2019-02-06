import sys
sys.stdin = open("6853_input.txt")

for tc in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    result = [0] * 3
    for n in range(int(input())):
        x, y = map(int, input().split())
        if x1 < x < x2 and y1 < y < y2:
            result[0] += 1
        elif (x1 <= x <= x2 and (y1 == y or y2 == y)) or (y1 <= y <= y2 and (x1 == x or x2 == x)):
            result[1] += 1
        else:
            result[2] += 1




    print(f"#{tc + 1} {' '.join(map(str, result))}")