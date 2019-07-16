import sys
sys.stdin = open("test_input.txt")

for test_case in range(int(input())):
    new_numbers = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
    test, n = list(input().split())
    n = int(n)
    numbers = list(input().split())
    result = []


    for now in range(10):
        cnt = 0
        for number in range(n):
            if new_numbers[now] == numbers[number]:
                result.append(new_numbers[now])



    print(f"{test} {' '.join(result)}")