import sys
sys.stdin = open("6692_input.txt")

for tc in range(int(input())):
    sum_money = 0
    for n in range(int(input())):
        p, x = map(float, input().split())
        sum_money += p * x

    print(f"#{tc + 1} {round(sum_money, 6)}")
