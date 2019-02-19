import sys
sys.stdin = open("1220_input.txt")
for tc in range(10):
    n = input()
    base = []
    for row in range(100):
        base.append(list(map(int, input().split())))
    result = 0
    for col in range(100):
        plus_0, plus_1, plus_2 = 0, 0, 0
        for row in range(100):
            now = base[row][col]
            if now == 1:
                plus_1 += 1
            elif now == 2:
                plus_2 += 1
            last = base[row][col]

    print(f"#{tc + 1} ")