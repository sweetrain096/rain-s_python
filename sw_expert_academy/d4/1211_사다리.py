import sys
sys.stdin = open("1211_input.txt")


def find_min(start):
    c = start
    count = 0
    r = 0
    while r < 99:
        count += 1
        if count > cnt:
            return -1
        if c + 1 < 100 and Map[r][c + 1] == 1:
            while c + 1 < 100 and Map[r][c + 1] == 1:
                c += 1
                count += 1
            r += 1
        elif c - 1 >= 0 and Map[r][c - 1] == 1:
            while c - 1 >= 0 and Map[r][c - 1] == 1:
                c -= 1
                count += 1
            r += 1
        elif Map[r + 1][c] == 1:
            r += 1

    return count


for _ in range(10):
    tc = int(input())

    Map = []
    for _ in range(100):
        Map.append(list(map(int, input().split())))

    cnt = 10000
    result = 100

    for i in range(99, -1, -1):
        find_result = find_min(i)
        if find_result == -1:
            continue
        if find_result < cnt:
            cnt = find_result
            result = i




    print(f"#{tc} {result}")