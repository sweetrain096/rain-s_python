import sys
sys.stdin = open("1289_input.txt")

for tc in range(int(input())):
    strings = input()
    for char in range(len(strings)):
        if 1 + char != len(strings):
            if strings[-(1 + char)] != strings[-(2 + char)] and strings[-(2 + char)]=='1':
                print(strings[-(2 + char)], len(strings[-(1 + char):]), strings[-(2 + char)] * len(strings[-(1 + char):]))
                strings[-(1 + char):] = strings[-(2 + char)] * len(strings[-(1 + char):])


        print(strings)
    print(f"#{tc + 1}")