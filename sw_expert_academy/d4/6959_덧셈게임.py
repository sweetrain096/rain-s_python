import sys
sys.stdin = open("6959_input.txt")

for tc in range(int(input())):
    testcase = list(input())
    while len(testcase) > 1:
        for i in range(1, len(testcase)):
            if not int(testcase[i - 1]) + int(testcase[i]):


    print(f"#{tc + 1} {testcase}")