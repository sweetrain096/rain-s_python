import sys
sys.stdin = open("1220_input.txt")

for tc in range(10):
    n = input()
    table = []
    for input_table in range(100):
        table.append(list(map(int, input().split())))
    result = 0
    for col in range(100):
        last = -1
        now = -1
        for row in range(100):
            if table[row][col]:
                now = table[row][col]
            if last == 1 and now == 2:
                result += 1


            last = now


    print(f"#{tc + 1} {result}")

