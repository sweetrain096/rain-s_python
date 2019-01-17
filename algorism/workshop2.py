import sys
sys.stdin = open("flatten_input.txt")

for test_case in range(10):
    final_count = int(input())
    tests = list(map(int, input().split()))

    for cnt in range(final_count + 1) :

        max_num = tests[0]
        max_index = 0
        min_num = tests[0]
        min_index = 0

        for i in range(100) :
            if max_num <= tests[i] :
                max_num = tests[i]
                max_index = i
            if min_num >= tests[i] :
                min_num = tests[i]
                min_index = i

        tests[max_index] -= 1
        tests[min_index] += 1

    print(f"#{test_case + 1} {max_num - min_num}")
