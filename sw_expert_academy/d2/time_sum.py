import sys
sys.stdin = open("time_input.txt")

for test_case in range(int(input())):
    t1, m1, t2, m2 = list(map(int, input().split()))
    new_m = m1 + m2
    if new_m >= 60 :
        new_m -= 60
        new_t = 1
    else :
        new_t = 0
    new_t += (t1 + t2)
    if new_t > 12:
        new_t -= 12

    print(f"#{test_case + 1} {new_t} {new_m}")