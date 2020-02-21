import sys
sys.stdin = open("5247_input.txt")

def inque(a):
    global wp
    Q[wp] = a
    wp += 1

def bfs():
    global rp
    inque(n)
    visited[n] = 1

    while rp < wp:
        t = Q[rp]
        rp += 1
        # t = Q.pop(0)
        for i in range(4):
            if not i:
                new = t + 1
            elif i == 1:
                new = t - 1
            elif i == 2:
                new = t * 2
            else:
                new = t - 10

            if new > 0 and new <= 1000000 and not visited[new]:
                inque(new)

                visited[new] = visited[t] + 1
            if new == m:
                return visited[new] - 1



for tc in range(int(input())):
    n, m = map(int, input().split())
    visited = [0] * 1000001
    Q = [0] * 1000000
    rp, wp = 0, 0
    print("#{} {}".format(tc + 1, bfs()))