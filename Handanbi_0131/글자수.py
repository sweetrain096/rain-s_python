import sys
sys.stdin = open("len_input.txt")

for test_case in range(int(input())):
    str1 = list(set(input()))
    str2 = input()
    check = [0] * len(str1)
    for char in range(len(str1)):
        for char2 in str2:
            if str1[char] == char2 :
                check[char] += 1
    result = max(check)

    print(f"#{test_case + 1} {result}")