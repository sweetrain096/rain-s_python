import sys
sys.stdin = open("1289_input.txt")

for tc in range(int(input())):
    strings = list(input())
    result = 0
    for char in range(len(strings)):
        if 1 + char != len(strings):
            if strings[-(1 + char)] != strings[-(2 + char)]:
                if strings[-(2 + char)] == '1':
                    # print(strings[-(2 + char)], len(strings[-(1 + char):]), strings[-(2 + char)] * len(strings[-(1 + char):]))
                    strings[-(1 + char):] = strings[-(2 + char)] * len(strings[-(1 + char):])
                    result += 1
                else:
                    # print(strings[-(2 + char)], len(strings[-(1 + char):]), strings[-(2 + char)] * len(strings[-(1 + char):]))
                    strings[-(1 + char):] = strings[-(2 + char)] * len(strings[-(1 + char):])
                    result += 1
        if strings[-(1 + char)] == '1' and (1 + char) == len(strings):
            strings[:] = '0' * (1 + char)
            result += 1
        # print(strings)
    print(f"#{tc + 1} {result}")