from collections import deque


def bfs(c_start, b_start):
    global time

    c_list = deque()
    c_list.append(c_start)
    b_list = deque()
    b_list.append(b_start)
    b_visited[b_start] = 1
    check = b_start

    while b_list:
        t = b_list.popleft()
        # print(time + 1, t, b_list, c_list)
        if t == c_list[-1]:
            return time + 1
        if t - 1 >= 0 and not b_visited[t - 1]:
            b_list.append(t - 1)
            b_visited[t - 1] = 1
        if t + 1 <= 200000 and not b_visited[t + 1]:
            b_list.append(t + 1)
            b_visited[t + 1] = 1
        if t * 2 <= 200000 and not b_visited[t * 2]:
            b_list.append(t * 2)
            b_visited[t * 2] = 1

        if t == check:
            time += 1
            check = b_list[-1]
            c_list.append(c_list[-1] + time + 1)

    return


# c, b = map(int, input().split())
c, b = 11, 2
b_visited = [0] * 200010
time = -1
print(bfs(c, b))