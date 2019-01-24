import sys
sys.stdin = open("9_input.txt")

for test_case in range(int(input())):
    numbers = input()
    result = "No"
    if "9" in numbers:
        result = "Yes"
    print(f"#{test_case + 1} {result}")