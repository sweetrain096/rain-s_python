import sys
sys.stdin = open("1215_input.txt")

for tc in range(10):
    n = int(input())
    base = []
    for line in range(8):
        base.append(input())
    result = 0
    for row in range(8):
        for i in range(8 - n + 1):
            plus = 0

            while plus < n // 2:
                if base[row][i + plus] == base[row][i + n - plus - 1]:

                    plus += 1
                else:
                    plus = 0
                    break
            if plus == n // 2:
                result += 1

            plus = 0
            while plus < n // 2:

                if base[i + plus][row] == base[i + n - plus - 1][row]:
                    plus += 1
                else:
                    plus = 0
                    break
            if plus == n // 2:
                result += 1



    print(f"#{tc + 1} {result}")