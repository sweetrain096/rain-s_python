import sys
sys.stdin = open("6959_input.txt")

for tc in range(int(input())):
    start = 0
    testcase = list(map(int, list(input())))
    # print(testcase)
    while len(testcase) > 1:
        temp = 20
        idx = 0
        for i in range(len(testcase) - 1):
            if temp > testcase[i] + testcase[i + 1]:
                temp = testcase[i] + testcase[i + 1]
                idx = i
        plus = testcase[idx] + testcase[idx + 1]
        testcase.pop(idx)
        testcase.pop(idx)
        if plus >= 10:
            testcase.insert(idx, 1)
            testcase.insert(idx + 1, plus % 10)
        else:
            testcase.insert(idx, plus)
        # print(testcase, start)
        start = (start + 1) % 2


    print(f"#{tc + 1} {'A' if start else 'B'}")