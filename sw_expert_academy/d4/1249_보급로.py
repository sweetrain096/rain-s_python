import sys
sys.stdin = open("1249_input.txt")

deg = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def is_wall(r, c):
    if r < 0 or r >= n or c < 0 or c >= n:
        return True
    return False


def bfs():
    q = [start]
    costs[0][0] = 0
    while q:
        tr, tc = q.pop(0)
        n_cost = costs[tr][tc]
        for dr, dc in deg:
            nr = tr + dr
            nc = tc + dc
            if not is_wall(nr, nc):
                if nr + nc == 0:
                    continue
                if costs[nr][nc] > n_cost + Map[nr][nc]:
                    costs[nr][nc] = n_cost + Map[nr][nc]
                    q.append((nr, nc))
    return costs[n-1][n-1]




for tc in range(int(input())):
    n = int(input())
    Map = []
    costs = [[1000000 for _ in range(n)] for _ in range(n)]
    start = (0, 0)
    end = (n - 1, n - 1)
    for i in range(n):
        line = input()
        tmp = []
        for j in line:
            tmp.append(int(j))
        Map.append(tmp)

    # print(Map)


    print(f"#{tc + 1} {bfs()}")








'''
class Heap:
    def __init__(self, n):
        self.__heapsize = 0
        self.__container = [None for _  in range(n * n)]

    def __get_par(self, node):
        return node // 2

    def push(self, pri):
        self.__heapsize += 1
        cur = self.__heapsize
        self.__container[cur] = pri
        par = self.__get_par(cur)

        while cur != 1:
            if self.__container[par] <= self.__container[cur]:
                break

deg = [(0, 1), (1, 0), (0, -1), (-1, 0)]




def bfs():
    dist = [[9999 for _ in range(n)] for _ in range(n)]
    p = [[None for _ in range(n)] for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]

    dist[0][0] = 0
    visited[0][0] = 1
    p[0][0] = None

    return
'''