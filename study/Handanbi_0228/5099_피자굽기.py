import sys
sys.stdin = open("5099_input.txt")

for tc in range(int(input())):
    n, m = map(int, input().split())
    cheese_list = list(map(int, input().split()))
    Q = [0] * n
    index = 0
    while True:
        # print(Q)
        if len(Q) == 1:
            result = Q[0][1]
            break
        if cheese_list and Q[0] == 0:
            index += 1
            Q.pop(0)
            Q.append([cheese_list.pop(0), index])
        elif cheese_list and len(Q) < n:
            index += 1
            Q.append([cheese_list.pop(0), index])

        elif Q[0] != 0:
            now = Q.pop(0)
            now_cheese = now[0] // 2
            if now_cheese:
                Q.append([now_cheese, now[1]])

    print(f"#{tc + 1} {result}")