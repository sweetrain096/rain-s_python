import sys
sys.stdin = open("samsung_bus_input.txt")

T = int(input())
for test_case in range(T):
    buses = [0 for i in range(5000)]

    for i in range(int(input())):
        a, b = list(map(int, input().split()))
        for j in range(a, b + 1):
            buses[j - 1] += 1

    P = int(input())
    result = []

    for i in range(P):
        result.append(buses[int(input())-1])

    result = " ".join(map(str, result))
    print(f"#{test_case + 1} {result}")
