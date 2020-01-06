import sys
sys.stdin = open("1824_input.txt")


def is_num(char):
    if ord(char) >= ord('0') and ord(char) <= ord('9'):
        return True
    return False


def move(nr, nc):
    if nr >= r:
        nr = 0
    elif nr < 0:
        nr = r - 1
    elif nc >= c:
        nc = 0
    elif nc < 0:
        nc = c - 1
    return nr, nc


def verify(now, nr, nc, dir, dir_n, dr, dc, memory):
    if visited[nr][nc]:
        for i in visited[nr][nc]:
            if i[0] == memory and i[1] == dir_n:
                return False
    visited[nr][nc].append((memory, dir_n))

    while True:
        # print(now, nr, nc, memory)
        if now == '@':
            return True

        # 숫자일때
        if is_num(now):
            memory = int(now)

        # 방향일 때
        if now in ['^', 'v', '<', '>']:
            if now == '^':
                dir = deg[0]
                dir_n = 0
            elif now == 'v':
                dir = deg[1]
                dir_n = 1
            elif now == '<':
                dir = deg[2]
                dir_n = 2
            else:
                dir = deg[3]
                dir_n = 3

            dr, dc = dir

        # 더하기, 빼기 일 때
        if now == '+':
            memory += 1
            if memory == 16:
                memory = 0

        if now == '-':
            memory -= 1
            if memory == -1:
                memory = 15

        # 메모리 따른 방향 변화
        if now == '_':
            if memory:
                dir = deg[2]
                dir_n = 2
            else:
                dir = deg[3]
                dir_n = 3
            dr, dc = dir
        if now == '|':
            if memory:
                dir = deg[0]
                dir_n = 0
            else:
                dir = deg[1]
                dir_n = 1
            dr, dc = dir

        if now == '?':
            for i in range(4):
                dr, dc = deg[i]
                tempr, tempc = move(nr + dr, nc + dc)

                if Map[tempr][tempc] == '@':
                    return True

            for i in range(4):
                dr, dc = deg[i]
                tempr, tempc = move(nr + dr, nc + dc)
                is_visit = False
                if visited[tempr][tempc]:
                    for j in visited[tempr][tempc]:
                        if j[0] == memory and j[1] == i:
                            is_visit = True
                            break
                if not is_visit:
                    flag = verify(Map[tempr][tempc], tempr, tempc, deg[i], i, dr, dc, memory)
                    if flag:
                        return True
            return False

        nr, nc = move(nr + dr, nc + dc)
        now = Map[nr][nc]
        if not visited[nr][nc]:
            visited[nr][nc].append((memory, dir_n))
        else:
            for check in visited[nr][nc]:
                if check[0] == memory and check[1] == dir_n:
                    return False


# 상하좌우 순서
deg = [(-1, 0), (1, 0), (0, -1), (0, 1)]

for TC in range(int(input())):
    r, c = map(int, input().split())
    Map = [["" for _ in range(c)] for _ in range(r)]
    visited = [[[] for _ in range(c)] for _ in range(r)]
    for row in range(r):
        temp = input()
        for col in range(c):
            Map[row][col] = temp[col]

    now = Map[0][0]
    nr, nc = 0, 0
    dir = deg[3]
    dr, dc = dir[0], dir[1]
    memory = 0
    end = False
    endr, endc = 0, 0


    for row in range(r):
        for col in range(c):
            if Map[row][col] == '@':
                end = True
                endr, endc = row, col
                break
        if end:
            break

    if end:
        # 끝내기 표시 위 방향 이상한 것 잡기
        end_flag = 0
        for i in range(4):
            rr, rc = deg[i]
            tr, tc = move(endr + rr, endc + rc)
            if i == 0:
                if Map[tr][tc] in ['>', '<', '^']:
                    end_flag += 1
            elif i == 1:
                if Map[tr][tc] in ['>', '<', 'v']:
                    end_flag += 1
            elif i == 2:
                if Map[tr][tc] in ['^', 'v', '<']:
                    end_flag += 1
            else:
                if Map[tr][tc] in ['^', 'v', '>']:
                    end_flag += 1
        if end_flag != 4:
            result = verify(now, nr, nc, dir, 3, dr, dc, memory)
        else:
            result = False
    else:
        result = False



    #
    # for i in Map:
    #     print(i)

    print(f"#{TC + 1} {'YES' if result else 'NO'}")
