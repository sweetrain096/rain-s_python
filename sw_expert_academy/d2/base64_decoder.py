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
print(encoding_dict)

T = int(input())
for test_case in range(T):
    strings = input()
    new_strings = ""

    for string in strings:
        new_strings += str(encoding_dict[string])

    print(new_strings)