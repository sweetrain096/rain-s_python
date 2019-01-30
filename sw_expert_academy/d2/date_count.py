import sys
sys.stdin = open("date_count_input.txt")

for test_case in range(int(input())):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    m1, d1, m2, d2 = list(map(int, input().split()))
    d_days = 0

    if m1 == m2:
        d_days = d2 - d1 + 1
    else:
        if not m2 - m1 == 1:
            for month in range(m1 + 1, m2):
                d_days += days[month - 1]
        d_days += days[m1 - 1] - d1 + 1
        d_days += d2

    print(f"#{test_case + 1} {d_days}")