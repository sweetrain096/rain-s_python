import sys
sys.stdin = open("base_input.txt")

encoding_dict = dict()
for i in range(26) :
    encoding_dict[chr(i+65)] = i
for i in range(26, 52) :
    encoding_dict[chr(i + 71)] = i
for i in range(52, 62):
    encoding_dict[chr(i-4)] = i
encoding_dict["+"] = 62
encoding_dict["/"] = 63

T = int(input())
for test_case in range(T):
    strings = input()
    new_strings = ""

    for string in strings:
        if len(str(bin(encoding_dict[string]))[2:]) <= 6:
            new_strings += str(0)*(6 - len(str(bin(encoding_dict[string]))[2:])) + str(bin(encoding_dict[string]))[2:]
    cnt = 0
    result = ""
    while True:
        result += chr(int('0b' + new_strings[cnt * 8 : (cnt + 1) * 8], 2))
        cnt += 1

        if (cnt + 1) * 8 >= len(new_strings):
            break

    print(f"#{test_case + 1} {result}.")