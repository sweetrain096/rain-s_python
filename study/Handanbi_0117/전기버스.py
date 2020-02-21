import sys
sys.stdin = open("bus_input.txt")

T = int(input())
for test_case in range(T):
    K, N, M = list(map(int, input().split()))
    charge_list = list(map(int, input().split()))
    bus_stop = [i for i in range(N + 1)]
    charge_stops = [0] * (N + 1)
    for charge_stop in charge_list :
        charge_stops[charge_stop] = 1

    cnt = 0
    now = 0
    while True:
        if now + K >= N :
            break
        check = set(charge_stops[now + 1 : now + 1 + K])
        if charge_stops[now + K] :
            now += K
            cnt += 1
        elif not check - set([0]) :
            cnt = 0
            break
        else :
            for i in range(K, 0, -1):
                if charge_stops[now + i]:
                    now += i
                    cnt += 1
                    break

    print(f"#{test_case + 1} {cnt}")