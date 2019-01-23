import sys
sys.stdin = open("palindrome_input.txt")

T = int(input())
for test_case in range(T):
    string = input()
    i = 0
    while True:
        result = 0
        if string[i] != string[-(i+1)] :
            break
        i += 1
        if i == int(len(string) / 2) :
            result = 1
            break
    print(f"#{test_case + 1} {result}")