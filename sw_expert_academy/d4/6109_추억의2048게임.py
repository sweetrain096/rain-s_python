import sys
sys.stdin = open("6109_input.txt")
dg = [[0, 1], [0, -1], [1, 0], [-1, 0]]

def is_wall(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True
    return False

for tc in range(int(input())):
    inputs = input().split()
    n = int(inputs[0])

    if inputs[1] == 'up':
        direction = dg[2]
    else:
        direction = dg[3]

    Map = []
    for i in range(n):
        Map.append(list(map(int, input().split())))


    # dr, dc = direction

    # 왼쪽
    if inputs[1] == 'left':
        index = 0
        dr, dc = dg[0]
        for row in range(n):
            idx = n
            for col in range(n):
                if not Map[row][col] and idx == n:
                    idx = col
                elif Map[row][col] and idx < col:
                    Map[row][idx] = Map[row][col]
                    Map[row][col] = 0
                    idx += 1

        for col in range(n-1):
            for row in range(n):
                if Map[row][col] == Map[row+dr][col+dc]:
                    Map[row][index] = Map[row][col] + Map[row+dr][col+dc]
                    Map[row + dr][col + dc] = 0
            index += 1

        for row in range(n):
            idx = n
            for col in range(n):
                if not Map[row][col] and idx == n:
                    idx = col
                elif Map[row][col] and idx < col:
                    Map[row][idx] = Map[row][col]
                    Map[row][col] = 0
                    idx += 1
    # 오른쪽
    elif inputs[1] == 'right':
        index = n-1
        dr, dc = dg[1]

        for row in range(n):
            idx = -1
            for col in range(n-1, -1, -1):
                if not Map[row][col] and idx == -1:
                    idx = col
                elif Map[row][col] and idx > col:
                    Map[row][idx] = Map[row][col]
                    Map[row][col] = 0
                    idx -= 1

        for col in range(n-1, 0, -1):
            for row in range(n):
                if Map[row][col] == Map[row+dr][col+dc]:
                    Map[row][index] = Map[row][col] + Map[row+dr][col+dc]
                    Map[row + dr][col + dc] = 0
            index -= 1

        for row in range(n):
            idx = -1
            for col in range(n-1, -1, -1):
                if not Map[row][col] and idx == -1:
                    idx = col
                elif Map[row][col] and idx > col:
                    Map[row][idx] = Map[row][col]
                    Map[row][col] = 0
                    idx -= 1

    # 위
    elif inputs[1] == 'up':
        index = 0
        dr, dc = dg[2]
        for col in range(n):
            idx = n
            for row in range(n):
                if not Map[row][col] and idx == n:
                    idx = row
                elif Map[row][col] and idx < row:
                    Map[idx][col] = Map[row][col]
                    Map[row][col] = 0
                    idx += 1

        for row in range(n-1):
            for col in range(n):
                if Map[row][col] == Map[row+dr][col+dc]:
                    Map[index][col] = Map[row][col] + Map[row+dr][col+dc]
                    Map[row + dr][col + dc] = 0
            index += 1

        for col in range(n):
            idx = n
            for row in range(n):
                if not Map[row][col] and idx == n:
                    idx = row
                elif Map[row][col] and idx < row:
                    Map[idx][col] = Map[row][col]
                    Map[row][col] = 0
                    idx += 1

    # 아래
    else:
        index = n-1
        dr, dc = dg[3]

        for col in range(n):
            idx = -1
            for row in range(n-1, -1, -1):
                if not Map[row][col] and idx == -1:
                    idx = row
                elif Map[row][col] and idx > row:
                    Map[idx][col] = Map[row][col]
                    Map[row][col] = 0
                    idx -= 1

        for row in range(n - 1, 0, -1):
            for col in range(n):
                if Map[row][col] == Map[row + dr][col + dc]:
                    Map[index][col] = Map[row][col] + Map[row + dr][col + dc]
                    Map[row + dr][col + dc] = 0
            index -= 1

        for col in range(n):
            idx = -1
            for row in range(n-1, -1, -1):
                if not Map[row][col] and idx == -1:
                    idx = row
                elif Map[row][col] and idx > row:
                    Map[idx][col] = Map[row][col]
                    Map[row][col] = 0
                    idx -= 1

    print(f"#{tc + 1}")
    for line in Map:
        print(' '.join(map(str, line)))
