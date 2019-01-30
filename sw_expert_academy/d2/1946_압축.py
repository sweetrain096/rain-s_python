import sys
sys.stdin = open("1946_input.txt")

for test_case in range(int(input())):
    result =""
    for test in range(int(input())):
        string, number = list(input().split())
        number = int(number)
        result += string * number

    print(f"#{test_case + 1}")
    for i in range(len(result)//10) :
        print(f"{result[i * 10 : i * 10 + 10]}")
    print(f"{result[i * 10 + 10 :]}")