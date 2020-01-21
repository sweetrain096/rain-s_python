import sys
sys.stdin = open("7465_input.txt")


def make_team(idx, i):
    visited[i] = 1

    team[idx].append(i)
    for check in people[i]:
        if not visited[check]:
            make_team(idx, check)
    people[i] = []


for tc in range(int(input())):
    n, m = map(int, input().split())

    people = [[]for _ in range(n + 1)]
    visited = [0 for _ in range(n + 1)]

    for i in range(m):
        me, you = map(int, input().split())
        people[me].append(you)
        people[you].append(me)

    # print(people)

    team = []
    idx = 0
    for i in range(1, n + 1):
        if people[i]:
            team.append([])
            make_team(idx, i)
            idx += 1
    # print(team)
    # print(visited)
    result = len(team)
    for i in range(1, n+1):
        if not visited[i]:
            result += 1

    print(f"#{tc + 1} {result}")