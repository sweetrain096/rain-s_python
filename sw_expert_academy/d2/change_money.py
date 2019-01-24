import sys
sys.stdin = open("money_input.txt")

for test_case in range(int(input())):
    changes = [0] * 8
    n = int(input())
    if n >= 50000:
        changes[0] += n // 50000
        n = n % 50000
    if n >= 10000:
        changes[1] += n // 10000
        n = n % 10000
    if n >= 5000:
        changes[2] += n // 5000
        n = n % 5000
    if n >= 1000:
        changes[3] += n // 1000
        n = n % 1000
    if n >= 500:
        changes[4] += n // 500
        n = n % 500
    if n >= 100:
        changes[5] += n // 100
        n = n % 100
    if n >= 50:
        changes[6] += n // 50
        n = n % 50
    if n >= 10:
        changes[7] += n // 10

    print(f"#{test_case + 1}\n{' '.join(map(str, changes))}")