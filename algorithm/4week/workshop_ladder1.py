import sys
sys.stdin = open("ladder_input.txt")

for t in range(10):
    tc = int(input())
    ladders = []
    for i in range(100):
        ladders.append(list(map(int, input().split())))
    ladders = ladders[::-1]



    for col in range(100):
        if ladders[0][col] == 2:
            index = col
    for row in range(1, 100):
        # print(index)

        if ladders[row][index - 1] and index != 0:
            while ladders[row][index - 1] and index != 0:
                index = index - 1
        elif index != 99 and ladders[row][index + 1]:
            while index != 99 and ladders[row][index + 1]:
                index = index + 1

    print(f"#{tc} {index}")


