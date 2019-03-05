import sys
sys.stdin = open("12761_input.txt")

def check(number):
    if number >= 0 and number <= 100000:
        if not visited[number]:
            return True
    return False


def bfs(a, b, n, m):
    Q = [n]
    visited[n] = 1
    check_cnt = Q[-1]
    cnt = 0
    order = ["-1", "+1"]
    while cnt <= 1:
        t = Q.pop(0)
        if t == 
        for i in order:
            if check(t + int(i)):
                Q.append(t + int(i))
                visited[t + int(i)] = 1
        if check(t + a):
            Q.append(t + a)
            visited[t + a] = 1
        if check(t - a):
            Q.append(t - a)
            visited[t - a] = 1
        if check(t * a):
            Q.append(t * a)
            visited[t * a] = 1
        if check(t + b):
            Q.append(t + b)
            visited[t + b] = 1
        if check(t - b):
            Q.append(t - b)
            visited[t - b] = 1
        if check(t * b):
            Q.append(t * b)
            visited[t * b] = 1

        if check_cnt == t:
            cnt += 1
            print(check_cnt, Q[-1])
            check_cnt = Q[-1]

        print(Q)
        print(cnt)



a, b, n, m = map(int, input().split())
visited = [0 for _ in range(100001)]
bfs(a, b, n, m)