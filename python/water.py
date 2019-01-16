test_case = int(input())
for test in range(test_case):
    cost_A, cost_B = 0, 0
    p, q, r, s, w = list(map(int, input().split()))
    cost_A = p * w
    cost_B = q
    if w > r :
        cost_B += s * (w - r)

    if cost_A <= cost_B :
        print(f"#{test + 1} {cost_A}")
    else :
        print(f"#{test + 1} {cost_B}")