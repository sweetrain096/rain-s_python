import sys
sys.stdin = open("17070_input.txt")


def is_wall(r, c):
    if r<0 or r>= n or c < 0 or c>= n:
        return True
    return False


def backtracking(hr, hc, tr, tc):
    global cnt
    visit[hr][hc] = 1
    # print(hr, hc, tr, tc)
    # for i in range(n):
    #     print(visit[i])
    # print()
    if hr == n-1 and hc == n-1:
        cnt += 1
    # all
    if not is_wall(hr+1, hc+1) and not visit[hr+1][hc+1]:
        if not Map[hr+1][hc+1] and not Map[hr+1][hc] and not Map[hr][hc+1]:
            backtracking(hr+1, hc+1, hr, hc)
    # 가로
    if hr == tr or (hr == tr + 1 and hc == tc + 1):
        if not is_wall(hr, hc+1) and not visit[hr][hc+1]:
            if not Map[hr][hc+1]:
                backtracking(hr, hc+1, hr, hc)
    # 세로
    if hc == tc or (hr == tr + 1 and hc == tc + 1):
        if not is_wall(hr+1, hc) and not visit[hr+1][hc]:
            if not Map[hr+1][hc]:
                backtracking(hr+1, hc, hr, hc)


    visit[hr][hc] = 0


n = int(input())
Map = []

for i in range(n):
    Map.append(list(map(int, input().split())))

visit = [[0 for _ in range(n)] for _ in range(n)]
cnt = 0

backtracking(0, 1, 0, 0)



print(cnt)