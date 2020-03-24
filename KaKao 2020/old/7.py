board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]
import pprint


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

rr1 = [1, 0, -1]
rc1 = [-1, -2, -1]
rr2 = [1, 0, -1]
rc2 = [1, 2, 1]



Q = []
def is_wall(r, c, N):
    if r < 0 or r >= N or c < 0 or c >= N:
        return True
    return False


def bfs(r1, c1, r2, c2, visit, N, board):

    Q.append([r1, c1, r2, c2])
    visit[r1][c1] = 1
    visit[r2][c2] = 1
    while Q:
        r1, c1, r2, c2 = Q.pop(0)
        cnt = max(visit[r1][c1], visit[r2][c2])


        # 이동
        for i in range(4):
            nr, nc = dr[i], dc[i]
            nr1, nc1 = r1 + nr, c1 + nc
            nr2, nc2 = r2 + nr, c2 + nc
            if is_wall(nr1, nc1, N) or is_wall(nr2, nc2, N):
                continue
            if board[nr1][nc1] or board[nr2][nc2]:
                continue
            if visit[nr1][nc1] and visit[nr2][nc2]:
                continue
            Q.append([nr1, nc1, nr2, nc2])
            visit[nr1][nc1] = cnt+1
            visit[nr2][nc2] = cnt+1


        # 회전
        # 1번 기준으로 2번만 움직일때
        for i in range(3):
            nr, nc = rr1[i], rc1[i]
            nr1, nc1 = r1, c1
            nr2, nc2 = r2 + nr, c2 + nc
            if is_wall(nr1, nc1, N) or is_wall(nr2, nc2, N):
                continue
            if board[nr1][nc1] or board[nr2][nc2]:
                continue
            if visit[nr1][nc1] and visit[nr2][nc2]:
                continue
            Q.append([nr1, nc1, nr2, nc2])
            visit[nr1][nc1] = cnt+1
            visit[nr2][nc2] = cnt+1


        for i in range(3):
            nr, nc = rr2[i], rc2[i]
            nr1, nc1 = r1 + nr, c1 + nc
            nr2, nc2 = r2, c2
            if is_wall(nr1, nc1, N) or is_wall(nr2, nc2, N):
                continue
            if board[nr1][nc1] or board[nr2][nc2]:
                continue
            if visit[nr1][nc1] and visit[nr2][nc2]:
                continue
            Q.append([nr1, nc1, nr2, nc2])
            visit[nr1][nc1] = cnt+1
            visit[nr2][nc2] = cnt+1


    return cnt - 1


def solution(board):
    answer = 0
    N = len(board)
    visit = [[0 for _ in range(N)] for _ in range(N)]


    answer = bfs(0, 0, 0, 1, visit, N, board)


    return answer


print(solution(board))