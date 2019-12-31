import sys
sys.stdin = open("2819_input.txt")


deg = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def is_wall(r, c):
    if r < 0 or r >= 4 or c < 0 or c >= 4:
        return True
    return False

def make_number(r, c, num):
    if len(num) == 7:
        if not numbers.get(''.join(num)):
            numbers[''.join(num)] = 1
        return

    for dr, dc in deg:
        nr = r + dr
        nc = c + dc
        if not is_wall(nr, nc):
            num.append(str(Map[nr][nc]))
            make_number(nr, nc, num)

            num.pop()
for tc in range(int(input())):
    Map = []
    numbers = dict()
    for i in range(4):
        Map.append(list(map(int, input().split())))

    for r in range(4):
        for c in range(4):
            make_number(r, c, [str(Map[r][c])])

    print(f"#{tc + 1} {len(numbers)}")